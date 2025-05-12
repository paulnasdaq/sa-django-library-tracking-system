import random
rand_list = [random.randrange(1, 20, 1) for _ in range(20)]

numbers_below_10 = [item for item in rand_list if item < 10]

def number_is_less_than_ten(num):
    return num <10
numbers_below_10_with_filter = filter(number_is_less_than_ten, rand_list)

# list_comprehension_below_10 =

# list_comprehension_below_10 =