# 5. você deve solicitar o nome e o salario, armazenar em um arquivo no formato de DIC, apicar 6% de desconto se o salario for maior que R$1.500,00 e mostrar o DIC na tela ao final de tudo.

while True:
    print('''ESCOLHA UMA OPÇÃO:
    [ 1 ] - CADASTRAR
    [ 0 ] - SAIR
    ''')
    opcao = int(input('Qual a opção desejada? '))
    
    if opcao == 1:
        nome = str(input('Digite um nome: '))
        salario = float(input('Digite um salario: '))
        
        with open('nome_salario.txt', 'a', encoding = 'utf8') as meu_arquivo:
            meu_arquivo.write(nome+':'+str(salario)+'\n')

    elif opcao == 0:
        break
    else:
        print('Opção invalida! ')