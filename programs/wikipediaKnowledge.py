'''
 * ************************************************************
 *      Program: Wikipedia Knowledge
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 */

/*
  *
  * | INPUT PORT                           | CONTENT                                                 |
  * |--------------------------------------|---------------------------------------------------------|
  * | /wikipediaKnowledge/data:i           | Input data text to get information                      |
  *
  * | OUTPUT PORT                          | CONTENT                                                 |
  * |--------------------------------------|---------------------------------------------------------|
  * | /wikipediaKnowledge/data:o           | Output text result                                      |
  *
'''

# Libraries
import datetime
import os
import platform
import wikipedia
import yarp


print("**************************************************************************")
print("**************************************************************************")
print("                     Program: Wikipedia Knowledge                         ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system ...")

print("")
print("Loading Wikipedia Knowledge engine ...")

print("")
print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network ...")

# Init YARP Network
yarp.Network.init()


print("")
print("[INFO] Opening data input port with name /wikipediaKnowledge/data:i ...")

# Open input data port
wikipediaKnowledge_inputPort = yarp.Port()
wikipediaKnowledge_inputPortName = '/wikipediaKnowledge/data:i'
wikipediaKnowledge_inputPort.open(wikipediaKnowledge_inputPortName)

# Create input data bottle
inputBottle=yarp.Bottle()

print("")
print("[INFO] Opening data output port with name /wikipediaKnowledge/data:o ...")

# Open output data port
wikipediaKnowledge_outputPort = yarp.Port()
wikipediaKnowledge_outputPortName = '/wikipediaKnowledge/data:o'
wikipediaKnowledge_outputPort.open(wikipediaKnowledge_outputPortName)

# Create output data bottle
outputBottle=yarp.Bottle()


print("")
print("Initializing wikipediaKnowledge engine ...")

# Get system configuration
print("")
print("Detecting system and release version ...")
systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)


print("")
print("")
print("**************************************************************************")
print("Wikipedia client:")
print("**************************************************************************")
print("")
print("Configuring Wikipedia client ...")

clientPossibleResults ="null"
clientTitleResults = "null"
clientURLResults = "null"
clientContentResults = "null"

print("[INFO] Client configuration done.")


while True:

    # Waiting to input data
    print("")
    print("Waiting for input data ...")

    wikipediaKnowledge_inputPort.read(inputBottle)
    dataToResolve = inputBottle.toString()
    dataToResolve = dataToResolve.replace('"','')

    print("[RECEIVED] Data received: "+str(dataToResolve))

    print("")
    print("")
    print("**************************************************************************")
    print("Processing:")
    print("**************************************************************************")

    try:
        # Sending request to Wikipedia
        print("")
        print("Connecting with Wikipedia server ...")

        print("")
        print("Searching possible results ...")

        clientPossibleResults = wikipedia.search(str(dataToResolve))
        print("")
        print("[INFO] Results founded.")


        print("")
        print("Searching specific results ...")

        try:
            serverRespone = wikipedia.page(str(dataToResolve))
            clientURLResults = serverRespone.url
            clientTitleResults = serverRespone.title
            clientContentResults = serverRespone.content
            print("")
            print("[INFO] Specific results founded ...")

        except:
            print("")
            print("[ERROR] Sorry i couldn´t find specific results, only possible ...")



        print("")
        print("[INFO] Server response done.")

        print("")
        print("")
        print("**************************************************************************")
        print("Results:")
        print("**************************************************************************")
        print("")
        print("[INFO] Possible results: "+ str(clientPossibleResults))
        print("")
        print("[INFO] URL results: "+ str(clientURLResults))
        print("")
        print("[INFO] Title results: "+ str(clientTitleResults))
        print("")
        print("[INFO] Content results: "+ str(clientContentResults))
    except:
        print("")
        print("[ERROR] Sorry, i could´t resolve your request.")


    # Send output results
    outputBottle.clear()
    outputBottle.addString("RESULTS:")
    outputBottle.addString("Possible results:")
    outputBottle.addString(str(clientPossibleResults))
    outputBottle.addString("URL results:")
    outputBottle.addString(str(clientURLResults))
    outputBottle.addString("Title results:")
    outputBottle.addString(str(clientTitleResults))
    outputBottle.addString("Content results:")
    outputBottle.addString(str(clientContentResults))

    wikipediaKnowledge_outputPort.write(outputBottle)

# Close YARP ports
print("Closing YARP ports ...")
wikipediaKnowledge_inputPort.close()
wikipediaKnowledge_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
