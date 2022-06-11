list_of_six = list(range(100, 200, 6))
list_of_fif = []
for i in list_of_six:
    if i % 5 == 0 and i < 151:
        list_of_fif.append(i)

print(list_of_fif)