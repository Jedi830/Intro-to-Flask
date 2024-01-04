import pymysql
import pymysql.cursors

connection = pymysql.connect(
    database = "world",
    user = "jdelacruz",
    password = "229770375",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor,
)

cursor = connection.cursor()

cursor.execute("SELECT `Name`,`Population`, `HeadOfState` FROM `country` ")

results = cursor.fetchall() 

from pprint import pprint as print

print(results[0]["HeadOfState"])

for x in results:
    print(x['HeadOfState'])
