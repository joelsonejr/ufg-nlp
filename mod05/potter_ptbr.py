# Incluir código fonte da Tarefa 6.2 aqui
def stemmer_portugues(palavra):
    """
    Adaptando para o idioma Portugês(BR)
    """
    sufixos = [
        'mente', 'ções', 'sões', 'ção', 'são', 'mente', 'izar', 'izaram', 'izando',
        'icamente', 'idades', 'idade', 'ivo', 'iva', 'ivos', 'ivas', 'ável', 'ível',
        'eza', 'ezas', 'ista', 'istas', 'oso', 'osa', 'osos', 'osas'
    ]

    for sufixo in sufixos:
        if palavra.endswith(sufixo):
            return palavra[:-len(sufixo)]
    return palavra

# Exemplo com frase
frase = "As organizações estavam funcionando perfeitamente e eficazmente"
palavras = frase.lower().split()

stemmed = [stemmer_portugues(palavra) for palavra in palavras]

print("Frase original:", frase)
print("Palavras com stemming aplicado:", stemmed)