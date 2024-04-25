#Alejandra Rodriguez Guevara 21310127 6E1

#M5 es un algoritmo que combina los conceptos de árboles de decisión y regresión. A diferencia de los árboles de decisión clásicos, que se utilizan principalmente 
#para problemas de clasificación, los árboles de regresión M5 están diseñados para problemas de regresión, donde la variable objetivo es continua en lugar de discreta. 

import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#Generamos datos de ejemplo.
np.random.seed(42)
X = np.random.rand(100, 1)  #Variable independiente.
y = 2 * X + 1 + 0.1 * np.random.randn(100, 1)  #Variable dependiente con ruido.

#Dividimos los datos en conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Creamos un árbol de regresión M5P
m5p_model = DecisionTreeRegressor(max_depth=3)  #Ajustamos la profundidad del árbol según nuestras necesidades.
m5p_model.fit(X_train, y_train)

#Realizamos predicciones en el conjunto de prueba.
y_pred = m5p_model.predict(X_test)

#Evalúamos el rendimiento del modelo.
mse = mean_squared_error(y_test, y_pred)
print(f"Error cuadrático medio: {mse:.4f}")

#Visualizamos el árbol.
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plot_tree(m5p_model, filled=True, feature_names=["X"])
plt.title("Árbol de Regresión M5P")
plt.show()