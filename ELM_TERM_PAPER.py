import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from google.colab import files

upload=files.upload()

da = pd.read_excel("dataset for buildings energy consumption of 3840 records (1).xlsx")
da

X = da.iloc[:, list(range(0, 10)) + list(range(15, 23))]
X

Y = da.iloc[:, 13]
Y

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=2529)

class ELM:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_weights = np.random.randn(input_size, hidden_size) * 0.5
        self.biases = np.random.randn(hidden_size) * 0.5
        self.output_weights = None
        self.hidden_size = hidden_size
        self.output_size = output_size

    def sigmoid(self, X):
        return 1 / (1 + np.exp(-X))

    def train(self, X, Y):
        H = self.sigmoid(np.dot(X, self.input_weights) + self.biases)
        self.output_weights = np.dot(np.linalg.pinv(H), Y)

    def predict(self, X):
        H = self.sigmoid(np.dot(X, self.input_weights) + self.biases)
        return np.dot(H, self.output_weights)

hidden_size = 100
output_size = 1
elm_model = ELM(input_size=X_train.shape[1], hidden_size=hidden_size, output_size=output_size)

elm_model.train(X_train, Y_train)
Y_pred = elm_model.predict(X_test)

mse = mean_squared_error(Y_test, Y_pred)
mae = mean_absolute_error(Y_test, Y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(Y_test, Y_pred)

threshold = Y_test.mean()
Y_test_binary = (Y_test > threshold).astype(int)
Y_pred_binary = (Y_pred > threshold).astype(int)
accuracy = accuracy_score(Y_test_binary, Y_pred_binary)

print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R2 Score: {r2:.4f}")
print(f"Accuracy: {accuracy:.4f}")

