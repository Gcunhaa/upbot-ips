import requests
from bs4 import BeautifulSoup
from requests.api import request

from core.urls import Urls

"""[summary]
    Acessa página para gerar csrfKey e retorna ela.
"""
def get_csrfkey(session : requests.Session) -> str:  

    page = session.get(Urls.login.value)

    soup = BeautifulSoup(page.content, 'html.parser')

    return soup.find('input', attrs={'name':'csrfKey'})['value']

"""[summary]
    Verifica se o usuário conseguiu logar com sucesso e se os parametros estão corretos
    Retorna verdadeiro se o login funcionou, retorna falso se o login falhou.
"""
def verify_login(request) -> bool:
    soup = BeautifulSoup(request.content,'html.parser')
    usuario = 'O Nome de usuário ou endereço de e-mail que você informou não pertence a nenhuma conta'
    senha = 'A senha informada está incorreta'
    return not usuario in soup.get_text() and not senha in soup.get_text()