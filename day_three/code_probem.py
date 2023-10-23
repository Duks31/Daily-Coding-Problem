"""
Given a list of integers return the largest product that can be made by multiplying any three integers

Example:
[-10, -10, 5, 2], should return 500, since -10 * -10 * 5 

Assume that the list has 3 integers
"""
from itertools import combinations  

numbers = [-10, -10, 5, 2]

# first solution

def max_product_of_three(numbers):
    numbers.sort()

    product1 = numbers[-1] * numbers[-2] * numbers[-3]
    product2 = numbers[0] * numbers[1] * numbers[-1]  

    return max(product1, product2)

result1 = max_product_of_three(numbers)
print(result1)


# second solution

def max_product(numbers, num_of_items_to_multiply = 3):
    combination_list = list(combinations(numbers, num_of_items_to_multiply))
    max_product = float("-inf")

    for combo in combination_list:
        product = 1
        for num in combo:
            product *= num 
        if product > max_product:
            max_product = product

    return max_product

result2 = max_product(numbers)
print(result2)