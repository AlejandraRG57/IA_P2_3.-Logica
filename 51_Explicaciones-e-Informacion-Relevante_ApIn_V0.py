#Alejandra Rodriguez Guevara 21310127 6E1

#El aprendizaje inductivo es un enfoque en el aprendizaje automático donde se intenta generalizar patrones a partir de ejemplos específicos.
#Se basa en la premisa de que los datos de entrenamiento contienen información sobre cómo se deben clasificar o predecir nuevas instancias.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#Cargamos el conjunto de datos de Iris.
iris = load_iris()
X = iris.data
y = iris.target

#Dividimos el conjunto de datos en entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Inicializamos y entrenamos un clasificador de árbol de decisión.
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

#Realizamos predicciones en el conjunto de prueba.
y_pred = clf.predict(X_test)

#Calculamos la precisión del clasificador.
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador de árbol de decisión:", accuracy)