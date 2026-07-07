import pandas as pd
import string
from textblob import TextBlob

# NLTK stop words listesini kullanmak için gerekli modülleri indiriyoruz
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# CSV dosyasını okuyoruz
df = pd.read_csv("amazon_review.csv")
print("Toplam yorum sayisi:", len(df))

# reviewText kolonunda boş değerleri çıkarıyoruz
df = df.dropna(subset=["reviewText"])
print("Bos yorumlar cikarildi, kalan yorum sayisi:", len(df))

# İngilizce stop words listesini alıyoruz
stop_words = set(stopwords.words("english"))

# Metni temizliyoruz
def metni_temizle(text):
    text = str(text).lower()                                  # küçük harfe çevir
    text = text.translate(str.maketrans("", "", string.punctuation))  # noktalama temizle
    kelimeler = text.split()                                   # kelimelere ayır
    kelimeler = [k for k in kelimeler if k not in stop_words]  # stop words'leri at
    return " ".join(kelimeler)

# Temizlenmiş metni yeni bir kolona ekliyoruz
df["cleaned_review"] = df["reviewText"].apply(metni_temizle)

# TextBlob ile her bir yorumun sentiment skorunu hesaplıyoruz
# Skor -1 ile 1 arasında değişir
# -1: Negatif, 0: Nötr, 1: Pozitif
def sentiment_skoru(text):
    return TextBlob(text).sentiment.polarity

# Skoru yeni bir kolona yazıyoruz
df["sentiment_score"] = df["cleaned_review"].apply(sentiment_skoru)

# Skora göre etiketi belirliyoruz
def etiketle(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# Etiketi yeni bir kolona yazıyoruz
df["sentiment_label"] = df["sentiment_score"].apply(etiketle)

# Sonuç istatistiklerini yazdırıyoruz
print("\n--- Sentiment Analizi Sonuclari ---")
print(df["sentiment_label"].value_counts())

print("\n--- Yuzdesel Dagilim ---")
print(df["sentiment_label"].value_counts(normalize=True).round(3) * 100)

# Örnek olarak ilk 5 yorumu ve sentiment etiketlerini yazdırıyoruz
print("\n--- Ornek Yorumlar ---")
print(df[["reviewText", "sentiment_label"]].head())

# Sonuçları yeni bir CSV dosyasına kaydediyoruz
df.to_csv("sentiment_results.csv", index=False)
print("\nSonuclar sentiment_results.csv dosyasina kaydedildi.")