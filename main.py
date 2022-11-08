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




mul = 1
for i in range(0, len(my_list), 3):
    print(f'{mul} * {my_list[i]}[{i}] = ', end=' ')
    mul*= my_list[i]
    print(mul)




min_max = 1
start_index = my_list.index(min(my_list))
end_index = my_list.index(max(my_list))
if start_index > end_index:
    start_index, end_index = end_index, start_index
print(f'start index = {start_index}, end index =  {end_index}')

for i in range(start_index+1, end_index):
    print(f'{my_list[i]}', end=' ')
    min_max*= my_list[i]
   # print(f'\nMul min & max = {min_max}')



sum_list = [0]* 3

for item in my_list:
    if item < 0:
        sum_list[0] += item
    if item % 2 == 0:
        sum_list[1] += item
    if item % 2 != 0:
        sum_list[2] += item



mmm = 1
start_index = end_index = 0
for i in range(0,len(my_list)):

    if start_index >  my_list[i] > 0:
        start_index = i
    if end_index < my_list[i] < 0:
        end_index = i

sum = 0
if start_index > end_index:
    start_index, end_index = end_index, start_index
print(f'start index = {start_index}, end index = {end_index}')
for i in range(start_index+1, end_index):
    print(f'{my_list[i]}', end=' ')
    sum += my_list[i]
#print(f'\nSum = {sum}')


print(f'Sum negative: {sum_list[0]}')
print(f'Sum even: {sum_list[1]}')
print(f'Sum odd: {sum_list[2]}')
print(f'Mul even 3 index: {mul}')
print(f'Mul min & max index: {min_max}')
print(f'Sum elementes: {sum}')