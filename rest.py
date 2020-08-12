import requests

def search(username):
    
    response = requests.get('https://api.github.com/users/{}'.format(username))

    try:

        if response.status_code != 200:
            raise ValueError("\nUsuário não encontrado!\n")
        else:
            print(response.json())

    except ValueError as err:
        print(err)

print('\n\n====== Buscar usuário do GitHub ======')

username = input('Digite o nome: ')

search(username)