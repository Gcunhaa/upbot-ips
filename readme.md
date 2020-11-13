# Upbot for IPS

![Screenshot from 2020-11-13 11-04-38](https://user-images.githubusercontent.com/28935645/99080867-ac430300-25a0-11eb-944c-d1fd827cd1ee.jpg)


This is a forum bot for getting your topics in the recent discussions, it will basically send a comment on a specific topic that is inside the topics.txt file. It's currently setup to run on https://gamersboard.com.br, you can make some tweaks to work on others forum's too.

### Installation

You should have python 3 and pip installed. Then you need to create the virtual enviroment and run it:
(If you are using windows just google how to run a python virtual enviroment)
```sh
$ python -m venv venv
$ source /venv/bin/activate
```
Install the projects dependencies:
```sh
$ pip install -R requirements.txt
```

Now it's ready to run.

### Run

First of all you should add topics on the topics.txt file. You should have one url per line, like that:
```
https://gamersboard.com.br/topic/41223-gcplugins-lista-de-plugins-free/
https://gamersboard.com.br/topic/60907-logincaptcha-o-seu-plugin-de-captcha-ap%C3%B3s-o-login/
```

Every time you want to run the bot, you should start the virtual enviroment (if you want to deactivate, just type in the shell deactivate)

```sh
$ source /venv/bin/activate
```

Then just run the main.py script, and fill your account and password, everything should run smoothly:
```sh
$ python main.py
```

