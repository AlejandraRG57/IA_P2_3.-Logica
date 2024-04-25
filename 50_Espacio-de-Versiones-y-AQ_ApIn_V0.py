#Alejandra Rodriguez Guevara 21310127 6E1

#El "Espacio de Versiones" es un concepto teórico en el contexto del aprendizaje automático que representa todas las posibles hipótesis consistentes con un conjunto dado de ejemplos de entrenamiento.

class AQ:
    def __init__(self):
        self.hypotheses = []

    def learn(self, X_pos, X_neg):
        #Inicializamos la hipótesis con la primera instancia positiva.
        hypothesis = X_pos[0]

        #Iteramos sobre las instancias positivas para encontrar una hipótesis más general.
        for instance in X_pos:
            for i in range(len(instance)):
                if instance[i] != hypothesis[i]:
                    hypothesis[i] = '?'  # '?' indicamos que el atributo puede ser cualquier valor.
        self.hypotheses.append(hypothesis)

        #Eliminamos instancias negativas inconsistentes.
        self.hypotheses = [h for h in self.hypotheses if not any(h[i] != '?' and h[i] != x[i] for x in X_neg for i in range(len(x)))]

    def predict(self, X):
        predictions = []
        for instance in X:
            for hypothesis in self.hypotheses:
                if all(h == '?' or h == x for h, x in zip(hypothesis, instance)):
                    predictions.append(1)
                    break
            else:
                predictions.append(0)
        return predictions

X_pos = [[1, 1, 0], [0, 1, 0], [1, 0, 1]]
X_neg = [[0, 0, 1], [1, 0, 0], [0, 1, 1]]

aq = AQ()
aq.learn(X_pos, X_neg)

#Predicciones en ejemplos de prueba.
X_test = [[1, 0, 0], [0, 1, 1], [1, 1, 1]]
predictions = aq.predict(X_test)
print(predictions)  #Salida esperada: [1, 1, 1]
