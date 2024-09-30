#Calculadora feita para seleção como voluntário de pesquisa
#Versão do python: 3
#Meu nome: Jean Carlo Nascimento Araújo

class OpcaoInvalida(Exception): #Exceção para quando usuário digitar uma opção inválida
    def __init__(self,mensagem):
        print("Não entendi qual a opção")
        print(mensagem)
    

numero1 = 0.0 #primeiro número da operação
numero2 = 0.0 #segundo número da operação
option = "null" #opções do usuário
flag = False #flag pra indicar se há resultado armazenado ou não
resultado = 0.0 #variável para armazenar resultados

def soma(x, y): #função para soma de duas variáveis
    return x + y
def sub(x, y): #função para subtração de duas variáveis
    return x - y
def mult(x, y): #função para multiplicação de duas variáveis
    return x * y
def div(x, y): #função para divisão de duas variáveis
    return x / y
    
while(True): #Laço principal
    while(True): # Laço de leitura dos valores 
        try:
            if(flag==False): #Quando não há nenhum resultado armazenado
                numero1 = float(input("Digite o primeiro número: "))
            else: #Quando há um resultado armazenado
                numero1 = resultado
            numero2 = float(input("Digite o segundo número: "))
            break
        except ValueError: #se usuário digitar um valor que não seja numérico há o tratamento da exceção
            print("você digitou um valor invalido :(")
    while(True): #Laço de leitura da operação
        try: #Tenta ler a opção de operação, se não reconhecer, lança uma exceção
            option = str(input("Qual operação deseja realizar?"))
            match option:
                case "+":
                    resultado = soma(numero1,numero2)
                    break
                case "-":
                    resultado = sub(numero1,numero2)
                    break
                case "*":
                    resultado = mult(numero1,numero2)
                    break
                case "/":
                    resultado = div(numero1,numero2)
                    break
                case _:
                    raise OpcaoInvalida("Use: \n + \n - \n * \n /")
        except OpcaoInvalida:
            continue

    print("O resultado de " + str(numero1) +" " + option +  " " + str(numero2) + " é igual a " + str(resultado))
    flag = True #Indica que existe um resultado armazenado
    while(True): #Laço de leitura da opção pós operação
        try:
            option = str(input("Deseja continuar? "))
            if(option.lower() == "sim"): # Vai continuar operando com os valores lidos
                break
            if(option.lower() == "não"): 
                option = str(input("Deseja reiniciar? "))
                if(option.lower == "sim"): #vai mudar flag para receber os dois números
                    flag = False
                    break
                if(option.lower() == "não"): #quer sair do programa
                    break 
                else: #digitou algo que não foi sim ou não
                    raise OpcaoInvalida("Use sim ou não")
            else: #digitou algo que não foi sim ou não
                raise OpcaoInvalida("Use sim ou não ")
        except OpcaoInvalida:
            continue
    if(option.lower() == "não"): 
        break #encerra o loop principal
