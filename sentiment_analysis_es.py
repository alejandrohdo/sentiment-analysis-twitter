""""Script que calcula sentimientos en ESPAÑOL, va de 0  a 1
donde 0 es negativo, 0.5 neutro y 1 es positivo"""
from classifier import SentimentClassifier

clf = SentimentClassifier()

x = "Esta muy buena esa pelicula"

y = "Que horrible comida!!!"

z = "Tuve una experiencia netural"

#sentimiento = clf.predict(x)
#sentimiento = clf.predict(y)
sentimiento = clf.predict(y)

print(sentimiento)