import random

# from random import shuffle
# import random as dkf (so random become dkf)


print(random)

print(dir(random))# it show all the module available

print(random.randint(1, 10))# it will give us a number btw 1 and 10
print(random)# will print a numb btw 0 and 1

print(random.choice([1,2,3,4,5]))# will print any numb btw 1 to5



my_list = [1,2,3,4,5]
random.shuffle(my_list)
#dkf.shuffle(my_list)
print(my_list)


