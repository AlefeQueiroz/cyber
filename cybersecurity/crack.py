import string
import itertools

def generate_passwords(min_length=1, max_length=8):

    characters = string.ascii_letters + string.digits + string.punctuation

    for length in range(min_length, max_length + 1):
        for password in itertools.product(characters, repeat=length):
            yield ''.join(password)

# Imprimir todas as senhas possíveis
print("Todas as senhas possíveis de 1 a 8 caracteres:")
print()

for password in generate_passwords():
    print(password)