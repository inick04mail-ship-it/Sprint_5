import random
import string


def generate_random_string(length: int) -> str:
   
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_unique_email(cohort_number: int = 1999) -> str:
    
    # случайное имя 5 букв
    name = generate_random_string(5)
    
    # случайная фамилия 6 букв
    surname = generate_random_string(6)
    
    # 3 случайные цифры
    random_digits = ''.join(random.choice(string.digits) for _ in range(3))
 
    return f"{name}{surname}{cohort_number}{random_digits}@yandex.ru"


def generate_password(min_length: int = 6) -> str:
    
    # минимальная длина
    if min_length < 6:
        min_length = 6
    
    # наборы символов
    lowercase = string.ascii_lowercase  
    uppercase = string.ascii_uppercase  
    digits = string.digits              
    
    # разные типы символов
    password_chars = [
        random.choice(lowercase),  
        random.choice(uppercase),  
        random.choice(digits)      
    ]
    
   
    all_chars = lowercase + uppercase + digits
    password_chars += [random.choice(all_chars) for _ in range(min_length - 3)]
    
    
    random.shuffle(password_chars)
    return ''.join(password_chars)


def generate_incorrect_password() -> str:
 
    # Случайная длина от 1 до 5
    length = random.randint(1, 5)
    
    # Генерируем короткий пароль
    return generate_random_string(length)


# примеры
if __name__ == "__main__":
    print("=" * 50)
    print("Примеры работы генераторов:")
    print("=" * 50)
    print(f"Случайная строка (5 символов): {generate_random_string(5)}")
    print(f"Уникальный email: {generate_unique_email()}")
    print(f"Пароль (6 символов): {generate_password()}")
    print(f"Некорректный пароль: {generate_incorrect_password()}")
    print("=" * 50)