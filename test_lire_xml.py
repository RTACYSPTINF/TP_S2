from lxml import etree
import os

os.chdir("H:\Doc_jspit\Travail-2010-2011\cours-TD-TP_JP\cours\Algo-RT1-Python\python_avance_S2\deputes")

tree = etree.parse("nosdeputes.fr_deputes_en_mandat_2019-03-14.xml")


for j in tree.xpath("/deputes/depute/nom/nom_de_famille"):
    print(j.text)




"""
for user in tree.xpath("H:\Doc_jspit\Travail-2010-2011\cours-TD-TP_JP\cours\Algo-RT1-Python\python_avance_S2\deputes"):
    print(user.text)
"""

with open("nosdeputes.fr_deputes_en_mandat_2019-03-14.xml",'r',encoding='utf-8') as f:
    a=f.readlines()
    
""""    
tree = etree.parse("voitures.xml")
for voiture in tree.xpath("/depute/nom/"):
    print "({}) : {}".format(voiture.xpath("marque")[0].text, voiture.xpath("nom")[0].text)
"""

tree = etree.parse("test.xml")
for user in tree.xpath("/users/user/nom"):
    print(user.text)
    
import json

with open('nosdeputes.fr_deputes_en_mandat_2019-03-14.json') as json_data:
    data_dict = json.load(json_data)

data_str = json.dumps(data_dict)
print(data_str)




