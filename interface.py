#! /usr/bin/python3

#from flask import Flask

from users import userlist
from flask import Flask, request, render_template , session
from influxdb import InfluxDBClient
import time
import json
import random
import logging
import os 
import string
import template as appHtml
import devices as  registeredDevices
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


@app.route('/ListUsers', methods=["GET"])
def ListUsers():
    htmlBuffer = "<!DOCTYPE html> <html> <head> <style> " 
    htmlBuffer = htmlBuffer + "table { width:30%; }"
    htmlBuffer = htmlBuffer + "table, th, td {"
    htmlBuffer = htmlBuffer + "border: 1px solid black;"
    htmlBuffer = htmlBuffer + "border-collapse: collapse; } th, td { padding: 15px; text-align: left; }"
    htmlBuffer = htmlBuffer + "table#t01 tr:nth-child(even) { background-color: #eee; } "
    htmlBuffer = htmlBuffer + "table#t01 tr:nth-child(odd) { background-color: #fff; }"
    htmlBuffer = htmlBuffer + "table#t01 th { background-color: black; color: white; }" 
    htmlBuffer = htmlBuffer + "</style> </head>"
    htmlBuffer = htmlBuffer + "<CENTER>"
    htmlBuffer = htmlBuffer + "<H1> User List </H1>"
    htmlBuffer = htmlBuffer +  "<TABLE id=\"t01\">"
    htmlBuffer = htmlBuffer +  "<tr> <th>No </th> <th>User ID </th> <th>Name</th> </tr>"
    buffer = "" 
    count = 1
    for row in userlist:
       count = count+1
    htmlBuffer = htmlBuffer + "</TABLE> </CENTER></HTML>"
    return  htmlBuffer

#-----
def GenerateDeviceListPage():
    page = appHtml.partOne
    # replace uSerNaMe with role
    role = session['role']
    editablePartTwo = appHtml.partTwo

    editablePartTwo = editablePartTwo.replace('uSeRnAmE' ,role)
    page = page + editablePartTwo

    # This is where we need to fill in the main part
    mainPart = "" 
    mainPart =  '<div class=\"main\"> \
                   <h2>Device Management </h2> \
                        <body> \
                            <table id=\"t01\">\
                               <tr> \
                               <th>No</th>\
                               <th>Name</th>\
                               <th>Device ID</th> \
                               <th>Description</th> \
                             </tr>'
    count = 1
    row = ""
    for device in registeredDevices.devicelist:
        row =        "<TR> <TD>" +str(count) + "</TD>"
        row = row +  "<TD>" + device[0] + "</TD>" 
        row = row +  "<TD>" + device[1] + "</TD>"
        row = row +  "<TD>" + device[2] + "</TD> <TR>"
        mainPart = mainPart + row 
        row = ""
        count = count + 1
    mainPart = mainPart + "</TABLE> </BODY> </DIV>" 

    page = page + mainPart
    # End of generating main content

    page = page + appHtml.partThree
    return page

#------

@app.route('/devices', methods=["GET"])
def DeviceManagement():
   html  = GenerateDeviceListPage()
   return html
   #return "<HTML> <H1> device Homepage  </H1> </HTML" 
   #return render_template("devices.html")  

@app.route('/analytics', methods=["GET"])
def Analytics():
   return render_template("analytics.html")  


@app.route('/dashboards', methods=["GET"])
def Dashboard():
   return render_template("dashboard.html")  
def GenerateFrontPage():
    page = appHtml.partOne 
    # replace uSerNaMe with role
    role = session['role']
    editablePartTwo = appHtml.partTwo

    editablePartTwo = editablePartTwo.replace('uSeRnAmE' ,role)
    page = page + editablePartTwo 
    
    # This is where we need to fill in the main part
    mainPart = '<div class="main">\
                    <h2>Open View  IoT </h2>\
                    <body>\
                          <img src="http://platform.i2otlabs.com/Front_page.jpg">\
                    </body>\
               </div>'
    page = page + mainPart
    # End of generating main content 

    page = page + appHtml.partThree
    return page
@app.route('/login', methods=["POST"])
def HandleLogin():
  retHtml = "" 
  loginname = request.form['fname']
  password = request.form['lname']
  success, role = ValidateUser(loginname,password)
  if success:
     session['login'] = loginname 
     session['role'] =  role
     session['status'] = "1" 
     retHtml   = GenerateFrontPage()
     #retHtml   = "frontpage.html"
  else:
     retHtml = "<HTML> autherror.html </HTML>"
  
  return retHtml
     
@app.route('/logout', methods=["GET"])
def HandleLogout():
    if  'login' in session:
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
