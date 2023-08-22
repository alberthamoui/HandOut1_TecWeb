import json

def extract_route(request):
    linhas = request.split('\n')
    path = linhas[0].split(' ')[1]
    return path[1:]

def read_file(path):
    with open(path, 'rb') as file:
        content = file.read()
    file.close()
    return content

def load_data(arquive):
    path = "data/{nome}".format(nome=arquive)
    with open(path, 'r') as file:
        dic = json.load(file)
    return dic

def load_template(arquive):
    path = "templates/{nome}".format(nome=arquive)
    with open(path, 'r') as file:
        content = file.read()
    return content

def build_response(body='', code=200, reason='OK', headers=''):
    response = f'HTTP/1.1 {code} {reason}\n'
    if headers:
        response += f'{headers}\n'
    response += '\n'
    if body:
        response += f'{body}'
    return response.encode()
