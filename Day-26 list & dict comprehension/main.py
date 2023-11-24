# numbers = [1, 5 ,7]
# new_list = [i + 1 for i in numbers]
# print(new_list)

# name = "Ranjith"
# new_list = [i for i in name]
# print(new_list)

# new_list = [i * 2 for i in range(1, 5)]
# print(new_list)

# names = ["ranjith", "ramesh", "suresh", "vishwaa", "siva"]
# new_list = [i.upper() for i in names if len(i) > 5]
# print(new_list)

########################################### DICT COMPREHENTION ############################################
import random
names = ["ranjith", "ramesh", "suresh", "vishwaa", "siva"]
marks = {i : random.randint(1, 100) for i in names }
print(marks)

marks1 = {k : v for (k,v) in marks.items() if v >= 60 }
print(marks1)