import random
import my_module

# print(my_module.my_fav_num)
# randint = random.randint(1,300)
# print(randint)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# rand_num = random.randint(0,1)
# if rand_num == 0:
#   print('Heads')
# else:
#   print('Tails')

friends = ['alice', 'bob', 'charile', 'david', 'emanuel']

rand_num = random.randint(0,4)

print(friends[rand_num])
print(random.choice(friends))