"""
Manipulação de texto, ou string
"""
frase = 'Curso em Video Python'

#  Fatiamento
print(frase[9])
print(frase[9:14])

#  Análise
print(len(frase))  # tamanho da string  
print(frase.count('o'))  # quantas vezes aparece determinado valor
print(frase.find('deo'))  # em que posição começa determinado valor
print('Curso' in frase)

#  Transformação
print(frase.replace('Python', 'Android'))  # troca um valor pelo outro
print(frase.upper())  # tudo em MAUÍSCULO
print(frase.lower())  # tudo em minúsculo
print(frase.capitalize())  # apenas a primeira letra em maiúscula
print(frase.title())  # primeira letra de cada palavra em maiúscula
frase2 = '   Aprenda Python   '
print(frase2)
print(frase2.strip())  # remove os espaços inúteis(preserva os espaços entre as palavras)
print(frase2.rstrip())  # remove os espaços inúteis da direita
print(frase2.lstrip())  # remove os espaços inúteis da esquerda

#  Divisão 
print(frase.split())  # gera uma lista, com todas as palavras da string separadas

#  Junção
print('-'.join(frase))  # junta toda a string, usando como separador o informado entre "('-')"

#  Texto longo

print("""Esperançosamente, as instruções de instalação acima funcionaram para você. Caso contrário, 
leia alguns métodos de instalação alternativos e detalhes extras abaixo.
As rodas estão disponíveis para arquiteturas x86 e x64 no Linux e Windows e para x64 no Mac. 
Se o pip não encontrar uma roda para sua plataforma, ele tentará compilar o pygame a partir do código-fonte 
(veja abaixo).
pygame requer um pip "mais novo". Se o pygame começar a compilar a partir da fonte e falhar, primeiro tente 
atualizar o pip .""")

