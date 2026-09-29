from api import converter_moeda, buscar_cotacao, converter_moedas, buscar_moedas
from validacoes import ler_int, fazer_requisicao

def main():
    moedas_disponiveis = buscar_moedas()
    if moedas_disponiveis is None:
        print("Nenhuma moeda encontrada, tente novamente mais tarde.")
        return
    while True:
        menu = ler_int("MENU DE CONVERSÕES\n1 - CONVERTER MOEDA ÚNICA\n2 - CONVERTER MOEDAS\n3 - BUSCAR COTAÇÃO\n4 - SAIR\nOPÇÃO: ")
        match menu:
            case 1:
                converter_moeda(moedas_disponiveis)
            case 2:
                converter_moedas(moedas_disponiveis)
            case 3:
                buscar_cotacao(moedas_disponiveis)
            case 4:
                print("Encerrando conversor de moedas.")
                break 
            case _:
                print("Opção inválida, tente novamente.")
                continue

if __name__ == '__main__':
    main()