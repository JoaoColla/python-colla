#funções
def pizza_salg ():
   print ("1 - Calabresa")
   print ("2 - Frango com catupiry")
   print ("3 - Quatro queijos")


def pizza_doce ():
   print ("1 - Sensação")
   print ("2 - Prestigio")
   print ("3 - Brigadeiro")


def bebida ():
   print ("1 - Coca")
   print ("2 - Guarana")
   print ("3 - Cini")


def menu_1():
   print(name + ", estas são as opções do nosso cardapio:")
   print("1 - Pizzas Salgadas")
   print("2 - Pizzas Doces")
   print("3 - Bebidas")



#saudação
print ("Olá, qual é o seu nome? ")
name = input("Você: ")
print()
print ("Seja bem-vindo a pizzaria Coca Colla, " + name)
print()



#cardapio
menu_1()
print()


#pedido
opc = int (input("Digite o numero do que deseja: \nVocê:"))


if opc == 1:
   pizza_salg()

   decisão = int (input("Digite o numero do que deseja: \nVocê:"))



elif opc == 2:
   pizza_doce()


elif opc == 3:
   bebida()


else:
   print("Nenhuma opção encontrada, tente novamente.")
   print()
   menu_1()





