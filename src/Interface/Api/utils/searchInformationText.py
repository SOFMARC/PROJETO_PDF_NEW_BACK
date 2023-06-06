import re

def searchInformationText(expressao, texto):
    res = re.compile(expressao)
    busca = res.search(texto)
    result = busca.group()

    return result