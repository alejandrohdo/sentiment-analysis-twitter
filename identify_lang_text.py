import spacy
from spacy_langdetect import LanguageDetector

spacy_nlp =  spacy.load('en_core_web_sm')
spacy_nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)

def identify_language_text(text):
	"""Identificacion de Lang de un post"""
	try:
		global spacy_nlp
		doc = spacy_nlp(text)
		return doc._.language.get('language') 
	except Exception as e:
		print ('Error de reconocimiento de lenguaje:', e)

print("Resultado>", identify_language_text('I honestly don’t understand your angle/issue here..'))