#Alejandra Rodriguez Guevara 21310127 6E1

#Las K-Decision Lists son una generalización de las listas de decisión binarias a múltiples clases.
#Los K-Decision Trees son una variante de los árboles de decisión que permite la clasificación de datos en múltiples clases.

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#Generamos datos de ejemplo.
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

#Dividimos los datos en conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Entrenamos un clasificador de árbol de decisión.
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

#Hacemos predicciones en el conjunto de prueba.
y_pred = clf.predict(X_test)

#Calculamos la precisión del clasificador.
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del árbol de decisión:", accuracy)