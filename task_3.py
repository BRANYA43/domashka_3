list_ten = list(range(10, 51, 10))
some_list = []

for i in range(len(list_ten)):
    print(i)
    some_list.append(list_ten[len(list_ten) - i - 1])

print(some_list)
