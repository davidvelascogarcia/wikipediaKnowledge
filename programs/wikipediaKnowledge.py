'''
 * ************************************************************
 *      Program: Wikipedia Knowledge
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
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

print("")
print("Loading Wikipedia Knowledge engine ...")
print("")

print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network ...")
print("")

# Init YARP Network
yarp.Network.init()

print("")
print("[INFO] Opening data input port with name /wikipediaKnowledge/data:i ...")
print("")

# Open wikipediaKnowledge input data port
wikipediaKnowledge_inputPort = yarp.Port()
wikipediaKnowledge_inputPortName = '/wikipediaKnowledge/data:i'
wikipediaKnowledge_inputPort.open(wikipediaKnowledge_inputPortName)

# Create wikipediaKnowledge input data bottle
wikipediaKnowledgeInputBottle = yarp.Bottle()

print("")
print("[INFO] Opening data output port with name /wikipediaKnowledge/data:o ...")
print("")

# Open wikipediaKnowledge output data port
wikipediaKnowledge_outputPort = yarp.Port()
wikipediaKnowledge_outputPortName = '/wikipediaKnowledge/data:o'
wikipediaKnowledge_outputPort.open(wikipediaKnowledge_outputPortName)

# Create wikipediaKnowledge output data bottle
wikipediaKnowledgeOutputBottle = yarp.Bottle()

print("")
print("Initializing wikipediaKnowledge engine ...")
print("")

# Get system configuration
print("")
print("Detecting system and release version ...")
print("")
systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

print("")
print("**************************************************************************")
print("Wikipedia client:")
print("**************************************************************************")
print("")
print("Configuring Wikipedia client ...")
print("")

clientPossibleResults = "null"
clientTitleResults = "null"
clientURLResults = "null"
clientContentResults = "null"

print("")
print("[INFO] Client configuration done at " + str(datetime.datetime.now()) + ".")
print("")

# Variable to control loopControlDataRequest
loopControlDataRequest = 0

while int(loopControlDataRequest) == 0:

    # Waiting to input data
    print("")
    print("**************************************************************************")
    print("Waiting for input data request:")
    print("**************************************************************************")
    print("")
    print("[INFO] Waiting for input data request ...")
    print("")

    # Read request and clean
    wikipediaKnowledge_inputPort.read(wikipediaKnowledgeInputBottle)
    dataToResolve = wikipediaKnowledgeInputBottle.toString()
    dataToResolve = dataToResolve.replace('"','')

    print("")
    print("[RECEIVED] Data received: " + str(dataToResolve) + " at " + str(datetime.datetime.now()) + ".")
    print("")

    print("")
    print("**************************************************************************")
    print("Processing:")
    print("**************************************************************************")
    print("")

    try:
        # Sending request to Wikipedia
        print("")
        print("[INFO] Connecting with Wikipedia server ...")
        print("")

        print("")
        print("Searching possible results ...")
        print("")

        # Seek server response
        clientPossibleResults = wikipedia.search(str(dataToResolve))

        print("")
        print("[INFO] Results founded.")
        print("")


        print("")
        print("Searching specific results ...")
        print("")

        # If specific results founded
        try:
            serverRespone = wikipedia.page(str(dataToResolve))
            clientURLResults = serverRespone.url
            clientTitleResults = serverRespone.title
            clientContentResults = serverRespone.content

            print("")
            print("[INFO] Specific results founded ...")
            print("")

        except:
            print("")
            print("[ERROR] Sorry i couldn´t find specific results, only possible ...")
            print("")

        print("")
        print("[INFO] Server response done at " + str(datetime.datetime.now()) + ".")
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

    # If server request error
    except:
        print("")
        print("[ERROR] Sorry, i could´t resolve your request.")


    # Send wikipediaKnowledge output results
    wikipediaKnowledgeOutputBottle.clear()
    wikipediaKnowledgeOutputBottle.addString("RESULTS:")
    wikipediaKnowledgeOutputBottle.addString("Possible results:")
    wikipediaKnowledgeOutputBottle.addString(str(clientPossibleResults))
    wikipediaKnowledgeOutputBottle.addString("URL results:")
    wikipediaKnowledgeOutputBottle.addString(str(clientURLResults))
    wikipediaKnowledgeOutputBottle.addString("Title results:")
    wikipediaKnowledgeOutputBottle.addString(str(clientTitleResults))
    wikipediaKnowledgeOutputBottle.addString("Content results:")
    wikipediaKnowledgeOutputBottle.addString(str(clientContentResults))
    wikipediaKnowledge_outputPort.write(wikipediaKnowledgeOutputBottle)

# Close YARP ports
print("[INFO] Closing YARP ports ...")
wikipediaKnowledge_inputPort.close()
wikipediaKnowledge_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
print("")
print("wikipediaKnowledge finished correctly.")
print("")
