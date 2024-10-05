Nome = input('Digite seu primeiro nome:')
Sobrenome = input('Digite seu segundo nome:')
print(Nome + Sobrenome)
print('Agora,vamos fazer sua média!')
primeira_nota = int(input('Digite sua primeira nota:'))
segunda_nota = int(input('Digite sua segunda nota:'))
terceira_nota = int(input('Digite sua terceira nota:'))
resultado = primeira_nota + segunda_nota + terceira_nota / 3

print(f' A soma das notas é {resultado}')
if resultado > 70:
    print('Parabéns você passou .')
if resultado < 70:
    print('Reprovado') 