import string
import random

def univers_func_str(inpt,):
    p = input(inpt).lower()
    if p == 'y' or p == 'n':
        return p
    return univers_func_str(inpt)

def univers_func_int(inpt):
    p = input(inpt)
    if p.isdigit():
        return int(p)
    return univers_func_int(inpt)

args = {
    'is_lower': univers_func_str('Использовать строчные буквы? [y/N]\n>'),
    'is_upper': univers_func_str('Использовать заглавные буквы? [y/N]\n>'),
    'is_digit': univers_func_str('Использовать числа? [y/N]\n>'),
    'is_symbl': univers_func_str('Использавть спец. символы? [y/N]\n>'),
    'len_pass': univers_func_int('Длинная пароля?\n>'),
    'numb_of_pass': univers_func_int('Кол-во паролей?\n>'),
}

def random_lowercase():
    len_st = len(string.ascii_lowercase) - 1
    return string.ascii_lowercase[random.randint(0, len_st)]

def random_uppercase():
    len_st = len(string.ascii_uppercase) - 1
    return string.ascii_uppercase[random.randint(0, len_st)]

def random_int():
    return string.digits[random.randint(0, 9)]

def random_spec_symbl():
    len_st = len(string.punctuation) - 1
    return string.punctuation[random.randint(0, len_st)]


def generate_password():
    password = ''

    def conditions(args, len_p, passd):
         if args == 'y' and len_p > len(passd):
             return True

    while args['len_pass'] > len(password):
        if conditions(args['is_lower'], args['len_pass'], password): password += random_lowercase()
        if conditions(args['is_upper'], args['len_pass'], password): password += random_uppercase()
        if conditions(args['is_digit'], args['len_pass'], password): password += random_int()
        if conditions(args['is_symbl'], args['len_pass'], password): password += random_spec_symbl()

    return password

def generate_passwords():
    pass_arr = []
    while args['numb_of_pass'] > len(pass_arr):
        pass_arr.append(generate_password())

    with open('passwords.txt', 'w', encoding='utf-8') as file:
        for s in pass_arr:
            file.write(s + '\n')

def run():
    generate_passwords()

if '__main__' == __name__:
    run()


