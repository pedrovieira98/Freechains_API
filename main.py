import os

chave = str(input("Digite uma senha: "))
senha = "freechains keys pubpvt '" + chave + "'"
senha_pub = os.system("freechains keys shared '" + chave + "'")
resultado = os.popen(senha).read().split()
print(senha_pub)
print(resultado[0])

print("--------------------------------- Regras ----------------------------------")
print("Se você é Pioneiro pode fazer tudo no Canal assim como membro Moderador.\nSe for usuário Ativo e Regular pode dar like e dislike. \nO Troll não pode fazer nada no Canal.\n-------------------------------------------------------------------------- \n")

def options():
    
    print("1 - Criar Canal")
    print("2 - Entrar em Canal")
    print("3 - Postar no Canal")
    print("4 - Dar like")
    print("5 - Dar dislike")
    print("6 - Ver Nível")
    print("7 - Sair")

menu_option = 0

#Variável para definir se está ou não em um canal
in_channel = False

while (menu_option != '7'):
    
    options()
    menu_option = str(input("Digite a opção desejada: "))

    if (menu_option == '1'):
        print(" --- Criação de Canal --- ")
        canal_nome = str(input("Qual o nome do canal a ser criado? "))
        senha_entrar = resultado[0]
        criar = os.system("freechains chains join '#" + canal_nome + "'senha_entrar'")
        in_channel = True

    elif (menu_option == '2'):
        print(" --- Entrar em Canal --- ")
        canal_nome = str(input("Qual o nome do canal que deseja entrar? "))
        senha_entrar = str(input("Qual a chave pública do canal? "))
        entrar = os.system("freechains chains join '#" + canal_nome + "''" + senha_entrar + '"')
        in_channel = True

    elif (menu_option == '3'):
        if (in_channel == True):
            print(" --- Postar no Canal --- ")
            mensagem = str(input("Qual a mensagem que deseja postar? "))
            post = os.system("freechains chain '#" + canal_nome + "' post inline" + mensagem)
        else:
            print("Você deve criar ou entrar em um canal antes")
            print("Retornando ao Menu\n")

    elif (menu_option == '4'):
        if (in_channel == True and rep >= 20):
            senha_priv = resultado[1]
            rep = os.system("freechains chain reps '#" + canal_nome + "'""' + resultado[0]'")
            if (rep >= 10):
                hash_msg = str(input("Qual o hash da mensagem que deseja dar like? "))
                like = os.system("freechains chain '#" + canal_nome + "' like'" + hash_msg + "' --sign='senha_priv'")
            else:
                print ("Você não pode dar like")

        else:
            print("Você deve criar ou entrar em um canal antes")
            print("Retornando ao Menu\n")

    elif (menu_option == '5'):
        if (in_channel == True and rep >= 20):
            senha_priv = resultado[1]
            rep = os.system("freechains chain reps '#" + canal_nome + "'""' + resultado[0]'")
            if (rep >= 10):
                hash_msg = str(input("Qual o hash da mensagem que deseja dar dislike? "))
                like = os.system("freechains chain '#" + canal_nome + "' dislike'" + hash_msg + "' --sign='senha_priv'")
            else:
                print ("Você não pode dar dislike")

        else:
            print("Você deve criar ou entrar em um canal antes")
            print("Retornando ao Menu\n")

    elif (menu_option == '6'):
        
        if (in_channel == True):
            print(" --- Ver Nível --- ")
            canal_nome = str(input("Qual o nome do canal? "))
            rep = os.system("freechains chain reps '#" + canal_nome + "'""' + resultado[0]'")
            print(rep)

            if (rep <= '0'):
                print("Você é um troll")
        
            elif (rep >= '0' and rep <= '10'):
                print("Você é um membro Regular")
        
            elif (rep >= '10' and rep <= '20'):
                print("Você é um membro Ativo")

            elif (rep >= '20'):
                print("Você é um membro Moderador")
        
            elif (senha_entrar == resultado[0]):
                print("Você é o Pioneiro")
        else:
            print("Você deve criar ou entrar em um canal antes")
            print("Retornando ao Menu\n")       
        
        ## A ser implementado
    #elif (menu_option == '8'):
        #if (in_channel == True):
            #print ("--- Ver Consensus ---")
            #con = os.system("freechains chain '#" + canal_nome + "' consensus")
            #view = str(input("Deseja ver o payload de alguma mensagem? (Digite s ou n) "))

            #if (view == 's'):
                #hash_msg = str(input("Qual o hash da mensagem que deseja ver? "))
                #payload = os.system("freechains chain '#" + canal_nome + "' get payload '" + hash_msg + "' file 'tmp/x.pay'")

            #else:
                #print("Retronando ao menu")


    elif (menu_option == '7'):
        print("Saindo")
    
    else:
        print("Opção não existente")
