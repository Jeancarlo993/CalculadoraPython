# Explicando a calculadora  
## Variáveis:  
   * duas variáveis pra armazenar os operandos,
   * uma variável para armazenar opções do usuário, inclusive as operações,
   * uma variável de controle,
   * uma variável para armazenar o resultado das operações.
## Funções/Procedimentos  
Criei funções/procedimentos para cada operação. Elas recebem dois valores e armazenam o resultado da operação na variável de resultado.
## Tratamento de Exceções    
Fiz o tratamento de dois tipos de exceção. 
  * ValueError -> quando o usuário digita um valor não número em dos operandos
  * OpcaoInvalida -> exceção criada para quando o usuário digitar um opção que não seja compreendida pelo programa. Neste caso, o método construtor escreve a mensagem informando que não entendeu a opção, enquanto sempre que a exceção é lançada, envia-se uma mensagem informando quais as opções seriam válidas.
## O funcionamento  
Um laço principal mantém o programa em funcionamento até que o usuário não deseje mais executar nenhum tipo de operação. Nas leituras dos números e das opções, temos também laços para garantir que elas sejam feitas corretamente até o fim. O programa encerra quando ao final o usuário não deseja nem continuar (ou seja, usar o último resultado como primeiro operando) e nem reiniciar a calculadora (obter novamente os dois operandos). 
