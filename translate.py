from googletrans import Translator

translator = Translator()
txt='Comment allex vous?'
output=translator.Translate(txt, dest='en')

print(output.text)