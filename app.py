import serial
import pymysql

ser = serial.Serial('/dev/ttyUSB0', 115200)

db = pymysql.connect(
        host='flaskapp.cr8ct5qe5uwv.us-east-2.rds.amazonaws.com',
        port=3306,
        user='root',
        password='root1234',
        db='flaskapp',
        )

if(db):
    print(db)

while(True):
    value = str(ser.readline())[2:-5]
    print(value)
   
    try:
        with db.cursor() as cursor:
            query = "insert into Readings values (NOW(),'"+value[0:5]+"', '"+value[6:9]+"', '"+value[10:]+"')"
            result = cursor.execute(query)
            print(result)
            db.commit()
    except Exception as e:
        print(e) 