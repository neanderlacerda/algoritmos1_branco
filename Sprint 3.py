import sqlite3
i=""
somaNotas=0
somavalor = 0
conexao = sqlite3.connect("escola.sqlite")
cursor = conexao.cursor()
# banco(Avaliação)
cursor.execute('''
			create table if not exists Avaliacao (
                                CodAvaliacao integer PRIMARY KEY AUTOINCREMENT,
				disciplina text,
				descricao text,
				valor int,
				dataA text
				)''')
# banco(Avalição X Alunos)
cursor.execute('''
			create table if not exists AVAlunos (
				CodAvaliacao integer,
				CodAluno integer,
				nomeAluno text,
				notaAV float,
				situacao text,
				notaFinal float
				)''')
# banco(Turma)
cursor.execute('''
			create table if not exists Turma (
                                CodTurma integer PRIMARY KEY AUTOINCREMENT,
				nome text,
				professor text,
				alunosXturma text
				)''')
# banco(Professores)
cursor.execute('''
			create table if not exists Professores (
			CodProfessor integer PRIMARY KEY AUTOINCREMENT,
				login text,
				senha text,
				nome text,
				email text
				)''')
# banco(Alunos)
cursor.execute('''
			create table if not exists Alunos (
                                CodAluno integer PRIMARY KEY AUTOINCREMENT,
                                login text,
                                senha text,
                                nome text,
                                sobrenome text,
                                email text,
                                datanasc text
                                )''')
# banco(Turma com Alunos)
cursor.execute('''
			create table if not exists TurmaXAluno (
				CodTurma integer,
				CodAluno integer
				)''')
# INICIO =================================================================
print("Este é o programa do grupo Branco!")
while True:
    print("_"*50)
    print("Seja Bem-vindo!")
    print("\nVocê deseja fazer login no perfil:\n")
    print("1) Aluno")
    print("2) Professor")
    print("3) Administrador")
    print("4) Sair")
    perfil = str(input("\nDigite o número do perfil escolhido: "))
# Aluno -------------------------------------------------------------------
    if(perfil == '1'):
        print("_"*50)
        print("\nPerfil do Aluno\n")
        logAluno = str(input("Informe seu login: "))
        senAluno = str(input("Informe sua senha: "))
        if(cursor.execute('''SELECT * FROM Alunos WHERE login=?''',(logAluno,))):
            rs = cursor.fetchall()
            for i in rs:
                codAluno = i[0]
                if(i[2]==senAluno):
                    while True:
                        print("\nMENU DE OPÇÕES:\n")
                        print("1) Ver boletim")
                        print("2) Fazer logoff")
                        opcao = str(input("Digite o número da opção que deseja: "))
                        if(opcao == '1'):
                            print("_"*50)
                            print("\nVer boletim\n")
                            cursor.execute('''SELECT * FROM AVAlunos WHERE CodAluno=?''',(codAluno,))
                            rs = cursor.fetchall()
                            print("\nCod Avaliação\tAluno\tNota\tSituação\n")
                            if rs:
                                for i in rs:
                                    print("%s\t\t%s\t%.2f\t%s"%(i[0],i[2],i[3],i[4]))
                        if(opcao == '2'):
                            resposta = str(input("Tem certeza que deseja fazer logoff?""\n""Sim -> s""\n""Não -> n""\n"))
                            if(resposta == "s"):
                                break
# Professor ---------------------------------------------------------------
    if(perfil == '2'):
        print("_"*50)
        print("\nPerfil do Professor\n")
        logProfessor = str(input("Informe seu login: "))
        senProfessor = str(input("Informe sua senha: "))
        if(cursor.execute('''SELECT * FROM Professores WHERE login=?''',(logProfessor,))):
            rs = cursor.fetchall()
            for i in rs:
                if(i[2]==senProfessor):
                    while True:
                        print("\nMENU DE OPÇÕES:\n")
                        print("1) Cadastrar avaliação")
                        print("2) Lançar notas")
                        print("3) Ver boletins de alunos")
                        print("4) Exportar Boletim")
                        print("5) Fazer logoff")
                        opcao = str(input("Digite o número da opção que deseja: "))
            #             1) CADASTRAR AVALIAÇÃO __________________________________
                        if(opcao == '1'):
                            print("_"*50)
                            print("\nCadastrar avaliações\n")
                            disciplina = str(input("Informe a disciplina: "))
                            descricao = str(input("Descrição: "))
                            valor = int(input("Informe o valor: "))
                            dataA = str(input("Informe a data da avaliação: "))
                            cursor.execute(''' INSERT INTO Avaliacao (disciplina,descricao,valor,dataA) VALUES (?,?,?,?) ''',(disciplina,descricao,valor,dataA))
                            conexao.commit()
                            print("_"*50)
                            print("Avaliação cadastrada com sucesso!")
             #            2) LANÇAR NOTAS__________________________________________
                        if(opcao == '2'):
                            print("_"*50)
                            print("\nLançar notas\n")
                            cursor.execute(''' SELECT * FROM Avaliacao ''')
                            rs = cursor.fetchall()
                            if rs:
                                print("\nCod\tAvaliação\n")
                                for i in rs:
                                    print("%s\t%s" % (i[0],i[1]))
                            else:
                                print("Não existem Avaliações")
                            cursor.execute(''' SELECT * FROM Alunos ''')
                            rs = cursor.fetchall()
                            if rs:
                                print("\nCod\tAluno\n")
                                for i in rs:
                                    print("%s\t%s" % (i[0],i[3]))
                            else:
                                print("Não existem alunos")
                            CodAvaliacao = int(input("Informe o código da avaliação: "))
                            CodAluno = int(input("Informe o código do aluno: "))
                            notaAV = float(input("Informe a nota do aluno:"))
                            cursor.execute('''SELECT * FROM Alunos WHERE CodAluno = ?''',(CodAluno,))
                            rs = cursor.fetchall()
                            if rs:
                                for i in rs:
                                    nomeAluno = i[3]
                            
                            somaNotas = notaAV+somaNotas
                            cursor.execute('''SELECT * FROM Avaliacao WHERE CodAvaliacao=?''',(CodAvaliacao,))
                            rs = cursor.fetchall()
                            if rs:
                                for i in rs:
                                    somavalor = i[3]+somavalor
                            media = (somavalor*60)/100
                            media40 = (somavalor*40)/100
                            if (somaNotas>=media):
                                situacao = "Aprovado"
                            if(somaNotas<media40):
                                situacao ="Reprovado"
                            if(somaNotas>=media40)and(somaNotas<media):
                                situacao ="Exame Final"
                            cursor.execute(''' INSERT INTO AVAlunos (CodAvaliacao, CodAluno,notaAV,nomeAluno,situacao) VALUES (?,?,?,?,?) ''',(CodAvaliacao,CodAluno,notaAV,nomeAluno,situacao))
                            conexao.commit()
                                
                            print("_"*50)
                            print("A nota foi lançada")

            #             3) VER BOLETINS DE ALUNOS___________________________________
                        if(opcao == '3'):
                            print("_"*50)
                            print("\nVer boletins de alunos\n")
                            cursor.execute('''SELECT * FROM AVAlunos ''')
                            rs = cursor.fetchall()
                            print("\nCod Avaliação\tAluno\tNota\tSituação\n")
                            if rs:
                                for i in rs:
                                    print("%s\t\t%s\t%.2f\t%s"%(i[0],i[2],i[3],i[4]))
            #             4) Exportar_____________________________________________________  
                        if(opcao=='4'):
                            arquivo=open("Boletim.txt","w")
                            cursor.execute('''SELECT * FROM AVAlunos''')
                            rs=cursor.fetchall()
                            if rs:
                                arquivo.write("\nCod Avaliação\tAluno\tNota\tSituação\n")
                                for i in rs:
                                    arquivo.write("%s\t\t%s\t%.2f\t%s\n"%(i[0],i[2],i[3],i[4]))
                            else:
                                print("Não existem notas para exportar")
                            arquivo.close()
                            print("_"*50)
                            print("Boletim exportado com sucesso")
                        #5) Sair_____________________________________________________________
                        if(opcao == '5'):
                            resposta = str(input("Tem certeza que deseja fazer logoff""\n""Sim -> s""\n""Não -> n""\n"))
                            if(resposta == "s"):
                                break
                else:
                    print("_"*50)
                    print("Login inválido")
# Administrador -----------------------------------------------------------
    if(perfil == '3'):
        user  = str(input("Digite seu nome de usuário: "))
        senha = str(input("Digite a senha de administrador: "))
        if(senha == "administrador"):
            print("_"*50)
            print("\nBem-vindo %s!\nPerfil Administrador\n" %user)
            while True:
                print("_"*50)
                print("MENU DE OPÇÕES:\n")
                print("1) Cadastrar professor")
                print("2) Cadastrar aluno")
                print("3) Cadastrar turma")
                print("4) Vincular aluno em turma")
                print("5) Visualizar avaliação")
                print("6) Visualizar boletim")
                print("7) Visualizar alunos")
                print("8) Visualizar turma")
                print("9) Fazer logoff")
                opcao = str(input("Digite o número da opção que deseja: "))
                #- 1) Cadastrar professor__________________________________
                if(opcao == '1'):
                    print("_"*50)
                    print("CADASTRO DE PROFESSORES ")
                    login = str(input("Digite o login do professor: "))
                    senha = str(input("Digite o senha do professor: "))
                    nome = str(input("Digite o nome do professor: "))
                    email = str(input("Digite o email do professor: "))
                    cursor.execute(''' INSERT INTO Professores (login,senha,nome,email) VALUES (?,?,?,?) ''',(login,senha,nome,email))
                    conexao.commit()
                    print("Professor %s adicionado com sucesso!" % nome)
                #- 2) Cadastrar aluno______________________________________
                if(opcao=='2'):
                    print("_"*50)
                    print("CADASTRO DE ALUNOS ")
                    login = str(input("Digite o login do aluno: "))
                    senha = str(input("Digite o senha do aluno: "))
                    nome = str(input("Digite o nome do aluno: "))
                    sobrenome = str(input("Digite o sobrenome: "))
                    datanasc = str(input("Digite a data de nascimento: "))
                    email = str(input("Digite o email do aluno: "))
                    dia = datanasc[0:2]
                    mes = datanasc[2:4]
                    ano = datanasc[4:]
                    datanasc= dia+"/"+mes+"/"+ano
                    cursor.execute(''' INSERT INTO Alunos (login,senha,nome,sobrenome,email,datanasc) VALUES (?,?,?,?,?,?) ''',(login,senha,nome,sobrenome,email,datanasc))
                    conexao.commit()
                    print("_"*50)
                    print("Aluno %s adicionado com sucesso!" % nome)
                #- 3) Cadastrar Turma_______________________________________
                if(opcao == '3'):
                    print("_"*50)
                    print("CADASTRO DE TURMAS ")
                    nome = str(input("Digite o nome da turma: "))
                    professor = str(input("Digite o nome do professor: "))
                    cursor.execute(''' INSERT INTO Turma (nome,professor) VALUES (?,?) ''',(nome,professor))
                    conexao.commit()
                    print("_"*50)
                    print("Turma:%s Cadastrada com sucesso!" %nome)
                #- 4) Vincular aluno em turma_______________________________
                if(opcao=='4'):
                    print("_"*50)
                    print("\nVincular aluno em turma\n")
                    cursor.execute(''' SELECT * FROM Turma ''')
                    rs = cursor.fetchall()
                    if rs:
                        print("\nCod\tTurma\n")
                        for i in rs:
                            print("%s\t%s" % (i[0],i[1]))
                    else:
                        print("Não existem turmas")
                    cursor.execute(''' SELECT * FROM Alunos ''')
                    rs = cursor.fetchall()
                    if rs:
                        print("\nCod\tAluno\n")
                        for i in rs:
                            print("%s\t%s" % (i[0],i[1]))
                    else:
                        print("Não existem alunos")
                    CodTurma = int(input("\nInforme o código da turma: "))
                    CodAluno = int(input("Informe o código do aluno: "))
                    cursor.execute(''' INSERT INTO TurmaXAluno (CodTurma, CodAluno) VALUES (?,?) ''',(CodTurma,CodAluno))
                    conexao.commit()
                if(opcao=='5'):
                    print("_"*50)
                    print("\nVisualizar avaliação\n")
                    cursor.execute(''' SELECT * FROM Avaliacao ''')
                    rs = cursor.fetchall()
                    if rs:
                        print("\nCod\tAvaliação\n")
                        for i in rs:
                            print("%s\t%s" % (i[0],i[1]))
                    else:
                        print("Não existem Avaliações")
                
                if(opcao=='6'):
                    print("_"*50)
                    print("\nVisualizar boletim\n")
                    print("_"*50)
                    print("\nVer boletins de alunos\n")
                    cursor.execute('''SELECT * FROM AVAlunos ''')
                    rs = cursor.fetchall()
                    print("\nCod Avaliação\tAluno\tNota\tSituação\n")
                    if rs:
                        for i in rs:
                            print("%s\t\t%s\t%.2f\t%s"%(i[0],i[2],i[3],i[4]))
                    
                    
                #- 7)  Visualizar alunos______________________________________   
                if(opcao=='7'):
                    print("_"*50)
                    print("\nVisualizar alunos\n")
                    cursor.execute('''SELECT * FROM Alunos''')
                    rs = cursor.fetchall()
                    print("\nAlunos")
                    for i in rs:
                        print("\nNome\tSobrenome\n%s\t%s"%(i[3],i[4]))
                #- 8) Visualizar turma________________________________________
                if(opcao=='8'):
                    print("_"*50)
                    print("\nVisualizar turma\n")
                    cursor.execute('''SELECT * FROM Turma''')
                    rs=cursor.fetchall()
                    if rs:
                        print("\nCod\tTurma\n")
                        for i in rs:
                            print("%s\t%s" % (i[0],i[1]))
                    else:
                        print("Não existem Turmas")

                    print()
                    CodTurma = int(input("Informe o código da turma que deseja visualizar os alunos: "))
                    cursor.execute(''' SELECT CodAluno FROM TurmaXAluno WHERE CodTurma = ?''',(CodTurma, ))
                    rs = cursor.fetchall()
                    if rs:
                        print("\nCodAluno\n")
                        for i in rs:
                            cursor.execute(''' SELECT * FROM Alunos WHERE CodAluno = ?''',(i[0], ))
                            rs2 = cursor.fetchone()
                            print("%s\t%s" % (rs2[0],rs2[1]))
                    else:
                        print("Não existem alunos")
                    print()
                    input()
                #- 9) Fazer logoff_____________________________________________
                if(opcao == '9'):
                    resposta = str(input("Tem certeza que deseja fazer logoff?""\n""Sim -> s""\n""Não -> n""\n"))
                    if(resposta == "s"):
                        break  
        # 2 tab) Feedback para senha errada do adiministrador...
        else:
            print("_"*50)
            print("\nSenha incorreta\n")
# Sair -------------------------------------------------------------------------
    if(perfil=='4'):
        break
cursor.close()
conexao.close()
                    
