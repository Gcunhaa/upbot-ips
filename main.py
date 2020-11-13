from core.client import Bot
from colorama import init
from pyfiglet import Figlet


init()

font = Figlet(font='slant')
print(font.renderText('GB Bump Bot'))
print('Desenvolvido por Gabriel Cunha')
print('')
print('')
print('')

username = str(input('Informe o nome do usuário: '))
password = str(input('Informe a senha do usuário: '))
print('')
print('')

#Inicia a conexão com fórum e o devido usuario
client = Bot(username=username, password=password)

#Faz um looping pelos tópicos no arquivo topics.txt
with open('topics.txt', 'r') as file:
    for topic_url in file.readlines():
        client.bump_topic(topic_url=topic_url)
