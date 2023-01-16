import string

stroka = input()
dic = {'T': 'A', 'A': 'T', 'C': 'G', 'G': 'C'}
#1
stroka = ''.join(map(lambda x: dic.get(x), stroka))
#2
stroka = ''.join([dic[x] for x in stroka])
#3 (without dictionary)
stroka.translate(string.maketrans("ATCG","TAGC"))
print(stroka)