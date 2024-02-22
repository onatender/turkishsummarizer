# Python Metin Özetleyici 📝💻

Bu proje, kullanıcının belirlediği dosyadaki Türkçe metni özetleyen bir Python betiğini içerir. Betik, kullanıcı tarafından belirtilen dosya yolundaki metni analiz eder, en sık geçen ve en önemli kelimeleri belirler ve kullanıcının belirlediği sayı kadar önemli kelimeyi metin içerisinde bulup çıkarır.

## Kullanım

Python dosyası, aşağıdaki gibi çağrılabilir:

```bash
python main.py --file dosya.txt --words 3
```

- `dosya.txt`: Türkçe metnin bulunduğu dosyanın yolu.
- `--words 3`: Metin özetlendikten sonra dönüşte bulunacak önemli kelime sayısı.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki kütüphanelere ihtiyaç duyulmaktadır:
- [snowballstemmer](https://pypi.org/project/snowballstemmer/): Türkçe metinlerde kök bulma ve dil analizi işlemleri için kullanılır.
- [trtokenizer](https://pypi.org/project/trtokenizer/): Türkçe metinlerin belirli ölçülerde parçalanması ve analizi için gereklidir.

Kurulum için aşağıdaki komutları kullanabilirsiniz:

```bash
pip install -r requirements.txt
```

## Örnek Çıktı

Örnek bir çıktı, aşağıdaki gibidir:

```plaintext
First 3 keywords are:
- Fenerbahçe
- Spor
- Futbol
```
