# engine = create_engine('mysql+pymysql://root:mM.1aA2aA3zZ4$@localhost/PAI')
#     df2 = pd.read_sql("SELECT * FROM data_1", con=engine)
#     df2 = list(df2['name'])
#     l = List()
#     str1 = ''
#     if len(num) == 1 and l[num[0]][0] == 'about':
#         result = ''
#         for i in tag:
#             if i[0] in df2:
#                 str1 = i[0]
#         brand = list(pd.read_sql("SELECT brand FROM data_1 WHERE name = %s" , con=engine , params=(str1,))['brand'])[0]
#         specs = list(pd.read_sql("SELECT specs FROM data_1 WHERE name = %s" , con=engine , params=(str1,))['specs'])[0]
#         score = list(pd.read_sql("SELECT score FROM data_1 WHERE name = %s" , con=engine , params=(str1,))['score'])[0]
#         num_of = list(pd.read_sql("SELECT num_of_rev FROM data_1 WHERE name = %s" , con=engine , params=(str1,))['num_of_rev'])[0]
#         price = list(pd.read_sql("SELECT price FROM data_1 WHERE name = %s" , con=engine , params=(str1,))['price'])[0]
#         result = 'ROBO : The discription of '+ str1 + " is brand " + brand +", have price Rs. "+str(price)+ ", having specs " + specs + ", score " + str(score)  + ", and number of reviews " + str(num_of)   

#     elif len(num) == 1 and num[0] == 5:
#         result = ''
#         flg = False
#         for i in tag:
#             if "CD" in i:
#                 num1 = int(i[0])
#                 flg = True
#         if flg == False:
#             num1 = 1
#         brand = list(pd.read_sql("SELECT brand FROM data_1", con=engine)['brand'])[:num1]
#         specs = list(pd.read_sql("SELECT specs FROM data_1", con=engine)['specs'])[:num1]
#         score = list(pd.read_sql("SELECT score FROM data_1", con=engine)['score'])[:num1]
#         num_of = list(pd.read_sql("SELECT num_of_rev FROM data_1", con=engine)['num_of_rev'])[:num1]
#         price = list(pd.read_sql("SELECT price FROM data_1", con=engine)['price'])[:num1]
#         result = []
#         for k in range(num1):
#             result.append("brand " + brand[k] +", have price Rs. "+str(price[k])+  ", having specs " + specs[k] + ", score " + str(score[k])  + ", and number of reviews " + str(num_of[k]))
#         result = "ROBO : The discription of Top "+ str(num1)+ " is " + str(' '.join(result))
#         result = result.replace('[','').replace("]",'')

#     elif len(num) == 1:
#         result = ''
#         str1 = ''
#         for i in tag:
#             if i[0] in df2:
#                 str1 = i[0]
#         result = list(pd.read_sql("SELECT {} FROM data_1 WHERE name = %s".format(l[num[0]][0]) , con=engine , params=(str1,))[l[num[0]][0]])[0]
#         if isinstance(result, float):
#             result = str(result)
#         result = "ROBO : The " + l[num[0]][0] + " of " + str1 + " is " + result
        
    
#     return result

