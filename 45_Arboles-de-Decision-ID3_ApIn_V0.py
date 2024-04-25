#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo ID3 (Iterative Dichotomiser 3) es un algoritmo de aprendizaje supervisado utilizado para construir árboles de decisión a partir de conjuntos de datos etiquetados.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#Cargamos el conjunto de datos de iris.
iris = load_iris()
X = iris.data
y = iris.target

#Dividimos los datos en conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Construimos el modelo de árbol de decisión utilizando ID3.
model = DecisionTreeClassifier(criterion="entropy", random_state=42)
model.fit(X_train, y_train)

#Hacemos predicciones en el conjunto de prueba.
y_pred = model.predict(X_test)

#Calculamos la precisión del modelo.
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)