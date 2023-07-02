# task 30

elem_first = int(input("Укажите значение 1-го элемента :"))
delta_elem = int(input("Укажите разность элементов :"))
count_number = int(input("Введите количество элементов :"))
res = [elem_first + (i - 1) * delta_elem for i in range(1, count_number + 1)]
print('Результат вычислений = ', *res)