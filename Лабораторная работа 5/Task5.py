import random
import string

def get_random_password() -> str:
    n = input('Введите длину пароля:')
    if n == '':
        n = 8
    else:
        n = int(n)

    return ''.join(random.sample
                   ((string.ascii_uppercase + string.ascii_lowercase + string.digits), n))

print(get_random_password())
