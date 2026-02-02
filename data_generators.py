import random
import string


def generate_random_string(length: int) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def generate_unique_email(cohort_number: int = 1999) -> str:
    """Генерация уникального email с использованием случайных букв и цифр."""
    name = generate_random_string(5)
    surname = generate_random_string(6)
    random_digits = "".join(random.choice(string.digits) for _ in range(3))
    return f"{name}{surname}{cohort_number}{random_digits}@yandex.ru"


def generate_password(min_length: int = 6) -> str:
    """Генерация валидного пароля: минимум одна строчная, прописная буква и цифра."""
    if min_length < 6:
        min_length = 6

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
    ]

    all_chars = lowercase + uppercase + digits
    password_chars += [random.choice(all_chars) for _ in range(min_length - 3)]

    random.shuffle(password_chars)
    return "".join(password_chars)


def generate_incorrect_password() -> str:
    """Генерация некорректного (слишком короткого) пароля."""
    length = random.randint(1, 5)
    return generate_random_string(length)
