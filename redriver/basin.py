from bs4 import BeautifulSoup
import requests
import mysql.connector

source = requests.get('https://waterdatafortexas.org/reservoirs/basin/red?fbclid=IwAR24ZFIUeFDYBBVOULRp8i3VDst1YJnvKYhU4NPLr0krIpkyYyV6UPBw89g').text
soup = BeautifulSoup(source, 'lxml')

# connect to mySQL db
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="", # enter your password
  # create database on mysql and connect  
  database = "redriver" 
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS basin")
mycursor.execute("CREATE TABLE `redriver`.basin ( `id` INT NOT NULL AUTO_INCREMENT, `occu` TEXT NOT NULL , `date` DATE NOT NULL , `full_per` FLOAT NOT NULL , `res_sto` INT(255) NOT NULL , `con_sto` INT(255) NOT NULL , `con_cap` INT(255) NOT NULL , PRIMARY KEY (`id`) ) ENGINE = InnoDB;")

# table 1
div = soup.find('div' , class_ = 'col-md-6' )
table = div.find('table', class_= 'table table-striped table-bordered table-condensed')
table_body = table.find('tbody')
rows = table_body.find_all('tr')
  
for row in rows:
  cols = row.find_all('td')
  col_1 = cols[0].text.strip()
  col_2 = cols[1].text.strip()
  col_3 = cols[2].text.strip()
  col_4 = cols[3].text.strip()
  col_5 = cols[4].text.strip()
  col_6 = cols[5].text.strip()

  #print(col_1, col_2, col_3, col_4, col_5,col_6)

  sql = ("""INSERT INTO basin(
            occu, date, full_per,
            res_sto, con_sto, con_cap ) 
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""").format(col_1, col_2, col_3, col_4, col_5, col_6)
  mycursor.execute(sql)
  mydb.commit()

mycursor.close()
mydb.close()
  