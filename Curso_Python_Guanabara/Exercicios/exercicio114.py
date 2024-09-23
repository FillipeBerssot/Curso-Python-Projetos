# Ex. 114- Crie um codigo em Python que teste se o site Pudim está acessivel pelo computador usado:

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print('O site Pudim não está acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso.')

