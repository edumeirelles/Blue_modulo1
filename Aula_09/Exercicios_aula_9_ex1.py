#1.	Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada.

x = int(input('Digite um número: '))
for i in range(1,11):
    print(str(x),'x',str(i),'=',x * i)