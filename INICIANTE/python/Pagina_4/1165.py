# uai
n = int(input())

if int(n/10) % 2 == 0:
    print('par')
else:
    caso = str(n)
    soma = 0
    for i in range(len(caso)):
        soma += int(caso[i])
    print(soma)


