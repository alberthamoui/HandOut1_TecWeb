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