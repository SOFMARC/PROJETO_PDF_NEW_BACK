import re

def remove_number_to_text(text):
    numeros = re.findall(r'\d+[\.\,\d]*', text) # Encontra todos os números com ponto ou vírgula
    numeros_x = re.findall(r'x\d+[\.\,\d]*', text) # Encontra todos os números com x e ponto ou vírgula

    for n in numeros_x:
        numeros.append(n[1:]) # Remove o x do começo dos números com x

    return numeros