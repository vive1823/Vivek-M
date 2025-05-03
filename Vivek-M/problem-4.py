#4

numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
mul_count = {i: 0 for i in range(1, 10)}
for i in range(1, 10):
    for num in numbers:
        if num % i == 0:
            mul_count[i] += 1
print(mul_count)
