#INOKrypt - https://github.com/TheThingsPlanet/INOKrypt
#Version 0.1 - Prototype Edition
#Developed by Shobhit Sharma (github.com/ScriptKKiddie) | (twitter.com/ScriptKKiddie)
#Write Us @ shobhit@technical0812.com

#THIS IS A TESTING PROGRAM - How INOKrypt Add An Extra Line of Security for your IoT Data?

from INOKrypt import INOKrypt    #Importing INOKrypt Main Package
import random
import time


#Creating Virtual Sensor for Testing Data
class IoTData:
    virtualSensor = {'Device ID':'218000',  #Static Unique Numerical ID of IoT Device
                     'Device IP':'192.168.34.23',    #IP Address of the Device [CLIENT'S IP]
                     'Server IP':'192.168.34.77',   #IP Address of the Server [SERVER'S IP]
                     'tempData':'',
                     'humData':'',
                     }


#CLIENT-SIDE OPERATIONS

#Getting Sensors Data

print("Initializing Device")
time.sleep(1)
print("Connecting")
time.sleep(1)
print("Device "+IoTData.virtualSensor['Device ID']+" is connected at "+IoTData.virtualSensor['Device IP'])
time.sleep(2)
print("Getting Data from Sensors")

temp = random.randint(25, 48)           #Generating Dummy Data for Temperature
hum = random.randint(12, 62)            #Generating Dummy Data for Humidity
print("Temperature is ",temp)
print("Humidity is ",hum)


# ---> Securing IoT Data Here [ INOKrypt.Algo.encode(LEVEL, DATA) ] Where 'LEVEL' is 1 (only 1 available in version 0.1) & 'DATA' can be any integer value

prepTemp = str(temp)+IoTData.virtualSensor['Device ID']
prepHum = str(hum)+IoTData.virtualSensor['Device ID']

print(prepTemp)
print(prepHum)


enTemp = INOKrypt.Algo.encode(1, prepTemp)          #where prepTemp is prepared Temperature sensor Data
enHum = INOKrypt.Algo.encode(1, prepHum)            #where prepHum is prepared Humidity sensor Data
enDeviceID = INOKrypt.Algo.encode(1,int(IoTData.virtualSensor['Device ID']))

# Verifying Encrypted Data
print("\n")
print("---Before INOKrypt Encoding---")
print("Temperature is: "+enTemp)
print("Humidity is: "+enHum)
time.sleep(1)
print("---After INOKrypt Encoding---")
print("ENCRYPTED Temperature is: "+enTemp)
print("ENCRYPTED Humidity is: "+enHum)

#Sending Data To Server

print("\n")
print(IoTData.virtualSensor['Server IP']+"/IoTData?deviceID="+enDeviceID+"&temp="+enTemp+"&hum="+enHum)         #This is for testing : The API will be "http://[SERVER IP]/IoTData?deviceID=DEVICE_ID&temp=TEMPERATURE&hum=HUMIDITY
time.sleep(2)


#SERVER-SIDE OPERATIONS

#Storing Data in IoT Server's Database

print("\n")
print("Receiving Data from "+IoTData.virtualSensor['Device IP'])
#print("Device ID: "+IoTData.virtualSensor['Device ID'])
print("\n")
time.sleep(1)
print("Received Incoming Data: Device ID:"+enDeviceID)

print("Received Incoming Data: Temperature Sensor's Data:"+enTemp)
print("Received Incoming Data: Humidity Sensor's Data:"+enHum)

# ---> Decoding Data here at Server Side [ INOKrypt.Algo.encode(LEVEL, DATA ] Where 'LEVEL' is 1 (REMEMBER THIS) (only 1 available in version 0.1) & 'DATA' is encoded Incoming Data

decDeviceID = str(INOKrypt.Algo.decode(1,enDeviceID))
decTemp = str(INOKrypt.Algo.decode(1,enTemp))
decHum = str(INOKrypt.Algo.decode(1,enHum))

print("\n")
print("-------------- IoT Data MySQL Table --------------")
print("--------------------------------------------------")
print("S.No. | Device ID |    Device IP    | Temp | Hum ")
print("  1.  | "+decDeviceID+"    | "+IoTData.virtualSensor['Device IP']+"   | "+decTemp[0]+decTemp[1]+"   |   "+decHum[0]+decHum[1])
print("--------------------------------------------------")

print("\n")

time.sleep(1)

print("Read The Documentation Here: https://inokrypt.readthedocs.io/en/latest/")
