# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

#menu da calculadora
menu = "Selecione o número da operação desejada:\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n"
print(menu)

#selecionar operação
op = input("\nDigite sua opção (1/2/3/4): ")

#selecionar operandos
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

#calculando
if(op == '1'):
	result = num1 + num2
	print("%d + %d = %d" %(num1,num2,result))
elif(op == '2'):
	result = num1 - num2
	print("%d - %d = %d" %(num1,num2,result))
elif(op == '3'):
	result = num1 * num2
	print("%d * %d = %d" %(num1,num2,result))
elif(op == '4'):
	result  = num1 / num2
	print("%d / %d = %d" %(num1,num2,result))
else:
	print("Operação inválida")