import requests

def search(username):
    
    return requests.get('https://api.github.com/users/{}'.format(username))

def check(response):
    try:
        if response.status_code != 200:
            raise ValueError("\nUsuário não encontrado!\n")
        else:
            print(response.json())
    except ValueError as err:
        print(err)

print('\n\n====== Buscar usuário do GitHub ======')

username = input('Digite o nome: ')

response = search(username)

check(response)