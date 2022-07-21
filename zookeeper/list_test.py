# put your code here
n = 0
user_number = int(input())
numbers_list = list()

while user_number != 55:
    user_number = int(input())
    numbers_list.append(user_number)
    n += 1

print(len(numbers_list))
print(sum(numbers_list))
print(round(sum(numbers_list) / len(numbers_list)))
