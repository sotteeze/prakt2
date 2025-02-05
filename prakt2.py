number = int(input("Введіть число: "))
prime_factors = []
divisor = 2
while number > 1:
    if number % divisor == 0:
        prime_factors.append(divisor)
        number = number // divisor
    else:
        divisor += 1

print("Прості множники:", " -> ".join(map(str, prime_factors)))