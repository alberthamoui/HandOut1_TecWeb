from utils import load_data, load_template, build_response
from urllib.parse import unquote_plus
from database import *


def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            titulo,texto = chave_valor.split('=')
            params[titulo] = unquote_plus(texto)

        db = Database('banco')
        db.add(Note(title=list(params.values())[-2], content=list(params.values())[-1]))

        return build_response(code=303, reason='See Other', headers='Location: /')
        # print(params)
    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content, id=dados.id)
        for dados in load_data()
        # note_template.format(title=dados['titulo'], details=dados['detalhes'])
        # for dados in load_data('notes.json')

    ]
    notes = '\n'.join(notes_li)

    body = load_template('index.html').format(notes=notes)
    return build_response(body)