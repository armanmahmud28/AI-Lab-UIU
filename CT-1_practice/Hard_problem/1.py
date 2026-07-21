#Binary Search (Without Built-in Functions)     

numbers = list(map(int, input("Enter sorted numbers: ").split()))

target = int(input("Enter target: "))

left = 0
right = len(numbers) - 1

found = False

while left <= right:

    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Found at index", mid)
        found = True
        break

    elif numbers[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

if not found:
    print("Element not found")  