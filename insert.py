import  pymysql.cursors
import csv

def insertToMySQL():
    try:
        mysqlconnection=pymysql.connect(host='localhost',
                         user='root',
                         password='root',db='moco_db',
                                cursorclass=pymysql.cursors.DictCursor)
    
        if mysqlconnection.open:
            print("OK")
            db_info=mysqlconnection.get_server_info()
            print(db_info)
            cursor=mysqlconnection.cursor()
        
        with open("user.csv") as csvfile:
            sp=csv.DictReader(csvfile)
            print(sp)
            for row in sp:
                print(row)
                print(row['id'], row['name'], row['district'],row['province'])
                sql='INSERT INTO municipality(id,name,district,province) VALUES(%s, %s,%s, %s)'
                val=(row['id'], row['name'], row['district'],row['province'])
                cursor.execute(sql,val)
                print(cursor.rowcount, "record inserted.")
                print ("Done")
        #close the connection to the database.
        cursor.close()
        mysqlconnection.close()
        mysqlconnection.commit()
    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)    
    
