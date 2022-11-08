import random
size = int(input('size -> '))
begin = int(input('begin -> '))
end= int(input('end -> '))

my_list = list()
for i in range(size):
    my_list.append(random.randint(begin, end))

for i in range(0, len(my_list)):
    print(f'{my_list[i]}[{i}]', end=' ')
print()

res_list_even = list()
res_list_odd = list()
res_list_neg = list()
res_list_pos = list()

for item in my_list:
    if item % 2 == 0:
        res_list_even.append(item)
for item in my_list:
    if item % 2 != 0:
        res_list_odd.append(item)
for item in my_list:
    if item < 0:
        res_list_neg.append(item)
for item in my_list:
    if item > 0:
        res_list_pos.append(item)

print(f'List even {res_list_even}:')
print(f'List odd {res_list_odd}:')
print(f'List negative {res_list_neg}:')
print(f'List positive {res_list_pos}:')