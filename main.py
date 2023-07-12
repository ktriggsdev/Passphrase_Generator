import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

pass_sect_1 = generate_password(12)
pass_sect_2 = generate_password(12)
pass_sect_3 = generate_password(12)
pass_sect_4 = generate_password(12)

passphrase = pass_sect_1 + "~" + pass_sect_2 + "~" + pass_sect_3 + "~" + pass_sect_4
print(passphrase)