import json
import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

def load_all_data():
    with open(os.path.join(DATA_DIR, "perfil_investidor.json"), encoding="utf-8") as f:
        perfil = json.load(f)

    with open(os.path.join(DATA_DIR, "produtos_financeiros.json"), encoding="utf-8") as f:
        produtos = json.load(f)

    transacoes = pd.read_csv(os.path.join(DATA_DIR, "transacoes.csv"))
    historico  = pd.read_csv(os.path.join(DATA_DIR, "historico_atendimento.csv"))

    return {
        "perfil": perfil,
        "produtos": produtos,
        "transacoes": transacoes,
        "historico": historico,
    }
