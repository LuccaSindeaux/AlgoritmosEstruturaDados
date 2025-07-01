# 1) Construa a classe Torre e a classe Apartamento. A classe Torre deve possuir os atributos id, nome e endereço. A classe Apartamento deve conter os atributos, id, número do apartamento, número da vaga de garagem e torre.

# 2) Este condomínio, não possui vagas de garagem para todos os apartamentos. Isso faz com que exista uma fila de espera por vagas. Implemente uma fila de espera que contenha os métodos para adicionar apartamentos na fila, retirar apartamentos informando o número da vaga que este apartamento receberá e um método para imprimir a fila de espera.

# 3) Construa um menu de opções ao usuário, com as funcionalidades do algoritmo. 

from Torre import Torre
from Apartamento import Apartamento
from FilaApartamento import FilaApartamento


def main():
    FilaApto = FilaApartamento()

    while True:
        print("\n=============== MENU ===============")
        print("1. Adicionar Apartamento à fila.")
        print("2. Remover apartamento da fila.")
        print("3. mostrar apartamentos na fila.")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = int(input("Número do apartamento: "))
            torre = input("Nome da Torre: ")
            vaga = int(input("Vaga esperada: "))
            FilaApto.AddAptoFila(numero, torre, vaga)
        
        elif opcao == "2":
            FilaApto.removerApto()
        
        elif opcao == "3":
            FilaApto.imprimir()

        elif opcao == "4":
            break

        else: 
            print("Opção inválida.")

        

if __name__ == "__main__":
    main()