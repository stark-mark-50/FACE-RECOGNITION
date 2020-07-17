import os
from deepface import DeepFace
while True:

    p=input("Enter -----   ")



    demography = DeepFace.analyze((p+str(".jpg")), actions = ['age','emotion'])
    #demographies = DeepFace.analyze(["img1.jpg", "img2.jpg", "img3.jpg"]) #analyzing multiple faces same time
    print("Age: ", demography["age"])
    ##print("Gender: ", demography["gender"])
    print("Emotion: ", demography["dominant_emotion"])
    ##print("Race: ", demography["dominant_race"])

    os.system(p+str(".jpg"))

##
##from deepface import DeepFace
##DeepFace.stream(r"C:\Users\admin\.deepface\weights")
