from validacoes import ler_moeda, ler_valor, fazer_requisicao, ler_moedas
from utilidades import quebra_linha


def converter_moeda(moedas_disponiveis):
        moeda_base, moeda_destino = ler_moeda(moedas_disponiveis)
        resposta = consultar_api(moeda_base, moeda_destino)
        if resposta:
            valor = ler_valor(moeda_base)
            cotacao = resposta[0]['rate']
            exibir_cotacao(cotacao, moeda_base, moeda_destino)
            conversao = valor * cotacao
            print(f"Conversão: {valor:.2f} {moeda_base} = {conversao:.2f} {moeda_destino}")
            quebra_linha()


def exibir_cotacao(cotacao, moeda_base, moeda_destino):
        print(f"Cotação atual: 1 {moeda_base} = {cotacao:.2f} {moeda_destino}")


def buscar_cotacao(moedas_disponiveis):
      moeda_base, moeda_destino = ler_moeda(moedas_disponiveis)
      resposta = consultar_api(moeda_base, moeda_destino)
      if resposta:
            exibir_cotacao(resposta[0]['rate'], moeda_base, moeda_destino)

      

def consultar_api(moeda_base, moeda_destino):
    api_link =  "https://api.frankfurter.dev/v2/rates"
    if isinstance(moeda_destino, list):
        quotes_valor = ','.join(moeda_destino)
    else:
        quotes_valor = moeda_destino
    parametros = {
        "base": moeda_base,
        "quotes": quotes_valor
    }
    resposta = fazer_requisicao(api_link, parametros)
    return resposta

def converter_moedas(moedas_disponiveis):
    moedas = ler_moedas(moedas_disponiveis)
    if moedas is None:
        print("Moedas inválidas.")
        return
    moeda_base = moedas[0]
    moeda_destino = moedas[1]
    resposta = consultar_api(moeda_base, moeda_destino)
    if resposta is not None and resposta:
        valor = ler_valor(moeda_base)
        for moeda in moeda_destino:
            cotacao = None
            for item in resposta:
                if item['quote'] == moeda:
                    cotacao = item['rate']
                    break
            if cotacao is not None and cotacao > 0:
                print(f'{moeda_base} = {moeda}'.center(30))
                exibir_cotacao(cotacao, moeda_base, moeda)
                conversao = valor * cotacao
                print(f"Conversão: {valor:.2f} {moeda_base} = {conversao:.2f} {moeda}")
                quebra_linha()
            else:
                print("Cotação inválida.")
    else:
         print("Dados inválidos, tente novamente mais tarde.")



def buscar_moedas():
      api_link = "https://api.frankfurter.dev/v2/currencies"
      moedas_disponiveis = []
      moedas_geral = fazer_requisicao(api_link)
      if moedas_geral:
        for moedas in moedas_geral:
            moedas_disponiveis.append(moedas['iso_code'])
        return moedas_disponiveis
      else:
           print("Nenhuma moeda encontrada.")
