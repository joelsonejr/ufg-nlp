import numpy as np
import pandas as pd
import unidecode
from nltk.tokenize import RegexpTokenizer

df_original = pd.read_csv('./olist.csv')

# exibindo review_text, da linha 1
df_original.iloc[1]['review_text']

# selecionando colunas
df = df_original[['review_text', 'review_text_processed', 'polarity']]

# exibindo review_text_processed do novo agrupamento
df.iloc[1]['review_text_processed']

# texto para normalização
exemplo = 'EXCELENTE!! Valeu demais passar um tempo pesquisando preços, pois encontrei esse ótimo carregador de celular, nota 10.'

# normalizando capitalização
print ("Antes de normalizar: \n")
print(exemplo)
exemplo = exemplo.lower()
print ("\n\n")
print ("Depois de de normalizar: \n")
print(exemplo)

# vizualizando valores da coluna review_text
df['review_text']

# normalizando todas as linhas da coluna review_text
df['review_preproc'] = df['review_text'].apply(lambda x: x.lower())

# removendo pontuação - método 01
# Analisar caractere a caractere e mandar na string sem pontuação somente os caracteres desejáveis.
exemplo_sem_punct = "".join(u for u in exemplo if u not in ("?", ".", ";", ":", "!", ","))

# removendo pontuação - método 02
# Usar o RegexTokenizer da lib NLTK 

# com '\w+' selecionamos apenas tokens de palavras ou dígitos
tokenizer = RegexpTokenizer(r'\w+')

# atualizando os valores das colunas
df['review_preproc'] = df['review_preproc'].apply(lambda x: ' '.join(tokenizer.tokenize(x)))

#retirar acentos
# Opção 1: Criar um mapeamento de caracteres acentuados para caracteres sem acento
repl = str.maketrans(
    "áéúíó",
    "aeuio"
)
palavra = 'ótimo'
palavra.translate(repl)

#retirar acentos
# Opção 2: Usar lib unidecode
# !pip install unidecode
exemplo.split()
exemplo = ' '.join([unidecode.unidecode(termo) for termo in exemplo.split()])


# atualizando os dados
df['review_preproc'] = df['review_preproc'].apply(lambda x: ' '.join([unidecode.unidecode(termo) for termo in x.split()]))

# remoção de stopwords
stopwords = ['de', 'para', 'uma', 'o', 'e'] # aqui listamos as palavras que mais se repetem, de acordo com o domínio de aplicação

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese') # este é um conjunto de palavras elencado por especialistas, os quais via estudo, identificaram que se repetem com frequencia.

exemplo = ' '.join([termo for termo in exemplo.split() if termo not in stopwords])

# removendo stopwords de toda a coluna
df['review_preproc'] = df['review_preproc'].apply(lambda x: ' '.join([termo for termo in x.split() if termo not in stopwords]))

# stemização
nltk.download('rslp')
stemmer = nltk.stem.RSLPStemmer()

exemplo = ' '.join([stemmer.stem(termo) for termo in exemplo.split()])

# atualizando os valores das colunas
df['review_preproc'] = df['review_preproc'].apply(lambda x: ' '.join(stemmer.stem(termo) for termo in x.split()))