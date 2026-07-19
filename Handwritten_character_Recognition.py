import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np
# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape images for CNN
x_train = x_train.reshape((-1, 28, 28, 1))
x_test = x_test.reshape((-1, 28, 28, 1))

# Build CNN model
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.2
)

# Evaluate model
loss, accuracy = model.evaluate(x_test, y_test)

print("Test Accuracy:", accuracy)

# Save model
model.save("handwritten_digit_model.h5")
print("Model saved successfully!")

# Load trained model
model = tf.keras.models.load_model("handwritten_digit_model.h5")

# Load MNIST test dataset
(_, _), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize
x_test = x_test / 255.0

# Select an image
index = 0

image = x_test[index]
input_image = image.reshape(1, 28, 28, 1)

# Predict
prediction = model.predict(input_image)

digit = np.argmax(prediction)

print("Predicted Digit:", digit)
print("Actual Digit:", y_test[index])

# Display image
plt.imshow(image, cmap="gray")
plt.title(f"Prediction: {digit}")
plt.axis("off")
plt.show()
