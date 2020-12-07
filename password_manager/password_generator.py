# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PasswordGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate() -> str:
        random_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
        random_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
        random_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
        password_pool = random_letters + random_symbols + random_numbers
        random.shuffle(password_pool)
        return "".join(password_pool)
