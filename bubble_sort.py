list = [4, 84, 35, 36, 76, 24, 53]

# for i in range (0, len(list)):
#     for j in range (i, len(list)):
#         if list[i] > list[j]:
#             list[i], list[j] = list[j], list[i]

# print(list)

for i in range (0, len(list)):
    for j in range (i, len(list)):
        if list[i] < list[j]:
            list[i], list[j] = list[j], list[i]

print(list)