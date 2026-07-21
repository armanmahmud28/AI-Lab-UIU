numbers = [2,5,7,10,12,15]

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)
