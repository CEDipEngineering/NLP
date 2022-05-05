from audioop import reverse
from functools import partial
from black import out
import mysql.connector
import re
from Levenshtein import distance as lev

# Class to help organize page scores
class Page():
    def __init__(self, url: str, id: int, tf_idf: float):
        self.url = url
        self.id = id
        self.tf_idf = tf_idf

    def __add__(self, other):
        return Page(self.url, self.id, self.tf_idf+other.tf_idf)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Page({self.url},{self.tf_idf})"

class Engine():

    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nlp',
            database='nlp',
        )
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT word FROM Words", None)
            self.all_words = [x for x in cursor]

    def search(self, word: str):
        word = re.sub("\[|\]|\(|\)|\n|\-|\.|\_|\;|\,", " ", word)
        word_list = re.split("\s+", word.lower())
        scores = []
        for w in word_list:
            if len(w)>0:
                scores.append(self.get_doc_scores(w))
        return self.merge_page_list(scores)

    def get_doc_scores(self, word) -> list:
        # Get 20 best tf_idfs for this word
        # Later, combine lists produced by this function to make 10 best matches.
        if word not in self.all_words:
            word = self.closest_match(word)[2]

        word_id = self.get_word_id(word)
        
        with self.connection.cursor() as cursor:
            query = """
            SELECT 
                url, id, tf_idf 
            FROM 
                Pages 
                INNER JOIN Words_To_Pages 
                ON (Words_To_Pages.id_Pages = Pages.id) 
            WHERE 
                Words_To_Pages.id_Words = {0} 
            ORDER BY tf_idf DESC 
            LIMIT 50
            """.format(word_id)
            cursor.execute(query, None)
            output = []
            for result in cursor:
                output.append(Page(url=result[0], id=result[1], tf_idf=result[2]))
            return output

    def merge_page_list(self, page_list):
        dict_pages = {}
        for k in page_list:
            for p in k:
                if p not in dict_pages:
                    dict_pages[p.id] = p
                else:
                    dict_pages[p.id] += p
        output = sorted(dict_pages.items(), key=lambda item: item[1].tf_idf, reverse=True)[:10]
        return [o[1].url for o in output]

    def get_word_id(self, word):
        ## Warning
        ## Will raise index out of range exception if word is not in self.all_words
        with self.connection.cursor() as cursor:
            query = "SELECT id FROM Words WHERE word = \"{0}\"".format(word)
            cursor.execute(query, None)
            result_ids = []
            for result in cursor:
                result_ids.append(result)
        return result_ids[0][0]

    def closest_match(self, word):
        matches = [[lev(word, self.all_words[i][0]), i, self.all_words[i][0]] for i in range(len(self.all_words))]
        return sorted(matches)[0]
