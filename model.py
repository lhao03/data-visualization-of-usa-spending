import pandas as pd
from states import states_names, state_codes,get_state_code
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

checkpoint_path = "hack-for-people/cp.ckpt"


def build_model():
    model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
  ])
    
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae', 'mse'])
#     model.compile(loss='mse',
#                 optimizer=optimizer,
#                 metrics=['mae', 'mse', 'accuracy'])
    
    return model

# build model
model = build_model()
model.load_weights(checkpoint_path)
# test predictions

normed_test_data = 

test_predictions = model.predict(normed_test_data)