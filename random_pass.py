import random
import string

def generate_password(length=10):
    list_alp = list(string.ascii_letters)
    list_spl = list(string.digits + string.punctuation)
    password_list = []
    password_list.extend(random.choices(list_alp, k=length//2))
    password_list.extend(random.choices(list_spl, k=length - len(password_list)))
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
print("--------------------------------------------------")
print("Here it is your strong password",generate_password())
print("--------------------------------------------------")






