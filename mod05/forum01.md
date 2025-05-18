a. 
Feito

b. 
Atividade 01: "falando falou falam diversos separados"
Atividade 02: "A mouse runs on the yard."
Atividade 03: 'dormindo', 'dormiu', 'dormem', 'felizmente', 'inicialmente'
              'sleeping', 'slept', 'sleep', 'happily', 'initially'
Atividade 04: 'dormindo', 'dormiu', 'dormem', 'felizmente', 'inicialmente'

c. 
Saída atividade 01
    ['falar', 'falar', 'falar', 'diverso', 'separado']

Saída atividade 02
    A (DT) mouse (NN) runs (VBZ) on (IN) the (DT) yard (NN) . (.)

Saída atividade 03
    Stemming em português (RSLP): ['dorm', 'dorm', 'dorm', 'feliz', 'inic']
    Stemming em inglês (Snowball): ['sleep', 'slept', 'sleep', 'happili', 'initi']

Saída atividade 04
    Palavra             Palavra Lematizada  Palavra_stemmed
    ----------------------------------------------------------
    dormindo            dormir              dorm
    dormiu              dormir              dorm
    dormem              dormer              dorm
    felizmente          felizmente          feliz
    inicialmente        inicialmente        inic

d. 
A técnica de Steamming remove o final das palavras, reduzindo-as ao seu radical.
Ele não considera o contexto, o que faz com que o resultado seja menos preciso,
porém mais eficiente.

A técnica de Lematização analisa o contexto, utilizando regras gramaticais para
encontrar o lema da palavra. Isso faz com que o precesso sejam mais lento, porém
mais preciso.
