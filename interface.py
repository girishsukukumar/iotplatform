#! /usr/bin/python3

#from flask import Flask
#@app.route("/")
#def hello():
#    return "Hello world!"

from users import userlist
from flask import Flask, request, render_template , session
from influxdb import InfluxDBClient
import time
import json
import random
import logging
import os 
INFLUX_PORT = 8086
INFLUX_HOSTNAME =  'localhost'
INFLUX_USERNAME = 'girish'
INFLUX_PASSWORD = 'gks3050'
INFLUX_DATABASE = 'defaultdb'


app = Flask(__name__,static_url_path='/static')
app.secret_key = '23333333'

def ValidateUser(user, passwd) :
    retval = False
    role = "Invalid"
    for row in userlist:
        login = row[0]
        password =  row[1]
        if user == login:
           if passwd == password:
              retval = True
              role  = row[2]
              break
    return retval,role
 
@app.route('/')
def home():
  return render_template("sensor.html")



@app.route('/devices', methods=["GET"])
def DeviceManagement():
#   return "<HTML> <H1> device Homepage  </H1> </HTML" 
   return render_template("devices.html")  

@app.route('/analytics', methods=["GET"])
def Analytics():
   return render_template("analytics.html")  


@app.route('/dashboards', methods=["GET"])
def Dashboard():
   return render_template("dashboard.html")  

@app.route('/login', methods=["POST"])
def HandleLogin():
  loginname = request.form['fname']
  password = request.form['lname']
  success, role = ValidateUser(loginname,password)
  if success:
     session['login'] = loginname 
     session['role'] =  role
     retHtml   = "frontpage.html"
  else:
     retHtml = "autherror.html"
  
  return render_template(retHtml)
     
@app.route('/logout', methods=["GET"])
def HandleLogout():
    session.pop('login', None)
    return render_template("logout.html")
   
@app.route('/event', methods=["POST"])
def HandleEventPost():
   returnString  = "No data"
   action = request.form['Action']
   data = request.form['data']
   INFLUX_HANDLE =  InfluxDBClient(host= INFLUX_HOSTNAME,
                        port=INFLUX_PORT,
                        username=INFLUX_USERNAME,
                        password=INFLUX_PASSWORD,
                        ssl=False,
                        verify_ssl=False)

   #print(INFLUX_HANDLE)
   INFLUX_HANDLE.switch_database('defaultdb')

   if action == 'Event':
     writeData = [] 
     jsonStr = data 
     # Check for Json data valdity 
     jsonStr  = jsonStr.replace("\'", "\"")
     jsonDict= json.loads(jsonStr)

     writeData.append( jsonDict)
     #print(writeData)

     milli_sec1 = int(round(time.time() * 1000))
     INFLUX_HANDLE.write_points(writeData)
     result =  "Sucess"
   else:
     result = "Not implemented" 
   milli_sec2 = int(round(time.time() * 1000))
   diff = milli_sec2 - milli_sec1 
   msg  = str(diff)  
   returnString = "<HTML> <H1>" + "Action=" + str(action) + "   data="+ str(data) + "</H1> "  + " " + msg + "  " + result  +  "</HTML>" 
   return returnString  

@app.route('/speed', methods=["POST"])
def sendspeed():
   return "<HTML> <H1> Speed Post </H1> </HTML" 

if __name__ == "__main__":
    app.run()
