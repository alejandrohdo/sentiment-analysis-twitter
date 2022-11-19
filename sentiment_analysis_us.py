""""Script que calcula sentimientos en INGLES, va de -1  a 1
donde -1 es negativo, 0 neutro y 1 es positivo"""
from nltk.sentiment.vader import SentimentIntensityAnalyzer

x = "It is a charming and beautiful product"
y = "It was a horrible experience!"
z = "I have nothing to say. Normal so far"

aa = """What do you think of a child watching in Willax a pedophile with a gun spitting out fake news, on ATV a magpie taking gossip and ripping off other people's lives or a group of gorillas stacking glasses and ventilating their grips?
That is the polarizing #TVBasura, loaded with hate that you sell."""
sid = SentimentIntensityAnalyzer()
resultados = sid.polarity_scores(aa)
print (resultados)

# import pandas as pd
# df = pd.read_csv("sentimientos_ingles.csv")
# df["sentimiento"] = df["mensaje"].apply(lambda i: sid.polarity_scores(i)['compound'])
# df.to_csv('mensajes_con_sentimientos.csv')