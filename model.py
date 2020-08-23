import pandas as pd
from states import states_names, state_codes,get_state_code
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from inputs import to_dataframe

checkpoint_path = "hack-for-people/cp.ckpt"


def build_model():
    model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[15]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
  ])
    
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    
    model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse', 'accuracy'])
    
    return model

# build model
model = build_model()
model.load_weights(checkpoint_path)
# test predictions
listt = [7991.245605,1681.732666,827.223572,1558.236084,1478.948486,322.951813,235.153625,1886.999268,4892.252930,2015,5.7,63.6,26.8,1.5, 0.2]
test_predictions = model.predict(to_dataframe(listt))
print(test_predictions)

def predict(vals):
      return model.predict(to_dataframe(vals))[0][0]
