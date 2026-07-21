# Program to print all prime numbers in a given range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime Numbers:")

for num in range(start, end + 1):

    if num < 2:
        continue

    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)
