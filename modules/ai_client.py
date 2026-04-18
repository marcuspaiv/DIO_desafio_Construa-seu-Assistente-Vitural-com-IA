import streamlit as st
import json

def build_system_prompt(data: dict) -> str:
    perfil   = data["perfil"]
    produtos = data["produtos"]

    produtos_txt = "\n".join(
        f"- {p['nome']} | risco: {p['risco']} | rentabilidade: {p['rentabilidade']} "
        f"| aporte mínimo: R$ {p['aporte_minimo']} | indicado para: {p['indicado_para']}"
        for p in produtos
    )

    metas_txt = "\n".join(
        f"- {m['meta']}: R$ {m['valor_necessario']:,.2f} até {m['prazo']}"
        for m in perfil.get("metas", [])
    )

    reserva_atual    = perfil["reserva_emergencia_atual"]
    reserva_objetivo = next(
        (m["valor_necessario"] for m in perfil["metas"] if "reserva" in m["meta"].lower()), 15000
    )
    progresso = (reserva_atual / reserva_objetivo) * 100

    return f"""Você é o FinBot, um assistente financeiro pessoal simpático, direto e confiável.
Você conhece profundamente o perfil do cliente e deve sempre personalizar suas respostas.

## PERFIL DO CLIENTE
- Nome: {perfil['nome']}
- Idade: {perfil['idade']} anos
- Profissão: {perfil['profissao']}
- Renda mensal: R$ {perfil['renda_mensal']:,.2f}
- Perfil investidor: {perfil['perfil_investidor']}
- Aceita risco: {"Sim" if perfil['aceita_risco'] else "Não"}
- Patrimônio total: R$ {perfil['patrimonio_total']:,.2f}
- Reserva de emergência atual: R$ {reserva_atual:,.2f} ({progresso:.1f}% da meta)

## METAS
{metas_txt}

## PRODUTOS DISPONÍVEIS
{produtos_txt}

## REGRAS DE COMPORTAMENTO
1. Sempre use dados reais do perfil do cliente nas respostas.
2. Seja objetivo — respostas curtas e claras, em português do Brasil.
3. Nunca invente dados; se não souber algo, diga claramente.
4. Ao recomendar produtos, considere o perfil moderado e a aversão a risco.
5. Use emojis moderadamente para tornar a conversa mais amigável.
6. Para cálculos de metas, use os valores reais do perfil.
"""


def get_ai_response(prompt: str, data: dict) -> str:
    system = build_system_prompt(data)
    provider = st.session_state.get("ai_provider", "groq")

    if provider == "groq":
        return _groq_response(system, prompt)
    else:
        return _ollama_response(system, prompt)


def _groq_response(system: str, prompt: str) -> str:
    try:
        from groq import Groq
        api_key = st.session_state.get("groq_key", "")
        if not api_key:
            return (
                "⚠️ **Chave Groq não configurada.**\n\n"
                "Adicione sua API Key gratuita na barra lateral.\n"
                "Acesse [console.groq.com](https://console.groq.com) para obter a chave."
            )

        client = Groq(api_key=api_key)
        history = st.session_state.get("messages", [])

        messages = [{"role": "system", "content": system}]
        for msg in history[-10:]:  # últimas 10 mensagens para contexto
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            max_tokens=1024,
            temperature=0.7,
        )
        return response.choices[0].message.content

    except ImportError:
        return "❌ Pacote `groq` não instalado. Execute: `pip install groq`"
    except Exception as e:
        return f"❌ Erro ao chamar Groq API: {str(e)}"


def _ollama_response(system: str, prompt: str) -> str:
    try:
        import ollama
        model = st.session_state.get("ollama_model", "llama3.2")
        history = st.session_state.get("messages", [])

        messages = [{"role": "system", "content": system}]
        for msg in history[-10:]:
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": prompt})

        response = ollama.chat(model=model, messages=messages)
        return response["message"]["content"]

    except ImportError:
        return "❌ Pacote `ollama` não instalado. Execute: `pip install ollama`"
    except Exception as e:
        return f"❌ Erro ao chamar Ollama: {str(e)}\n\nVerifique se o Ollama está rodando (`ollama serve`)."
