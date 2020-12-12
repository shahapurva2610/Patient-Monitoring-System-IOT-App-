from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
	con = pymysql.connect(
		host='readings.cr8ct5qe5uwv.us-east-2.rds.amazonaws.com',
		port=3306,
		user='admin',
		password='adminadmin',
		db='readings',
		)
	cur = con.cursor()
	resultValue = cur.execute("select * from READINGS")

	if resultValue > 0:
		sensorDetails = cur.fetchall()
		d11x = []
		d12x = []
		d21x = []
		d22x = []
		d31x = []
		d32x = []
		cnt1 = 0
		cnt2 = 0
		cnt3 = 0
		for sensor in sensorDetails:
			if(sensor[1] == "Room 1"):
				cnt1 = cnt1 + 1
				d11x.append(cnt1)
				d12x.append(sensor[3])

			if(sensor[1] == "Room 2"):
				cnt2 = cnt2 + 1
				d21x.append(cnt2)
				d22x.append(sensor[3])


			if(sensor[1] == "Room 3"):
				cnt3 = cnt3 + 1
				d31x.append(cnt3)
				d32x.append(sensor[3])


		print(cnt1)
		print(cnt2)
		print(cnt3)

		print(d11x)
		print(d21x)
		print(d31x)

		print(d12x)
		print(d22x)
		print(d32x)

		return render_template('index.html', data=sensorDetails, d11=d11x, d12=d12x,d21=d21x,d22=d22x,d31=d31x,d32=d32x)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5001)
