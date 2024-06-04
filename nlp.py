import nltk
import re
from nltk import word_tokenize , pos_tag , ngrams , sent_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.corpus import stopwords
import pandas as pd
from sqlalchemy import create_engine
from List import List


def removeStopWords(text):
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
    return filtered_words

def questions():
    file_path = 'questions.txt'
    with open(file_path, 'r') as file:
        text = file.read().splitlines()
    return text

def setOfText(text):
    result = set()
    l = List()
    for i in text:
        for num ,  j in enumerate(l):
            if i.lower() in j:
                result.add(num)
                break

    return result

def chatBot(tag , tokens):
    company = ['xiomi','samsang','apple','redmi','techno','infinix','vivo','oppo']
    bst ='-'
    top_num  = 0
    engine = create_engine('mysql+pymysql://root:mM.1aA2aA3zZ4$@localhost/PAI')
    result = 'nothing found sorry'
    price = []
    rate = []
    specs = []
    name = '-'
    und = '-'
    abv = '-'
    for i , j in enumerate(tag):
        if j[1] == "CD":
            alpha1 = j[0]
            if 'k' in alpha1.lower():
                price.append(alpha1)
            elif '.' in alpha1:
                rate.append(alpha1)
            elif 'gb' in alpha1.lower():
                specs.append(alpha1)
            else:
                alphab = tag[i-1]
                if alphab[0].lower() == "best"  or alphab[0].lower() == "top":
                    pass
                else:
                    price.append(alpha1)
        if j[0].lower() in company: 
            name = j[0]



    
    for j , i in enumerate(tokens):
        if i.lower() == 'under' or i.lower() == 'below':
            und = 'a'
        if i.lower() == 'above':
            abv = 'a'
    post = pos_tag(tokens)
    for i , j in enumerate(post):
        if j[0].lower() == 'best' or j[0].lower() == 'top':
            bst = 'o'
            alphab = post[i+1]
            if alphab[1] == "CD":
                top_num = int(alphab[0])
                print(bst)
    p1 = []
    ram = []
    rom = []
    for i in range(len(price)):
        alpha2 = price[i]
        if len(alpha2) < 2:
            rate.append(alpha2)
        else:
            p1.append(int(alpha2.replace('K','000').replace('k','000')))

    for i in range(len(rate)):
        rate[i] = float(rate[i])

    for i in range(len(specs)):
        alpha3 = specs[i]
        if len(alpha3) < 4:
            ram.append(alpha3)
        else:
            rom.append(alpha3)
    if len(p1) == 2 and name != '-':
        df3 = 'ROBO : The mobiles in the price range between '+ str(min(p1)) + ' and ' + str(max(p1)) +' are given below \n'
        df1 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE LOWER(company) IN ('{name}') AND price >= {min(p1)} AND price <= {max(p1)}" , con=engine)['price'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE LOWER(company) IN ('{name}') AND price >= {min(p1)} AND price <= {max(p1)}" , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE LOWER(company) IN ('{name}') AND price >= {min(p1)} AND price <= {max(p1)}" , con=engine)['score'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE LOWER(company) IN ('{name}') AND price >= {min(p1)} AND price <= {max(p1)}" , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df1,
            'score' : df4,
            'specs' :df5
        }
        if bst != '-' and top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
                
        return dict

    if len(rate) == 2 and name != '-':
        df3 = 'ROBO : The mobiles in the score range between '+ str(min(rate)) + ' and ' + str(max(rate)) +' are given below \n'
        df1 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE LOWER(company) IN ('{name}') AND score >= {min(rate)} AND score <= {max(rate)}" , con=engine)['score'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE LOWER(company) IN ('{name}') AND score >= {min(rate)} AND score <= {max(rate)}" , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE LOWER(company) IN ('{name}') AND score >= {min(rate)} AND score <= {max(rate)}" , con=engine)['price'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE LOWER(company) IN ('{name}') AND score >= {min(rate)} AND score <= {max(rate)}" , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df4,
            'score' : df1,
            'specs' :df5
        }
        if bst != '-' and top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
             
        return dict


    elif len(p1) == 2:
        df3 = 'ROBO : The mobiles in the price range between '+ str(p1[0]) + ' and ' + str(p1[1]) +' are given below \n'
        df1 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE price BETWEEN {p1[0]} AND {p1[1]}" , con=engine)['price'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE price BETWEEN {p1[0]} AND {p1[1]}" , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE price BETWEEN {p1[0]} AND {p1[1]}" , con=engine)['score'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE price BETWEEN {p1[0]} AND {p1[1]}" , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df1,
            'score' : df4,
            'specs' :df5
        }
        if bst != '-' and top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
             
        return dict

    elif len(rate) == 2:
        df3 = 'ROBO : The mobiles in the score range between '+ str(min(rate)) + ' and ' + str(max(rate)) +' are given below \n'
        df1 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE score BETWEEN {min(rate)} AND {max(rate)}" , con=engine)['score'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE score BETWEEN {min(rate)} AND {max(rate)}" , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE score BETWEEN {min(rate)} AND {max(rate)}" , con=engine)['price'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE score BETWEEN {min(rate)} AND {max(rate)}" , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df4,
            'score' : df1,
            'specs' :df5
        }
        if bst != '-' and top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
             
        return dict
    elif len(p1) == 1 and abv != '-' and name !='-':
        df3 = 'ROBO : The mobiles in the price range above ' + str(p1[0]) +' are given below \n'
        df1 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE LOWER(company) IN ('{name}') AND price >= {p1[0]}" , con=engine)['score'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE LOWER(company) IN ('{name}') AND price >= {p1[0]}" , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE LOWER(company) IN ('{name}') AND price >= {p1[0]}" , con=engine)['price'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE LOWER(company) IN ('{name}') AND price >= {p1[0]}" , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df4,
            'score' : df1,
            'specs' :df5
        }
        if bst != '-' and top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
             
        return dict
    elif len(p1) == 1 and und != '-' and name !='-':
        df3 = 'ROBO : The mobiles in the price range above ' + str(p1[0]) +' are given below \n'
        df1 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE LOWER(company) IN ('{name}') AND price <= {p1[0]}" , con=engine)['score'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE LOWER(company) IN ('{name}') AND price <= {p1[0]}" , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE LOWER(company) IN ('{name}') AND price <= {p1[0]}" , con=engine)['price'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE LOWER(company) IN ('{name}') AND price <= {p1[0]}" , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df4,
            'score' : df1,
            'specs' :df5
        }
        if bst != '-' and top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
             
        return dict

    elif len(p1) == 1 and abv != '-':
        df3 = 'ROBO : The mobiles in the price range above ' + str(p1[0]) +' are given below \n'
        df1 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE price >= {p1[0]}" , con=engine)['score'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE price >= {p1[0]}" , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE price >= {p1[0]}" , con=engine)['price'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE price >= {p1[0]}" , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df4,
            'score' : df1,
            'specs' :df5
        }
        if bst != '-' and top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
             
        return dict

    

        
    elif len(p1) == 1 and und != '-':
        df3 = 'ROBO : The mobiles in the price range below ' + str(p1[0]) +' are given below \n'
        df1 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE price <= {p1[0]}" , con=engine)['score'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE price <= {p1[0]}" , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE price <= {p1[0]}" , con=engine)['price'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE price <= {p1[0]}" , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df4,
            'score' : df1,
            'specs' :df5
        }
        if bst != '-' and top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
             
        return dict   

    elif len(rate) == 1 and abv != '-':
        df3 = 'ROBO : The mobiles in the price score above ' + str(rate[0]) +' are given below \n'
        df1 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE score >= {rate[0]}" , con=engine)['score'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE score >= {rate[0]}" , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE score >= {rate[0]}" , con=engine)['price'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE score >= {rate[0]}" , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df4,
            'score' : df1,
            'specs' :df5
        }
        if bst != '-' and top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
             
        return dict   

    elif len(rate) == 1 and und != '-':
        df3 = 'ROBO : The mobiles in the score range below ' + str(rate[0]) +' are given below \n'
        df1 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE score <= {rate[0]}" , con=engine)['score'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE score <= {rate[0]}" , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE score <= {rate[0]}" , con=engine)['price'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE score <= {rate[0]}" , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df4,
            'score' : df1,
            'specs' :df5
        }
        if bst != '-' and top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
             
        return dict
    elif len(rate) == 0 and len(p1) == 0 and len(ram) == 0 and len(rom) == 0 and name != '-':
        df3 = 'ROBO : The mobiles of the brand '+ name +' are given below \n'
        df1 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE LOWER(company) IN ('{name}') " , con=engine)['score'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE LOWER(company) IN ('{name}') " , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE LOWER(company) IN ('{name}') " , con=engine)['price'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE LOWER(company) IN ('{name}') " , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df4,
            'score' : df1,
            'specs' :df5
        }
        if bst != '-' and top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
             
        return dict
    elif len(rate) == 0 and len(p1) == 0 and len(ram) == 0 and len(rom) == 0 and name == '-' and bst !='-':
        print("sdsdsds")
        df1 = list(pd.read_sql(f"SELECT score FROM data_1 WHERE score >= 4.8" , con=engine)['score'])
        df2 = list(pd.read_sql(f"SELECT name FROM data_1 WHERE score >= 4.8" , con=engine)['name'])
        df4 = list(pd.read_sql(f"SELECT price FROM data_1 WHERE score >= 4.8" , con=engine)['price'])
        df5 = list(pd.read_sql(f"SELECT specs FROM data_1 WHERE score >= 4.8 " , con=engine)['specs'])
        dict = {
            'name' : df2,
            'price' : df4,
            'score' : df1,
            'specs' :df5
        }
        if top_num != 0:
            dict = {
            'name' : df2[:top_num],
            'price' : df1[:top_num],
            'score' : df4[:top_num],
            'specs' :df5[:top_num]
        }
         
        return dict

def ROBO(text):
    stp = removeStopWords(text)
    tag= pos_tag(stp)
    tkk = word_tokenize(text)
    product = chatBot(tag,tkk)
    product = pd.DataFrame(product)
    product.to_csv("data.csv")



        

