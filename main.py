#--Task 1--
def find_pythagorean_triples(n):
    triples = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c_squared = a**2 + b**2
            c = int(c_squared ** 0.5)
            if c <= n and c_squared == c**2:
                triples.append((a, b, c))
    return triples

n = int(input("Enter a number n: "))
print(find_pythagorean_triples(n))
#--Task 2--
def pascals_triangle(n):
    triangle = []
    for row in range(n):
        current_row = [1]
        if triangle:
            last_row = triangle[-1]
            current_row.extend([last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)])
            current_row.append(1)
        triangle.append(current_row)
    return triangle

n = int(input("Enter the number of rows: "))
for row in pascals_triangle(n):
    print(row)
#--Task 3--
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            sieve[num*num : limit+1 : num] = [False]*len(sieve[num*num : limit+1 : num])
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

print(sieve_of_eratosthenes(1000))
#--Task 4--
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

number = int(input("Enter a number n: "))
print(prime_factors(number))
#--Task 5--
def is_palindrome(x):
    return str(x) == str(x)[::-1]

palindromes = []
for i in range(1, 101):
    if is_palindrome(i) and is_palindrome(i**2):
        palindromes.append(i)

print(palindromes)
#--Task 6--
def number_to_words(n):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 0:
        return "zero"
    if n < 10:
        return units[n]
    if 10 <= n < 20:
        return teens[n - 10]
    if 20 <= n < 100:
        return tens[n // 10] + (" " + units[n % 10] if n % 10 != 0 else "")
    if 100 <= n < 1000:
        return units[n // 100] + " hundred" + (" " + number_to_words(n % 100) if n % 100 != 0 else "")


number = int(input("Enter a number less than 1000: "))
print(number_to_words(number))
#--Task 7--
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_twin_primes(n):
    primes = [num for num in range(n, 2*n + 1) if is_prime(num)]
    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i+1] - primes[i] == 2:
            twin_primes.append((primes[i], primes[i+1]))
    return twin_primes

n = int(input("Enter a number n: "))
print(find_twin_primes(n))
#--Task 8--
def wrap_text(text, width):
    lines = text.split('\n')
    wrapped_text = []
    for line in lines:
        while len(line) > width:
            space_index = line.rfind(' ', 0, width)
            if space_index == -1:
                space_index = width
            wrapped_text.append(line[:space_index])
            line = line[space_index:].lstrip()
        wrapped_text.append(line)
    return '\n'.join(wrapped_text)

text = input("Enter the text: ")
n = int(input("Enter the width: "))
print(wrap_text(text, n))
#--Task 10--
def find_magical_vectors(N):
    from itertools import combinations_with_replacement
    magical_vectors = []
    for comb in combinations_with_replacement(range(1, N+1), N):
        if sum(comb) == 1 or sum(comb) != 0:
            if sum(comb) == 1 and N == 1:
                magical_vectors.append(comb)
            elif sum(comb) != 0 and sum(comb) == 1:
                continue
            else:
                product = 1
                for num in comb:
                    product *= num
                if sum(comb) == product:
                    magical_vectors.append(comb)
    return magical_vectors

N = int(input("Enter the value of N: "))
print(find_magical_vectors(N))
#--Task 11--
def find_optimal_capital(cities):
    x_coords = [city[0] for city in cities]
    y_coords = [city[1] for city in cities]
    x_coords.sort()
    y_coords.sort()
    mid = len(cities) // 2
    if len(cities) % 2 == 0:
        capital_x = (x_coords[mid - 1] + x_coords[mid]) // 2
        capital_y = (y_coords[mid - 1] + y_coords[mid]) // 2
    else:
        capital_x = x_coords[mid]
        capital_y = y_coords[mid]
    return (capital_x, capital_y)

cities = []
N = int(input("Enter the number of cities: "))
for i in range(N):
    x = int(input(f"Enter x coordinate for city {i+1}: "))
    y = int(input(f"Enter y coordinate for city {i+1}: "))
    cities.append((x, y))

print("Optimal capital coordinates:", find_optimal_capital(cities))
