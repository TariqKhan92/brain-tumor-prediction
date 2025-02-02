import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load your trained model
model = load_model('C:\Users\HC\Downloads\brain tumor prediction\model.h5')

# Define class labels
CLASSES = ['pituitary', 'glioma', 'no tumor', 'meningioma']

def predict_tumor(image_path):
    # Preprocess the uploaded image
    img = load_img(image_path, target_size=(150, 150))  # Adjust size based on your model
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = CLASSES[np.argmax(predictions)]
    confidence = np.max(predictions)
    
    return predicted_class, confidence
