# Aula 7 – Stemming e Lematização

**Objetivo: ao fim desta aula, o aluno deverá saber aplicar e interpretar stemming e lematização para auxiliar no processo de análise automatizada de textos**

---

# Exercício 1
**Objetivo: entender o problema de termos flexões e variações de vocabulário na análise automatizada de textos**
 
Em textos livres sobre filmes, podemos nos referir a “personagem” ou “personagens”, e ambos – para fins de saber quais são nossos interesses – querem dizer a mesma coisa.

Se 50% das pessoas usam a palavra “personagem” no singular, e os outros 50% usam a palavra no plural, o que aconteceria com uma visualização de relevância de palavras?

---

# Exercício 2
**Objetivo:  encontrar o sufixo e a raiz de palavras**
 
Nas palavras abaixo, encontre quais têm o mesmo sufixo e quais têm a mesma raiz:

cantar, cantarei, cantaria, cantaremos, cantarolamos, cantoria, canto, falarei, falaria, fala,alegre, alegria, amor, amaria, amaremos

---

# Exercício 3
**Objetivo: analisar TF de palavras usando raízes sem sufixos**
 
No trecho abaixo, calcule o TF das palavras considerando (a) o trecho original e (b) somente as raízes das palavras, retirando os sufixos.

“fala falante falada falando falações faladas por faladores mudos”

(c) Qual é a diferença entre as informações que são representadas em cada um dos vetores de descrição que obtivemos nos itens (a) e (b)?


---

# Exercício 4
**Objetivo: usar um stemmer em NTLK**
 
O trecho de código abaixo invoca um removedor de sufixos (stemmer) para a palavra “wording”.

    !python
    from nltk.stem import SnowballStemmer
    stemmer = SnowballStemmer("english")
    stemmer.stem("wording")

(a) Qual é o resultado? Expanda o teste para outras palavras que você conhece e que tenham sufixos. Quais foram os resultados?

(b) Mude a língua do stemmer para “portuguese”. Ele ainda funciona?

(c) Use o SnowballStemmer em português para as palavras “fala” e “falante”. O que aconteceu?

(d) O RSLPStemmer é um stemmer feito especificamente para a língua portuguesa. Para usar, use o código abaixo. Teste o RSLPStemmer com as palavras “fala” e “falante”. Quais foram os resultados?

    !python
    from nltk.stem import RSLPStemmer
    stemmer = RSLPStemmer()
    stemmer.stem("palavras")



---

# Exercício 5
***Objetivo: verificar os efeitos de usar stemming na análise de textos em coleções***
No notebook desta aula, há um trecho de código para carregar a base de dados IMDB, realizar stemming de palavra em palavra, e então calcular o DF de cada stem.

Como esses resultados se comparam com os resultados obtidos sem usar stemming?

---

# Exercício 6
**Objetivo: encontrar lemas de palavras**

Em um dicionário, é evidente que não podemos ter entradas para todas as flexões de uma palavra. Por exemplo, os verbos são sempre mostrados no infinitivo, isto é, para saber o que significa “cantei” devemos procurar pela palavra “cantar”.

(a) Encontre a “entrada de dicionário” (ou seja, o lema) de cada uma das palavras abaixo:

Carrão | trenzinho | avião | aviões | aviação | voava | voar | voaremos

(b) O lema de uma palavra é o mesmo que sua raiz? Encontre um caso de palavra cujo lema seja diferente da raiz.

---

# Exercício 7
**Objetivo: usar um lematizador em NLTK**

No NLTK, já existe um lematizador para a língua inglesa:

    !python
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatizer.lemmatize("characters")


(a) Teste o lematizador com algumas palavras. Os resultados fazem sentido?

(b) Encontre uma palavra em que a lematização leve a um resultado diferente do stemming.

---

# Exercício 8
**Objetivo: analisar os efeitos de lematização na análise de textos.**

No notebook desta aula, há um trecho de código para carregar a base de dados IMDB, realizar lematização de palavra em palavra, e então calcular o DF de cada lema.

Como esses resultados se comparam com os resultados obtidos usando stemming? E com os resultados sem usar nenhuma das duas estratégias?

---

# Exercício 9
**Objetivo: comparar o funcionamento do stemmer e do lematizador**

(a) Qual é o princípio de funcionamento do stemmer? (fonte importante: https://www.cs.toronto.edu/~frank/csc2501/Readings/R2_Porter/Porter-1980.pdf)

(b) O lematizador com WordNet usa uma grande base de dados de palavras (a WordNet) para consultar lemas de palavras. Como isso é diferente do stemmer?

(c) Qual dos dois (stemmer ou lematizer) é mais fácil de portar para outras línguas? Por que? 

(d) Como stemming e lematização podem ajudar em sistemas de busca por conteúdo?

(e) Pelo que estudamos até o momento, stemming ou lematização devem ser realizados antes ou depois de um processo de part-of-speech tagging?



---

# Exercício 10 (para a próxima aula)
**Objetivo: estudar a WordNet**

Leia sobre a Wordnet (https://wordnet.princeton.edu/).

Quais são três possíveis tipos de perguntas que a WordNet pode nos ajudar a responder?

.qr: 450|https://wordnet.princeton.edu/

