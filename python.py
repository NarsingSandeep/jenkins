import math
import statistics
import random

def dict_operations(numbers):
    data = {'sum': sum(numbers), 'max': max(numbers), 'min': min(numbers)}
    return data

def sqrt_of_list(numbers):
    return [round(math.sqrt(x), 2) for x in numbers]

def multiply_with_random(numbers):
    return [x * random.randint(1, 10) for x in numbers]

def calculate_mean(numbers):
    return statistics.mean(numbers)

def calculate_median(numbers):
    return statistics.median(numbers)

def calculate_mode(numbers):
    return statistics.mode(numbers)

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Square root of list:", sqrt_of_list(numbers))
    print("Multiplied with random values:", multiply_with_random(numbers))
    print("Mean:", calculate_mean(numbers))
    print("Median:", calculate_median(numbers))
    print("Mode:", calculate_mode(numbers))
    print("Dictionary operations:", dict_operations(numbers))

if __name__ == "__main__":
    main()