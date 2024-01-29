import os

chave = str(input("Digite uma senha: "))
senha = "freechains keys pubpvt '" + chave + "'"
senha_pub = os.system("freechains keys shared '" + chave + "'")
resultado = os.popen(senha).read().split()
print(senha_pub)
print(resultado[0])

def options():
    print("1 - Criar Canal")
    print("2 - Entrar em Canal")
    print("3 - Dar like")
    print("4 - Dar dislike")
    print("5 - Ver Nível")
    print("6 - Ver Ranking")
    print("7 - Sair")

menu_option = 0

while (menu_option != '7'):
    
    options()
    menu_option = str(input("Digite a opção desejada: "))

    if (menu_option == '1'):
        print(" --- Criação de Canal --- ")
        canal_nome = str(input("Qual o nome do canal a ser criado? "))
        criar = os.system("freechains chains join '#" + canal_nome + "'""' + resultado[0]'")

    elif (menu_option == '2'):
        print(" --- Entrar em Canal --- ")
        canal_nome = str(input("Qual o nome do canal que deseja entrar? "))
        senha_entrar = str(input("Qual a chave pública do canal? "))
        entrar = os.system("freechains chains join '#" + canal_nome + "'" + senha_entrar)

    elif (menu_option == '3'):
        print(" Em desenvolvimento ")


    elif (menu_option == '4'):
        print(" Em desenvolvimento ")


    elif (menu_option == '5'):
        print(" --- Ver Hierarquia --- ")
        canal_nome = str(input("Qual o nome do canal? "))
        rep = os.system("freechains chain reps '#" + canal_nome + "'""' + resultado[0]'")
        print(rep)

    elif (menu_option == '6'):
        print(" Em desenvolvimento ")

    else:
        print("Saindo")
