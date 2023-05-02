#1 
def countdown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list
print(countdown(10))


#2
def print_and_return(a,b):
    print(a)
    return(b)
print(print_and_return(1,2))


#3
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([1,2,3,4,5,6,7,8,9,10]))


#4
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    count = 0
    new_list =[]
    for i in range(0, len(list)):
        if list[i] > list[1]:
            count += 1
            new_list.append(list[i])
    print(count)
    return new_list
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))

#5
def length_and_value(size, value):
    new_list = []
    new_list.append(value)
    new_list = [value] * size
    return new_list
print(length_and_value(5,9))
print(length_and_value(2,6))


