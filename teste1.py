num = float(input('\nDigite um numero: '))
seq2 = 1
seq1 = 0
aux = 0
vetor =[seq1, seq2]

while seq2<num:
    aux= seq1+seq2
    seq1 = seq2
    seq2 = aux
    vetor.append(seq2)
    

if num in vetor:
    print('\nO numero faz parte da seqência')
else:
    print('\nO numero não faz parte da sequência')