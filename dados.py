import json
import os


ARQUIVO_DADOS = "dados.json"


def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        for casal, gls in dados.items():
            novas_gls = []

            for gl in gls:
                if isinstance(gl, str):
                    novas_gls.append({
                        "nome": gl,
                        "status": "Quero assistir"
                    })
                else:
                    novas_gls.append(gl)

            dados[casal] = novas_gls

        salvar_dados(dados)
        return dados

    return {}


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4
        )