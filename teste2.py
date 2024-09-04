texto = str(input('\nDigite um texto: '))

texto = texto.lower()

quantidade_a = texto.count('a')

if quantidade_a > 0:
    print(f"\nA letra 'a' aparece {quantidade_a} vez(es) na string")
else:
    print("\nA letra 'a'  não está presente na string")