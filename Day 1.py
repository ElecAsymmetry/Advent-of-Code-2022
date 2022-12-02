#This is probably extremely inefficient but I made it in 10 minutes so what can you expect.


with open("D:/Visual Studio Code/Advent of Code/Day 1/Day 1.txt") as inputs:
    #Get all numbers into a list
    amounts = [line for line in inputs]


stripped_list = []

for amount in amounts:
    #Remove all new lines
    stripped_list.append(amount.replace("\n",''))

current_sum = 0
final_list = []

for number in stripped_list:
    #Creates a sum of numbers, then appends them and resets the sum when the number is equal to ''
    if number == '':
        final_list.append(current_sum)
        current_sum = 0

    elif number != '':
        number = int(number)
        current_sum += number

#Finally Sort the List so that largest is at the end
sorted_list = sorted(final_list)

print(f"Part 1: {sorted_list[-1]}")

print(f"Part 2: {sum([sorted_list[-1],sorted_list[-2], sorted_list[-3]])}" )
