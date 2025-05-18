import spacy

# Carregar o modelo em português do spaCy
nlp = spacy.load('pt_core_news_sm')

# Função para classificar sentenças como "positivo" ou "negativo"
def classify_sentence(sentence):
    doc = nlp(sentence)

    positive_adjectives = ['ótimo', 'excelente', 'incrível', 'fantástico', 'maravilhoso',
    'esplêndido', 'formidável', 'impecável', 'admirável', 'brilhante',
    'eficiente', 'agradável', 'genial', 'sensacional', 'encantador',
    'valioso', 'competente', 'respeitável', 'exemplar', 'notável']

    negative_adjectives = ['ruim', 'péssimo', 'horrível', 'terrível', 'lamentável',
    'medíocre', 'inaceitável', 'sofrível', 'decepcionante', 'inútil',
    'incompetente', 'insatisfatório', 'desagradável', 'fraco', 'problemático',
    'desastroso', 'ineficiente', 'reprovável', 'questionável', 'ridículo']


    # Verificar a presença de palavras-chave
    if any(token.lemma_ in positive_adjectives for token in doc):
        return "positivo"
    elif any(token.lemma_ in negative_adjectives for token in doc):
        return "negativo"
    else:
        return "neutro"

# Exemplos de sentenças para classificação
sentences = [
    "O tempo hoje está terrível",
    "Aquele filme é muito péssimo.",
    "Essa foi a formidável viagem da minha vida.",
    "O resultado da prova foi notável."
]

# Classificar e imprimir os resultados
for sentence in sentences:
    classification = classify_sentence(sentence)
    print(f"Sentença: '{sentence}' - Classificação: {classification}")