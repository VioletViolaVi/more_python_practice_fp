# list comprehension: make me a list for me to look at
# - shorter way to write stuff

# empty_list = []

# for num in range(20):
#     empty_list.append(num ** 2)

empty_list = [num ** 2 for num in range(20)]
empty_list = [num * 2 for num in "abc"]
empty_list = [num + "at" for num in "abc"]
empty_list = [num for num in range(10) if num < 3]

print(empty_list)
 