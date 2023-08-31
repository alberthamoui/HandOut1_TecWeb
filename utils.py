import json
from database import *

def extract_route(request):
    linhas = request.split('\n')
    path = linhas[0].split(' ')[1]
    return path[1:]

def read_file(path):
    with open(path, 'rb') as file:
        content = file.read()
    file.close()
    return content


def load_data():
    db = Database('banco')
    notes = db.get_all()
    return notes


def load_template(arquive):
    path = "templates/{nome}".format(nome=arquive)
    with open(path, 'r',encoding='utf-8') as file:
        content = file.read()
    return content


def build_response(body='', code=200, reason='OK', headers=''):
    if headers=='':
        string = "HTTP/1.1 {code} {reason}\n\n{body}".format(code=code, reason=reason, headers=headers, body=body)
    else:
        string = "HTTP/1.1 {code} {reason}\n{headers}\n\n{body}".format(code=code, reason=reason, headers=headers, body=body) 
    return string.encode()


# 'HTTP/1.1 200 OK\n\nbody of the response'