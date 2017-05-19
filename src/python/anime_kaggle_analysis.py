# -*- coding: utf-8 -*-
"""

@author: Vijay Penumarti <pvjdev@gmail.com>
"""

import pymysql #Package that connects to mysql db
import requests #Package that handles HTTP requests
import os #Import for the clear command
import json #Handle JSONs in Python

#clear console by using clear()
clear = lambda: os.system('cls')

#the config object
config = json.load(open('development/local.json'))

#DB Config Credentials
DB_CONFIG = config["MYSQL_DB_CONNECTOR"]

# Connect to the database

connection = pymysql.connect(
    host = DB_CONFIG['host'],
    user = DB_CONFIG['user'],
    password = DB_CONFIG['password'],
    db = DB_CONFIG['db'],
    charset = DB_CONFIG['charset'],
    cursorclass = pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Select Records
        query = "select * from `aa_anime_details_list`"
        cursor.execute(query)

    # Connection is not autocommit by default. Commit to save our changes
    connection.commit()
    result = cursor.fetchall()
    genres = []
    split_genre = ''
    for element in result:
        genres.append(element['genre'])
    print(genres)
finally:
    connection.close()
