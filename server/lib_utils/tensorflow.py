# prompt: creat code for prediction image

import tensorflow as tf
from tensorflow import keras
import numpy as np

# Load the saved model
rice_model = keras.models.load_model("models/rice_model.h5")
potato_model = keras.models.load_model("models/potato_model.h5")


def predict_rice_image(image):
    """
    Predicts the class of an image using the loaded model.

    Args:
        image_path: Path to the image file.

    Returns:
        A dictionary containing the predicted class label and confidence score.
    """
    img = tf.keras.preprocessing.image.load_img(image, target_size=(416, 416))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize

    predictions = rice_model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    confidence = predictions[0][predicted_class]

    # Assuming you have a label map (replace with your actual label map)
    label_map = {
        0: "helminthosporium_oryzae",
        1: "xanthomonas_oryzae",
        2: "ustilaginoidea_virens",
        3: None,
        4: "health",
    }  # Example

    predicted_label = label_map.get(predicted_class, None)

    if predicted_label is not None or predicted_label is not "health":
        return {"label": predicted_label, "confidence": float(confidence)}
    elif predicted_label is None:
        return {"error": "this image is not leaf"}
    elif predicted_label is "health":
        return {"label": predicted_label, "confidence": float(confidence)}


def predict_potato_image(image):
    """
    Predicts the class of an image using the loaded model.

    Args:
        image_path: Path to the image file.

    Returns:
        A dictionary containing the predicted class label and confidence score.
    """
    img = tf.keras.preprocessing.image.load_img(image, target_size=(416, 416))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize

    predictions = potato_model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    confidence = predictions[0][predicted_class]

    # Assuming you have a label map (replace with your actual label map)
    label_map = {
        0: "alternaria_solani",
        1: "phytophthora_infestans",
        2: "health",
        3: None,
    }  # Example

    predicted_label = label_map.get(predicted_class, None)

    if predicted_label is not None or predicted_label is not "health":
        return {"label": predicted_label, "confidence": float(confidence)}
    elif predicted_label is None:
        return {"error": "this image is not leaf"}
    elif predicted_label is "health":
        return {"label": predicted_label, "confidence": float(confidence)}
