from modulo import carrega_conteudos_json
import pprint
import json

def exibir_conteudos_json():
    """
    Recebe um arquivo json por input do usuário e lê o seu conteúdo fazendo o tratamento de erros adequado.
    """
    try:
        pprint.pprint(carrega_conteudos_json(input("Coloque o nome do arquivo: ")))
    except TypeError:
        print("O parâmetro `arquivo` não era uma string.")
        exibir_conteudos_json()
    except FileNotFoundError:
        print("O arquivo não pode ser encontrado.")
        exibir_conteudos_json()
    except IsADirectoryError:
        print("A string passada representa um diretório.")
        exibir_conteudos_json()
    except PermissionError:
        print("Não há autorização para acessar o arquivo.")
        exibir_conteudos_json()
    except OSError:
        print("Houve um problema do Sistema Operacional durante a leitura do arquivo.")
        exibir_conteudos_json()
    except json.JSONDecodeError:
        print("Os conteúdos dentro do arquivo não estavam no formato de um `json`.")
        exibir_conteudos_json
    

exibir_conteudos_json()
