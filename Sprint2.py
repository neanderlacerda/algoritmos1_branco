i=0
professor=[]
professores=[]
aluno=[]
alunos=[]
turma=[]
turmas=[]
listaAlunos=[]
print("Este é o programa do grupo cinza!")
while True:
  print("_"*50)
  print("Seja Bem-vindo!")
  print("\nVocê deseja fazer login no perfil:\n")
  print("1) Aluno")
  print("2) Professor")
  print("3) Administrador")
  print("4) Sair")
  perfil = str(input("\nDigite o número do perfil escolhido: "))
#____ALUNO_______________________________________________________
  if(perfil == "1"):
    user  = str(input("Digite seu nome de usuário: "))
    senha = str(input("Digite sua senha: "))
    for i in alunos:
        if(user== i["Login"]):
            if(senha == i["Senha"]):
              print("\nBem-vindo %s!\nPerfil Aluno\n" %i["Nome"])
              print("Dados pessoais: ")
              print("Nome completo: ",i["Nome"],i["Sobrenome"])
              print("Data de nascimento: ",i["Datanasc"])
              print("Email: ",i["Email"])
              while True:
                print("MENU DE OPÇÕES:\n")
                print("1) Ver boletim")
                print("2) Fazer logoff")
                opcao = int(input("Digite o número da opção que deseja: "))
                if(opcao == 1):
                  print("(MOSTRAR BOLETIN)\n")
                if(opcao == 2):
                  resposta = str(input("Tem certeza que deseja fazer logoff?""\n""Sim -> s""\n""Não -> n""\n"))
                if(resposta == "s"):
                  break
#____PROFESSOR____________________________________________________
  if(perfil == "2"):
    user  = str(input("Digite seu nome de usuário: "))
    senha = str(input("Digite sua senha: "))
    for i in professores:
        if(user== i["Login"]):
            if(senha == i["Senha"]):
                print("\nBem-vindo %s!\nPerfil Professor\n" %i["Nome"])
                print("Dados pessoais: ")
                print("Email: ",i["Email"])
                while True:
                  print("MENU DE OPÇÕES:\n")
                  print("1) Cadastrar avaliação")
                  print("2) Lançar notas")
                  print("3) Ver boletins de alunos")
                  print("4) Fazer logoff")
                  opcao = int(input("Digite o número da opção que deseja: "))
                  if(opcao == 1):
                    print("Cadastro de avaliações\n")
                    disciplina = str(input("Informe a disciplina:"))
                    descricao = str(input("Descreva a avaliação:"))
                    valor = float(input("Informe o valor da avaliação:"))
                    dataAplicacao = str(input("Informe a data da avaliação:\n"))                                        
                  if(opcao == 2):
                    print("(MOSTRAR LANÇAMENTO DE NOTAS)\n")
                  if(opcao == 3):
                    print("(MOSTRAR LISTA DE ALUNOS)\n")
                  if(opcao == 4):
                    resposta = str(input("Tem certeza que deseja fazer logoff""\n""Sim -> s""\n""Não -> n""\n"))
                  if(resposta == "s"):
                    break
#____ADMINISTRADOR__________________________________________________
  if(perfil == "3"):
    user  = str(input("Digite seu nome de usuário: "))
    senha = str(input("Digite a senha de administrador: "))
    if(senha == "administrador"):
      print("\nBem-vindo %s!\nPerfil Administrador\n" %user)
      while True:
        print("_"*50)
        print("MENU DE OPÇÕES:\n")
        print("1) Cadastrar professor")
        print("2) Cadastrar turma")
        print("3) Cadastrar aluno")
        print("4) Visualizar avaliação")
        print("5) Visualizar boletim")
        print("6) Visualizar alunos")
        print("7) Fazer logoff")
        opcao = int(input("Digite o número da opção que deseja: "))
#_______________Cadastro de professores______________________________
        if(opcao == 1):
          print("_"*50)  
          print("CADASTRO DE PROFESSORES ")
          login = str(input("Digite o login do professor: "))
          senha = str(input("Digite o senha do professor: "))
          nome = str(input("Digite o nome do professor: "))
          email = str(input("Digite o email do professor: "))
          professor={"Nome": nome,
           "Senha": senha,
           "Email": email,
           "Login": login}
          professores.append(professor)
          print("Professor %s adicionado com sucesso!" % nome)
          print("Professores adicionados: ")
          for i in professores:
              print(i["Nome"])
#_______________Cadastro de turmas___________________________________        
        if(opcao == 2):
          print("_"*50)  
          print("CADASTRO DE TURMAS ")
          nome = str(input("Digite o nome da turma: "))
          professor = str(input("Digite o nome do professor: "))
#_          *** Feedback para erros ***
          if(len(professores)==0):
                print("Não existem professores cadastrados")
          if(len(alunos)==0):
            print("Não existem alunos cadastrados")
          for i in alunos:
            print("Alunos cadastrados no sistema: \n",i["Nome"])
          print("_"*20,"Adicionar alunos","_"*20)
          while True:
            pesquisa=input("Para sair digite (sair) \n Digite o nome do aluno: ")
            for i in alunos:
              if (pesquisa==i["Nome"]):
                listaAlunos.append(i["Nome"]+" "+i["Sobrenome"])
            if (pesquisa=="sair"):
              break
          for i in professores:
              if(professor== i["Nome"]):
                turma={"Nome":nome,
                "Professor": professor,
                "Alunos":listaAlunos}
                turmas.append(turma)
                print("Turma %s cadastrada com sucesso!"% turma)
              else:
                print("Professor não encontrado!")
                
#_______________Cadastro de alunos___________________________________          
        if(opcao == 3):          
          print("_"*50)  
          print("CADASTRO DE ALUNOS ")
          nome = str(input("Digite o nome do aluno: "))
          sobrenome = str(input("Digite o sobrenome: "))
          datanasc = str(input("Digite a data de nascimento: "))
          login = str(input("Digite o login do aluno: "))
          senha = str(input("Digite o senha do aluno: "))
          email = str(input("Digite o email do aluno: "))
          dia = datanasc[0:2]
          mes = datanasc[2:4]
          ano = datanasc[4:]
          datanasc= dia+"/"+mes+"/"+ano
          aluno={"Nome": nome,
           "Sobrenome": sobrenome,
           "Datanasc": datanasc,
           "Login": login,
           "Senha": senha,
           "Email": email}
          alunos.append(aluno)
          print("_"*50)
          print("Aluno %s adicionado com sucesso!" % nome)
#_______________Visualizar avaliações___________________________________                                   
        if(opcao == 4):
          print("(VISUALIZAR AVALIAÇÕES)\n")
#_______________Visualizar notas________________________________________                                             
        if(opcao == 5):
          print("(VISUALIZAR BOLETIM)\n")
#_______________Visualizar alunos_______________________________________                                             
        if(opcao == 6):
          print("_"*50)
          print("LISTA DE ALUNOS\n")
          for i in alunos:
            print(i["Nome"])
#_______________sair____________________________________________________                                                         
        if(opcao == 7):
          resposta = str(input("Tem certeza que deseja fazer logoff?""\n""Sim -> s""\n""Não -> n""\n"))
          if(resposta == "s"):
            break
#___SAIR________________________________________________________________                                                       
  if(perfil == "4"):
    resposta = str(input("Tem certeza que deseja sair?""\n""Sim -> s""\n""Não -> n""\n"))
    if(resposta == "s"):
      break
