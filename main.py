import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import Sequential
from keras.layers import Dense
from tensorflow import keras


def inputData():
  print("Ввод Да или Нет")
  a=str(input("На тебя кричали?"))
  if a == "да" or a == "Да" or a == "ДА":
    a = 1
  else:
    a = 0
  b=str(input("Тебя это задело?"))
  if b == "да" or b == "Да" or b == "ДА":
    b = 1
  else:
    b = 0
  c=str(input("Тебе грустно?"))
  if c == "да" or c == "Да" or c == "ДА":
    c = 1
  else:
    c = 0
  d=str(input("Ты хочешь кушать?"))
  if d == "да" or d == "Да" or d == "ДА":
    d = 1
  else:
    d = 0
  
  array=[a,b,c,d]
  return array

def otv(array):
  ii=array[0][0]
  if ii>=0.9:
    return "\n\nЭто обидно"
  elif ii<0.9 and ii >= 0.2:
    return "\n\nНе обижайся, всё хорошо"
  else:
    return "\n\nНе приятно"


c=np.array([
    [1,1,1,1],
   [1,1,1,0],
   [1,1,0,1],
   [1,0,1,1],
   [0,1,1,1],
   [0,0,0,0],
   [1,0,0,0],
   [0,1,1,0],
   [1,1,0,0],
   [1,0,1,0]
   ])
f=np.array([1, 1, 0.6, 0.6, 0, 0, 0, 0, 1, 0])


model = keras.Sequential()
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))
history = model.fit(c, f, epochs=600, verbose=0)

reshenie=model.predict([inputData()])
print(otv(reshenie))

