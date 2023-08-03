import random

def get_random_string():
    strings = ["Hello", "World", "Python", "Programming", "AI"]
    return random.choice(strings)

def len_random_string():
    random_string = get_random_string()
    return len(random_string)