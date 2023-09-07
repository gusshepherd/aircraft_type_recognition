
from recognition.helpers.load_model import load_model
import numpy as np
from recognition.interface.preprocessor import preprocess_image_tensor
aircraft_classes = ['737', '747', '767', 'A340', 'CRJ', 'DC', 'DHC', 'E', 'MD']
def predict_image(image_processed, model):
  y_pred = model.predict(image_processed)
  output = np.array(y_pred)
  predicted_index = np.argmax(output)
  predicted_class = aircraft_classes[predicted_index]
  print("\n✅ prediction done: ", predicted_class, "\n")
  return predicted_class