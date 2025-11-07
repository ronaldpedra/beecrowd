"""
beecrowd | 2754
Saída 8
Por Roberto A. Costa Jr, UNIFEI BR Brazil

Timelimit: 1
O seu professor de programação gostaria que você fizesse um programa com 
as seguintes características:

Crie duas variáveis reais de dupla precisão;
Atribua a primeira o valor 234.345 e a segunda o valor 45.698;
Imprima as duas variáveis com seis casas decimais;
Imprima as duas variáveis sem nenhuma casa decimal;
Imprima as duas variáveis com uma casa decimal;
Imprima as duas variáveis com duas casas decimais;
Imprima as duas variáveis com três casas decimais;
Imprima as duas variáveis com notação cientifica com 'e';
Imprima as duas variáveis com notação cientifica com 'E';
Imprima as duas variáveis com a representação mais curta, com 'e' ou 'E' 
ou sem;
Imprima as duas variáveis com a representação mais curta, com 'e' ou 'E' 
ou sem;
Para imprimir, separe os valores com um espaço em branco, um traço (-) e 
um espaço em branco.

Entrada
Não há.

Saída
O resultado de seu programa deve ser escrito conforme o exemplo da saída.

Exemplo de Entrada	Exemplo de Saída
234.345000 - 45.698000
234 - 46
234.3 - 45.7
234.34 - 45.70
234.345 - 45.698
2.343450e+02 - 4.569800e+01
2.343450E+02 - 4.569800E+01
234.345 - 45.698
234.345 - 45.698
"""
A = 234.345
B = 45.698

print(f'{A:.6f} - {B:.6f}')
print(f'{A:.0f} - {B:.0f}')
print(f'{A:.1f} - {B:.1f}')
print(f'{A:.2f} - {B:.2f}')
print(f'{A:.3f} - {B:.3f}')
print(f'{A:.6e} - {B:.6e}')
print(f'{A:.6E} - {B:.6E}')
print(f'{A:.3f} - {B:.3f}')
print(f'{A:.3f} - {B:.3f}')
