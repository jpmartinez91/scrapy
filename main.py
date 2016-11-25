from bs4 import BeautifulSoup
import requests
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')
url = "https://------------->>"
baseUrl = "https://------------->>"

def join_word (arg):
    line = ''
    for ikm, pasa in enumerate(arg):
        if pasa.strip() != "":
            line = line + pasa.strip()
    return line

def descomponer_pagina(html):
    data = html.find_all('div', {'class':'hitlistmaterial_tableless'})
    for i, texto in enumerate(data):
        title=''
        try:
            title = texto.find('tag', {'id/class':'name-tag'}).getText().strip()            
        except Exception as e:
            pass        
        newRes = requests.get(baseUrl+link)
        if newRes.status_code == 200:
            try:
                detailMaterial = BeautifulSoup(newRes.text, "html.parser")
                headerMaterial = detailMaterial.find_all('div',{'material_tile_body'})
            except AttributeError:
                pass
            for k, header in enumerate(headerMaterial):
                try:
                    variable = join_word(header.find('tag', {'id/class': 'name-tag'}).getText().splitlines()).split(':')[1]                    
                except AttributeError:
                    pass           
            query = "INSERT INTO table () VALUES ();
            cursor.execute(query)
            dbConnect.commit()                
    newPage = html.find('a', {'name-tag':'next page'}).get('href')
    get_body_html(baseUrl+newPage)

def get_body_html(arg):
        res = requests.get(arg)
        if res.status_code == 200:
            body = BeautifulSoup(res.text, "html.parser")
            descomponer_pagina(body)
        else:
            print "NO CONNECTED"

DB_HOST = 'host'
DB_USER = 'user'
DB_PASS = 'pwd'
DB_NAME = 'MERLOT'
datosDB = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
dbConnect = MySQLdb.connect(*datosDB)
cursor = dbConnect.cursor()
get_body_html(url)
