import requests

def ler_moeda(moedas_disponiveis):
    if not moedas_disponiveis:
        return None
    while True:
        moeda_base = input('Informe a moeda base: ').upper().strip()
        moeda_destino = input('Informe a moeda destino: ').upper().strip()
        if moeda_base in moedas_disponiveis and moeda_destino in moedas_disponiveis and moeda_base != moeda_destino:
            return moeda_base, moeda_destino
        else:
            print("Moeda inválida, tente novamente.")


def ler_valor(moeda_base):
    while True:
        valor = input(f'Valor em {moeda_base}: ').replace(',', '.')
        try:
            msg = float(valor)
            if msg > 0:
                return msg
            else:
                print('Valor deve ser maior do que 0, tente novamente')
        except ValueError:
            print("Valor inválido, tente novamente")


def fazer_requisicao(link_api, parametros=None):
    try:
        resposta = requests.get(link_api, params=parametros, timeout=10)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.Timeout:
        print("A API demorou muito para responder.")
        return None
    except requests.exceptions.ConnectionError:
        print("Não foi possível se conectar a API.")
        return None
    except requests.exceptions.HTTPError:
        print("Erro HTTP ao acessar a API.")
        return None
    except requests.exceptions.JSONDecodeError:
        print("A resposta da API não está em formato JSON válido.")
        return None
    except requests.exceptions.RequestException:
        print("Erro ao acessar a API.")
        return None


def ler_int(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor > 0:
                return valor
            else:
                print("O valor deve ser maior do que 0.")
        except ValueError:
            print("Por favor, digite um número inteiro válido, tente novamente")


def ler_moedas(moedas_disponiveis):
    if not moedas_disponiveis:
        return None
    moeda_destino = []
    while True:
        moeda_base =  input('Informe a moeda base: ').upper().strip()
        if moeda_base not in moedas_disponiveis:
            print("Moeda base inválida, tente novamente.")
            continue
        while True:
            moeda_dest = input("Informe a moeda destino [0 para sair]: ").upper().strip()
            if moeda_dest == '0' and len(moeda_destino) > 0 :
                print("Saindo...")
                return moeda_base, moeda_destino
            elif moeda_dest == '0' and len(moeda_destino) == 0:
                print("Moeda destino vazia, operação cancelada.")
                return None
            elif moeda_dest in moedas_disponiveis and moeda_base != moeda_dest and moeda_dest not in moeda_destino:
                moeda_destino.append(moeda_dest)
            else:
                print("Moeda destino inválida, tente novamente.")


