# Etapa 1: Verificação e Instalação das Bibliotecas Necessárias
import subprocess
import sys

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Instalar as bibliotecas necessárias
install_and_import('spacy')
install_and_import('nltk')
install_and_import('scikit-learn')
install_and_import('pandas')

# Baixar o modelo de português do spaCy, caso não esteja instalado
subprocess.run([sys.executable, "-m", "spacy", "download", "pt_core_news_sm"])

# Etapa 2: Importar as Bibliotecas e Inicializar Recursos
import spacy
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Baixar recursos necessários do nltk para stemming e lematização
nltk.download('rslp')  # Baixar o stemmer RSLP para português
nltk.download('wordnet')  # Baixar o WordNet para lematização
nltk.download('omw-1.4')  # Baixar o Open Multilingual Wordnet
nltk.download('punkt')  # Baixar o tokenizer 'punkt' para português

from nltk.stem import RSLPStemmer
from nltk.stem import WordNetLemmatizer

# Carregar o modelo de português do spaCy
nlp = spacy.load("pt_core_news_sm")

# Inicializar o lematizador e o stemmer
lemmatizer = WordNetLemmatizer()
stemmer = RSLPStemmer()

# Etapa 3: Definir Funções de Pré-Processamento

# Função de lematização usando spaCy
# Esta função utiliza o spaCy para lematizar o texto, retornando os lemas dos tokens.
def lematizar(texto):
    doc = nlp(texto)
    return ' '.join([token.lemma_ for token in doc])

# Função de stemming usando NLTK
# Esta função utiliza o nltk para aplicar stemming aos tokens do texto.
def aplicar_stemming(texto):
    tokens = nltk.word_tokenize(texto, language='portuguese')
    return ' '.join([stemmer.stem(token) for token in tokens])

# Função de pré-processamento completo
# Esta função aplica lematização seguida de stemming ao texto.
def preprocessamento(texto):
    texto_lematizado = lematizar(texto)
    texto_stemmed = aplicar_stemming(texto_lematizado)
    return texto_stemmed

# Etapa 4: Pré-Processar Documentos e Calcular TF-IDF

# Lista de documentos de exemplo para indexação
documentos = [
    "O gato está correndo no jardim.",
    "Os gatos gostam de correr e brincar.",
    "Ela gosta de estudar linguística computacional.",
    "Linguística computacional é uma área fascinante.",
    "O gato preto da Renata dorme na varanda.",
    "A inteligência artificial está transformando a indústria global.",
    "O novo presidente anunciou reformas econômicas importantes.",
    "Vacinas são essenciais para prevenir doenças graves.",
    "A floresta amazônica sofre com o desmatamento acelerado.",
    "Professores discutem novas metodologias de ensino à distância.",
    "O time venceu o campeonato com uma virada histórica.",
    "A inflação afeta o poder de compra das famílias brasileiras.",
    "A Segunda Guerra Mundial começou em 1939 e envolveu várias nações.",
    "A cantora lançou um álbum que mistura pop e música eletrônica.",
    "O novo filme da Marvel bateu recordes de bilheteria."
]

# Aplicar pré-processamento em todos os documentos
# Esta linha aplica a função de pré-processamento em cada documento.
documentos_preprocessados = [preprocessamento(doc) for doc in documentos]

# Exibir os documentos preprocessados
print("Documentos Preprocessados:")
for doc in documentos_preprocessados:
    print(doc)

# Inicializar o vetor TF-IDF
vectorizer = TfidfVectorizer()

# Ajustar e transformar os documentos preprocessados
# Esta linha ajusta e transforma os documentos preprocessados em uma matriz TF-IDF.
tfidf_matrix = vectorizer.fit_transform(documentos_preprocessados)

# Obter os termos (features) do TF-IDF
termos = vectorizer.get_feature_names_out()

# Exibir a matriz TF-IDF usando um DataFrame para melhor visualização
df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=termos)

# Exibir a matriz TF-IDF
print("Matriz TF-IDF:")
print(df_tfidf)

# Etapa 5: Consulta de Documentos e Calcular Similaridade

# Função para processar consulta e calcular similaridade
# Esta função pré-processa a consulta, transforma em vetor TF-IDF e
# calcula a similaridade coseno.
def consultar_documentos(consulta):
    consulta_preprocessada = preprocessamento(consulta)
    consulta_tfidf = vectorizer.transform([consulta_preprocessada])
    similaridades = cosine_similarity(consulta_tfidf, tfidf_matrix)
    documento_mais_similar = similaridades.argmax()
    return documento_mais_similar, similaridades

# Exemplo de consultas
consultas = [
    "gato no jardim",
    "estudar linguística",
    "gato da Renata"
]

# Processar cada consulta e exibir resultados
for consulta in consultas:
    indice, similaridades = consultar_documentos(consulta)
    print(f"Consulta: '{consulta}'")
    print(f"Documento mais similar: {documentos[indice]}")
    print(f"Similaridades: {similaridades}\n")
