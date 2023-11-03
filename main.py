def eh_primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Testando a função para números de 1 a 100
for i in range(1, 101):
    if eh_primo(i):
        print(f'{i} é primo')
    else:
        print(f'{i} não é primo')
