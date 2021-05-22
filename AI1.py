'''
    This Program has a lot of place holder variables. Change them and add the data that fits your needs.
    
    By the way this program was supposed to have more NNs, that is why I have created
    many instanses and classes of algorithms.
    Made by Stavros Klaoudatos
'''



import tensorflow as tf
import tensorboard
import tensorflow.keras
from tensorflow.keras import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.datasets import fashion_mnist
import sklearn
from sklearn import tree
import face_recognition
import cv2
import numpy as np
from Speak_Text import SpeakText
from tensorflow.keras.preprocessing.text import Tokenizer
import json
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import Sequential
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam




class AI_Command(object):

    def __init__(self, model, algorithm):
        self.model = model
        self.algorithm = algorithm

    class NeuralNetwork(object):

        def __init__(self):
            self.model = Sequential()
            self.algorithm = 'Neural NeuralNetwork'

    class DecisionTreeClassifier(object):
        def __init__(self):
            self.model = tree.DecisionTreeClassifier
            self.algorithm = 'Decision Tree'
    class SpeechPrediction(object):
        def __init__(self):
            self.model = Tokenizer(num_words=10000000000,oov_token='<OOV>')
            self.algorithm = 'Natural Language Processing'


    def Face_Recognition(self):

        self.algorithm = 'Face recognition'
        video_capture = cv2.VideoCapture(1)



        
        # Create arrays of known face encodings and their names
        person1_image = face_recognition.load_image_file('image of person1.jpg')
        person1_face_encoding = face_recognition.face_encodings(person1_image)[0]
        .
        .
        .
        .



        known_face_encodings = [
            person_face_encoding,
            .
            .
            .

        ]
        known_face_names = [
            "Name of Person 1",
            .
            .
            .
            .
            

        ]


        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while True:

            ret, frame = video_capture.read()

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

           
            rgb_small_frame = small_frame[:, :, ::-1]

      
            if process_this_frame:

                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
  
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                    stringtoappend = name + ' Male'
                    face_names.append(stringtoappend)

                    hello = 'Hello  ' + str(name)
                    print(hello)
            process_this_frame = not process_this_frame



            for (top, right, bottom, left), name in zip(face_locations, face_names):
                
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

  
            cv2.imshow('Video', frame)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


        video_capture.release()
        cv2.destroyAllWindows()



NN1 = AI_Command.NeuralNetwork()
NN2 = AI_Command.NeuralNetwork()
NN3 = AI_Command.NeuralNetwork()
NN4 = AI_Command.NeuralNetwork()
NN5 = AI_Command.NeuralNetwork()

Tree1 = AI_Command.DecisionTreeClassifier()
Tree2 = AI_Command.DecisionTreeClassifier()
Tree3 = AI_Command.DecisionTreeClassifier()
Tree4 = AI_Command.DecisionTreeClassifier()
Tree5 = AI_Command.DecisionTreeClassifier()


Face_Recognition = AI_Command('-','Face_Recognition')
Voice_Recognition = AI_Command('-','Voice_Prediction')


Face_Recognition.Face_Recognition()





