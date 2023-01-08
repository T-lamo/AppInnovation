import time
import csv
from naoqi import ALProxy
import pandas as pd

# Source : http://doc.aldebaran.com/2-1/naoqi/peopleperception/alfacedetection-tuto.html

IP = "192.168.13.88"
PORT = 9559

# Create a proxy to ALFaceDetection
faceProxy = ALProxy("ALFaceDetection", IP, PORT)
tts = ALProxy("ALTextToSpeech", IP, PORT)

# Subscribe to the ALFaceDetection proxy
# This means that the module will write in ALMemory with
# the given period below
period = 500
faceProxy.subscribe("Test_Face", period, 0.0 )

# ALMemory variable where the ALFaceDetection module
# outputs its results.
memValue = "FaceDetected"

# Create a proxy to ALMemory
memoryProxy = ALProxy("ALMemory", IP, PORT)


# A simple loop that reads the memValue and checks whether faces are detected.
for i in range(0, 20):
  time.sleep(0.5)
  val = memoryProxy.getData(memValue, 0)


# Check whether we got a valid output: a list with two fields.
if(val and isinstance(val, list) ):
    # We detected faces !
    # For each face, we can read its shape info and ID.
    # First Field = TimeStamp.
    timeStamp = val[0]
    # Second Field = array of face_Info's.
    faceInfoArray = val[1]

  
    # Browse the faceInfoArray to get info on each detected face.
    for faceInfo in faceInfoArray:
        # First Field = Shape info.
        faceShapeInfo = faceInfo[0]
        # Second Field = Extra info (empty for now).
        faceExtraInfo = faceInfo[1]
        print ("  alpha %.3f - beta %.3f" % (faceShapeInfo[1], faceShapeInfo[2]))
        print ("  width %.3f - height %.3f" % (faceShapeInfo[3], faceShapeInfo[4]))

        print("faceId : ", faceExtraInfo[0])
        print("score reco : ", faceExtraInfo[1])
        print("face label : ", faceExtraInfo[2])
        print("left eye point : ", faceExtraInfo[3])
        print("right eye point : ", faceExtraInfo[4])
        print("nose point : ", faceExtraInfo[7])
        print("mouth point : ", faceExtraInfo[8])

        # Define the structure of the data
        student_header = ['leftEyePoint1','leftEyePoint2','leftEyePoint3','leftEyePoint4','leftEyePoint5','leftEyePoint6'
        ,'rightEyePoint1','rightEyePoint2','rightEyePoint3','rightEyePoint4','rightEyePoint5','rightEyePoint6'
        , 'nosePoint1','nosePoint2','nosePoint3','nosePoint4','nosePoint5','nosePoint6'
        , 'mouthPoint1','mouthPoint2','mouthPoint3','mouthPoint4','mouthPoint5','mouthPoint6','numEtudiant']
        student_data = []
        id = 0

        for idx,category in enumerate(faceExtraInfo[3]) :
            if(idx < 6):
                print(category)
                student_data.append(category)
        for idx,category in enumerate(faceExtraInfo[4]) :
            if(idx < 6):
                print(category)
                student_data.append(category)
        for idx,category in enumerate(faceExtraInfo[7]) :
            if(idx < 6):
                print(category)
                student_data.append(category)
        for idx,category in enumerate(faceExtraInfo[8]) :
            if(idx < 6):
                print(category)
                student_data.append(category)
        
        student_data.append("1")
        print(student_data)
        # df = pd.read_csv('studentsFaces.csv')
        # df = df.append(student_data)
        df = pd.DataFrame(student_data)
        
        # df.columns = student_header
        print(df)
        # df.loc[len(df)] = student_data
        df.to_csv('studentsFaces.csv')

# Unsubscribe the module.
faceProxy.unsubscribe("Test_Face")
tts.say("c'est bon.")
print ("Test terminated successfully.")