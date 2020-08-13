import requests

def search(username):
    
    return requests.get('https://api.github.com/users/{}'.format(username))

def check(response):
    try:
        if response.status_code != 200:
            raise ValueError("\nUsuário não encontrado!\n")
        else:
            show(response.json())
    except ValueError as err:
        print(err)

def show(userData):
    print('\n\n===== Usuário Encontrado =====\n')
    print('\nNome: {}'.format(userData['name']))
    print('{} \n'.format(userData['bio']))
    print('Repositório público: {} \n'.format(userData['public_repos']))
    print('Seguidores: {} \n\n'.format(userData['followers']))

print('\n\n====== Buscar usuário do GitHub ======\n')

username = input('Digite o nome: ')

response = search(username)

check(response)