import json


def salvar_historico(linha: str, caminho_arquivo: str) -> None:
    arquivo = open(caminho_arquivo, 'a')
    arquivo.write(f'{linha}\n')
    arquivo.close()


def ler_historico(caminho_arquivo: str) -> list:
    lista_linhas_arquivo = []
    arquivo = open(caminho_arquivo, 'r')
    for linha in arquivo:
        linha_json = linha.strip()
        linha_json_2 = json.loads(linha_json)
        lista_linhas_arquivo.append(linha_json_2)
    arquivo.close()
    return lista_linhas_arquivo


def ler_log(caminho) -> list:
    lista_linhas_arquivo = []
    arquivo = open(caminho, 'r')
    for linha in arquivo:
        linha_limpa = linha.strip()  # retira caracteres de escape e espacos branco (\n \t \r ' ')
        lista_linhas_arquivo.append(linha_limpa)
    arquivo.close()
    return lista_linhas_arquivo
