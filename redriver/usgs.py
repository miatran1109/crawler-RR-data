from bs4 import BeautifulSoup
import requests
import mysql.connector

source = requests.get('https://waterdata.usgs.gov/nwis/uv?cb_00010=on&cb_00060=on&cb_00065=on&cb_00095=on&cb_00300=on&cb_00400=on&cb_63680=on&format=html&site_no=05054000&period=&begin_date=2020-11-21&end_date=2020-11-28').text
soup = BeautifulSoup(source, 'lxml')

# connect to mySQL db
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mtn1910", # enter your password
  # create database on mysql and connect  
  database = "redriver" 
)

mycursor = mydb.cursor()

# or create database
# mycursor.execute("CREATE DATABASE redriver")

# create table
mycursor.execute("DROP TABLE IF EXISTS usgs")
mycursor.execute("CREATE TABLE usgs(id INT PRIMARY KEY AUTO_INCREMENT ,date_time VARCHAR(100), discharge_ft3_per_s VARCHAR(100), disolved_oxygen_mg_per_L VARCHAR(100),  gege_height_feet VARCHAR(100), temperature_water_degC VARCHAR(100), specific_conductance_unfus_per_cm_at_25degC VARCHAR(100), pH_water_unfltr_field_std_units VARCHAR(100), turbidity_ir_led_light_det_ang_90_deg VARCHAR(100))")
# just to check 
# mycursor.execute("DESCRIBE usgs")
# for x in mycursor:
#     print(x)

# find table stored data
table = soup.find('table', class_='tablesorter')
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
    col_7 = cols[6].text.strip()
    col_8 = cols[7].text.strip()
    
    # cols = [ele.text.strip() for ele in cols]
    # data.append([ele for ele in cols if ele])
    
    # print column 
    #print(col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8)
   
    # insert crawled data to table
    value = (col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8)
    sql = ("INSERT INTO usgs(date_time, discharge_ft3_per_s, disolved_oxygen_mg_per_L, gege_height_feet, temperature_water_degC, specific_conductance_unfus_per_cm_at_25degC, pH_water_unfltr_field_std_units, turbidity_ir_led_light_det_ang_90_deg) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')").format(*col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8)
    mycursor.execute(sql)

    

