from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.datasets import mnist
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
import pandas as pnd
import numpy as np

dataset = pnd.read_csv('studentsFaces.csv',sep=',') 


# Scindage du corpus en 3
train, validate, test = np.split(dataset.sample(frac=1), [int(.8*len(dataset)), int(.9*len(dataset))])

train = pnd.DataFrame(train)
test = pnd.DataFrame(test)
validate = pnd.DataFrame(validate)

# Creation du model
model = Sequential()
model.add(Dense(100, activation='relu', input_dim=7))
model.add(Dense(50, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=[tf.keras.metrics.Precision()])

attribut = ['leftEyePoint1','leftEyePoint2','leftEyePoint3','leftEyePoint4','leftEyePoint5','leftEyePoint6'
        ,'rightEyePoint1','rightEyePoint2','rightEyePoint3','rightEyePoint4','rightEyePoint5','rightEyePoint6'
        , 'nosePoint1','nosePoint2','nosePoint3','nosePoint4','nosePoint5','nosePoint6'
        , 'mouthPoint1','mouthPoint2','mouthPoint3','mouthPoint4','mouthPoint5','mouthPoint6']

# Sortie
y_train = train.numEtudiant
y_test = test.numEtudiant
y_validate = validate.numEtudiant

# Entree
X_train = train[attribut]
X_test = test[attribut]
X_validate = validate[attribut]


# Nombre d'étudiant
nb_classes = 3

# Transformation des numéro d'étudiant en vecteur OneHot
y_train = to_categorical(y_train, nb_classes)
y_test = to_categorical(y_test, nb_classes)
y_validate = to_categorical(y_validate, nb_classes)


# Training
model.fit(X_train, y_train
, epochs=20, verbose=1, validation_data=(X_validate,y_validate))

# Evaluation
score = model.evaluate(X_test, y_test, verbose=0)
print('Test score:', score[0])
print('Test precision:', score[1])



