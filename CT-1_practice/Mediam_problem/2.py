#Find the Second Largest Element

numbers = [20,40,10,50,70,60]

largest = max(numbers)
numbers.remove(largest)

print(max(numbers))

'''''
#without built-in functions

numbers = list(map(int, input("Enter numbers: ").split()))

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest =", second)

'''''

