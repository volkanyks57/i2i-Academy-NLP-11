# i2i-Academy-NLP-11
Python, Pandas ve TextBlob ile Amazon ürün yorumları üzerinde sentiment analizi

# Özet
  Bu projede bir NLP uygulaması geliştirilerek Amazon ürün yorumları üzerinde sentiment
  analizi yapıldı. Yaklaşık 5000 İngilizce yorum içeren bir dataset Pandas ile yüklendi,
  metinler temizlendi ve TextBlob kütüphanesi ile her yorum Positive, Negative ya da Neutral
  olarak etiketlendi. Sonuçların istatistikleri hesaplanarak yorumların büyük çoğunluğunun
  pozitif olduğu görüldü.

# Tamamlanan Görevler
  - Amazon ürün yorumları içeren CSV dataset Pandas ile yüklendi.
  - Boş yorumlar veri setinden çıkarıldı.
  - Metin temizleme fonksiyonu yazıldı (küçük harfe çevirme, noktalama kaldırma, stop words filtreleme).
  - TextBlob ile her yorumun polarity skoru hesaplandı.
  - Skorlara göre yorumlar Positive, Negative ve Neutral olarak etiketlendi.
  - Sonuçlar yeni bir kolon olarak eklendi ve istatistikler yazdırıldı.
  - Etiketlenmiş sonuçlar ayrı bir CSV dosyasına kaydedildi.

# Kullanılan Teknolojiler
- Python 3.11
- Pandas
- TextBlob
- NLTK
