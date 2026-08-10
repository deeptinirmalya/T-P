# rooms = {}
# n = int(input("Enter number of persons: "))

# z = n // 4
# if n % 4 != 0:
#     z += 1

# print("Number of rooms allocated:", z)

# for i in range(1, z + 1):
#     name = input(f"Enter name to be allocated for Room {i}: ")
#     rooms[i] = name

# print(rooms)
a = 5

price1, discount1 = 50, 4
price2, discount2 = 60, 8

output1 = a >= 5
output2 = a % 5 == 0
output3 = a % 2 != 0 and a < 10
output4 = a % 2 != 0 and -10 < a < 10

temp = a
count = 0
while temp != 0:
    temp //= 10
    count += 1

output5 = count % 2 == 0 and count < 10

of1 = price1 - (price1 * discount1 / 100)
of2 = price2 - (price2 * discount2 / 100)
is_offer1_cheaper = of1 < of2

print(output1)
print(output2)
print(output3)
print(output4)
print(output5)
print(is_offer1_cheaper)


