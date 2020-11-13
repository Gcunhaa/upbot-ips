import requests
import sys
from colorama import Fore

from core.urls import Urls
from core.utils import verify_login, get_csrfkey


"""[summary]
    Classe responsável por cuidar do client e conexão com o servidor.
"""
class Bot():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.headers.update({"User-Agent" : "Mozilla/5.0"})
        self.auth()

    """[summary]
        Método responsável pela autentificação do usuário na gamersboards.
    """
    def auth(self):
        print(Fore.YELLOW + '[!] Bot inciado')
        print(Fore.YELLOW + f'[!] Logando no usuário: {self.username}')
        
        payload = {
            'csrfKey' : get_csrfkey(self.session),
            'auth' : self.username,
            'password' : self.password,
            'remember_me' : '1',
            '_processLogin' : 'usernamepassword',
            '_processLogin': 'usernamepassword'
        }

        try:
            request = self.session.post(Urls.login.value, params=payload)
            
            if not verify_login(request):
                print(Fore.RED + '[-] Usuário ou senha incorreto.')
                sys.exit()

        except requests.exceptions.RequestException as e:
            print(Fore.RED + '[-] Algum erro aconteceu ao fazer o login!')
            sys.exit()
        
        print(Fore.GREEN + '[+] Logado com sucesso.')
    

    """[summary]
        Método responsável por impulsionar o tópico    
    """
    def bump_topic(self, topic_url : str):
        print(Fore.YELLOW + f'[!] Impulsionando o tópico: {topic_url}')

        payload = {
            'do' : 'bump',
            'csrfKey' : get_csrfkey(self.session)
        }

        error = False

        try:
            request = self.session.post(topic_url, params=payload)
        except  requests.exceptions.RequestException as e:
            print(Fore.RED + '[-] Algum erro aconteceu ao impulsionar o tópico, indo para o próximo...')
            error = True

        if not error:
            print(Fore.GREEN + '[+] Tópico impulsionado com sucesso.')
     