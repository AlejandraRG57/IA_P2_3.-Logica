#Alejandra Rodriguez Guevara 21310127 6E1

#La "Mejor Hipótesis Actual" es el modelo que mejor se ajusta a los datos de entrenamiento disponibles en un momento dado, según una métrica de evaluación específica. 

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Generamos datos de ejemplo.
X, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)

#Dividimos los datos en conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Entrenamos un modelo de regresión lineal.
model = LinearRegression()
model.fit(X_train, y_train)

#Hacemos predicciones en el conjunto de prueba.
y_pred = model.predict(X_test)

#Calculamos el error cuadrático medio.
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio:", mse)