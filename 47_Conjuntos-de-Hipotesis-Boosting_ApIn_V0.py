#Alejandra Rodriguez Guevara 21310127 6E1

#El boosting es un método de ensamble que combina múltiples hipótesis más débiles para construir un clasificador más fuerte.

import numpy as np

#Clase Boosting para el algoritmo de boosting.
class Boosting:
    def __init__(self, n_estimators=50, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators #Número de árboles.
        self.learning_rate = learning_rate #Tasa de aprendizaje.
        self.max_depth = max_depth #Profundidad máxima de los árboles.
        self.estimators = [] #Lista de árboles.

    #Método para entrenar el modelo de boosting.
    def fit(self, X, y):
        n_samples = X.shape[0]
        weights = np.ones(n_samples) / n_samples #Inicializamos los pesos de las muestras.

        #Iteramos sobre el número de árboles.
        for _ in range(self.n_estimators):
            tree = DecisionTree(max_depth=self.max_depth) #Inicializamos un árbol de decisión.
            tree.fit(X, y, sample_weight=weights) #Ajustamos el árbol con los pesos de las muestras.
            y_pred = tree.predict(X) #Hacemos predicciones con el árbol.
            error = np.sum(weights * (y_pred != y)) / np.sum(weights) #Calculamos el error ponderado.

            #Calculamos el peso del clasificador.
            if error == 0: #Evitamos la división por cero.
                alpha = 1
            else:
                alpha = self.learning_rate * np.log((1 - error) / error)

            #Actualizamos los pesos de las muestras.
            weights *= np.exp(alpha * (y_pred != y))
            #Normalizamos los pesos.
            weights /= np.sum(weights)
            #Guardamos el peso y el árbol.
            self.estimators.append((alpha, tree))

    #Método para hacer predicciones.
    def predict(self, X):
        y_pred = np.zeros(X.shape[0])
        #Sumamos las predicciones ponderadas de cada árbol.
        for alpha, tree in self.estimators:
            y_pred += alpha * tree.predict(X)
        #Clasificamos las predicciones.
        return np.sign(y_pred)

#Clase DecisionTree para árboles de decisión.
class DecisionTree:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth #Profundidad máxima del árbol.
        self.tree = {} #Estructura del árbol.

    #Método para ajustar el árbol.
    def fit(self, X, y, sample_weight=None):
        #Crecemos el árbol.
        self.tree = self._grow_tree(X, y, sample_weight=sample_weight)

    #Método interno para crecer el árbol.
    def _grow_tree(self, X, y, depth=0, sample_weight=None):
        #Obtenemos el número de muestras y características.
        n_samples, n_features = X.shape
        #Devolvemos la clase mayoritaria si se alcanza la profundidad máxima o no hay varianza en las etiquetas.
        if depth >= self.max_depth or np.std(y) == 0:
            return np.sign(np.mean(y))

        #Inicializamos variables para la mejor característica, umbral y gini.
        best_feature, best_threshold = None, None
        best_gini = float('inf')

        #Iteramos sobre todas las características.
        for feature in range(n_features):
            #Encontramos los umbrales únicos para la característica actual.
            thresholds = np.unique(X[:, feature])
            #Iteramos sobre los umbrales.
            for threshold in thresholds:
                #Dividimos los datos en dos conjuntos usando el umbral.
                left_indices = X[:, feature] < threshold
                right_indices = ~left_indices
                #Calculamos el índice de Gini ponderado.
                left_gini = self._gini(y[left_indices], sample_weight=sample_weight[left_indices])
                right_gini = self._gini(y[right_indices], sample_weight=sample_weight[right_indices])
                gini = (np.sum(sample_weight[left_indices]) * left_gini + np.sum(sample_weight[right_indices]) * right_gini) / n_samples
                #Actualizamos la mejor característica y umbral si se encuentra un menor índice de Gini.
                if gini < best_gini:
                    best_gini = gini
                    best_feature = feature
                    best_threshold = threshold

        #Devolvemos la clase mayoritaria si no se puede dividir más.
        if best_gini == float('inf'):
            return np.sign(np.mean(y))

        #Dividimos los datos en dos subconjuntos y crecemos los subárboles izquierdos.

        left_indices = X[:, best_feature] < best_threshold
        right_indices = ~left_indices
        left_subtree = self._grow_tree(X[left_indices], y[left_indices], depth + 1, sample_weight=sample_weight[left_indices])
        right_subtree = self._grow_tree(X[right_indices], y[right_indices], depth + 1, sample_weight=sample_weight[right_indices])

        #Devolvemos la estructura del árbol con la mejor característica, umbral y subárboles.
        return {'feature': best_feature, 'threshold': best_threshold, 'left': left_subtree, 'right': right_subtree}

    #Método para calcular el índice de Gini.
    def _gini(self, y, sample_weight=None):
        #Calculamos la proporción de cada clase.
        if sample_weight is None:
            p1 = np.sum(y == 1) / len(y)
            p2 = np.sum(y == -1) / len(y)
        else:
            p1 = np.sum(y == 1) / np.sum(sample_weight)
            p2 = np.sum(y == -1) / np.sum(sample_weight)
        #Calculamos el índice de Gini.
        return 1 - p1**2 - p2**2

    #Método para hacer predicciones recursivas.
    def predict(self, X):
        return np.array([self._predict(x, self.tree) for x in X])

    #Método interno para hacer predicciones recursivas.
    def _predict(self, x, node):
        #Devolvemos la clase si el nodo es una hoja.
        if isinstance(node, (int, float)):
            return node
        #Obtenemos la mejor característica y umbral del nodo.
        feature, threshold = node['feature'], node['threshold']
        #Elegimos el subárbol izquierdo o derecho según el valor de la característica.
        if x[feature] < threshold:
            return self._predict(x, node['left'])
        else:
            return self._predict(x, node['right'])

#Generamos datos sintéticos.
np.random.seed(0)
X = np.random.rand(100, 2) * 10 - 5 #Características.
y = np.sign(X[:, 0]**2 + X[:, 1]**2 - 9) #Etiquetas.

#Dividimos los datos en conjuntos de entrenamiento y prueba.
X_train, X_test = X[:80], X[80:]
y_train, y_test = y[:80], y[80:]

#Entrenamos el modelo de Boosting.
boosting = Boosting(n_estimators=50, learning_rate=0.1, max_depth=3)
boosting.fit(X_train, y_train)

#Hacemos predicciones en el conjunto de prueba.
y_pred = boosting.predict(X_test)

#Calculamos la precisión.
accuracy = np.mean(y_pred == y_test)
print("Precisión:", accuracy)