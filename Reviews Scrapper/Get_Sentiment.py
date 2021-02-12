from unidecode import unidecode
from textblob import TextBlob

def GetSentiment(Text):
    uni_text = unidecode(Text)
    analysis = TextBlob(uni_text)
    sentiment = analysis.sentiment.polarity
    return sentiment