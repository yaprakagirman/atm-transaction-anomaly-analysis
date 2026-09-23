# ATM İşlem ve Anomali Analizi

Bu proje, sentetik ATM işlem verileri üzerinde veri temizleme, keşifsel veri analizi, istatistiksel testler ve anomali sınıflandırması uygular. Analizler Jupyter Notebook içinde adım adım yürütülür ve grafiklerle desteklenir.

Notebook; bir yıllık sentetik veri üretimi, eksik değer simülasyonu, aykırı değer analizi, ölçekleme, regresyon, hipotez testi ve karar ağacı tabanlı anomali tespiti bölümlerini içerir.

## Proje kapsamı

- 2024 yılını kapsayan 240.000 ATM işlemi
- 1.500 sentetik müşteri kimliği
- 80 ATM
- İşlem tutarı, işlem süresi, başarısız deneme sayısı ve konum bilgileri
- Yaklaşık %5 anomali sınıfı
- Tekrarlanabilir veri üretimi (`random_state=42`)
- Eksik değerlerin medyan ve mod ile tamamlanması
- IQR yöntemiyle aykırı değer analizi
- Min-Max, Z-score ve RobustScaler karşılaştırması
- OLS ve doğrusal regresyon analizi
- Spearman korelasyon analizi
- Mann–Whitney U hipotez testi
- Dengeli karar ağacı sınıflandırması
- Confusion matrix, özellik önem grafiği ve karar ağacı görselleştirmesi
- Markovian ve memoryless sistem yaklaşımının görsel açıklaması

## Dosyalar

```text
atm-transaction-anomaly-analysis/
├── atmproje1.ipynb
├── atm_islemleri_tr_1yil.csv
├── atm_islemleri_tr.csv
├── tests/
│   └── test_project_assets.py
├── requirements.txt
├── .gitignore
└── README.md
```

| Dosya | Açıklama |
| --- | --- |
| `atmproje1.ipynb` | Veri üretimi, analiz, modelleme ve görselleştirme adımlarını içeren ana notebook |
| `atm_islemleri_tr_1yil.csv` | Notebook’un varsayılan olarak kullandığı, 2024 yılını kapsayan 240.000 satırlık sentetik veri seti |
| `atm_islemleri_tr.csv` | Aynı şemaya sahip alternatif 240.000 satırlık sentetik veri seti |
| `requirements.txt` | Notebook’u çalıştırmak için gereken Python paketleri |
| `tests/test_project_assets.py` | Notebook ve veri dosyalarının yapısal bütünlük kontrolleri |

## Veri sözlüğü

Her iki CSV dosyası 14 sütun içerir.

| Sütun | Açıklama |
| --- | --- |
| `islem_id` | Benzersiz sentetik işlem kimliği |
| `zaman_damgasi` | İşlemin gerçekleştiği tarih ve saat |
| `musteri_id` | Sentetik müşteri kimliği |
| `atm_id` | Sentetik ATM kimliği |
| `atm_konumu` | ATM’nin şehir ve ilçe etiketi |
| `tutar` | İşlem tutarı |
| `durum` | İşlem sonucu: `success` veya `failed` |
| `hatali_deneme_sayisi` | İşlemle ilişkili başarısız deneme sayısı |
| `islem_suresi_sn` | İşlem süresi, saniye |
| `onceki_isleme_uzaklik_km` | Önceki işleme göre sentetik mesafe, kilometre |
| `saat` | Zaman damgasından çıkarılan saat, 0–23 |
| `haftanin_gunu` | Haftanın günü, Pazartesi=0 ve Pazar=6 |
| `saat_araligi` | Günün zaman dilimi etiketi |
| `anomali_mi` | Hedef değişken: normal=0, anomali=1 |

## Veri seti özeti

### `atm_islemleri_tr_1yil.csv`

- 240.000 satır
- Tarih aralığı: 1 Ocak 2024 – 31 Aralık 2024
- 1.500 müşteri kimliği
- 80 ATM
- 228.090 normal işlem
- 11.910 anomali
- Eksik değer yok
- Notebook bu dosyayı varsayılan veri kaynağı olarak okur

### `atm_islemleri_tr.csv`

- 240.000 satır
- Tarih aralığı: 1 Ocak 2024 – 31 Aralık 2024
- 1.500 müşteri kimliği
- 80 ATM
- 228.000 normal işlem
- 12.000 anomali
- Eksik değer yok
- Daha geniş konum ve saat aralığı kategorileri içeren alternatif veri setidir

## Kurulum

Repoyu klonlayın:

```bash
git clone https://github.com/yaprakagirman/atm-transaction-anomaly-analysis.git
cd atm-transaction-anomaly-analysis
```

Sanal ortam oluşturun:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Linux veya macOS:

```bash
source .venv/bin/activate
```

Bağımlılıkları kurun:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Çalıştırma

Jupyter Lab’i başlatın:

```bash
jupyter lab
```

Ardından `atmproje1.ipynb` dosyasını açıp hücreleri yukarıdan aşağıya çalıştırın.

Notebook’un ilk hücresi `atm_islemleri_tr_1yil.csv` veri setini aynı sabit seed ile yeniden üretir ve mevcut dosyanın üzerine yazar. Hazır veri setini değiştirmeden yalnızca analizi çalıştırmak istiyorsanız ilk hücreyi atlayıp ikinci hücreden başlayın.

## Analiz akışı

1. Sentetik ATM verisinin üretilmesi veya hazır CSV’nin yüklenmesi
2. Veri tiplerinin düzenlenmesi ve temel kalite kontrolleri
3. Kontrollü şekilde eksik değer eklenmesi
4. Sayısal eksiklerin medyanla, kategorik eksiklerin modla doldurulması
5. IQR ile işlem tutarı aykırı değerlerinin belirlenmesi
6. Dağılım, konum, zaman dilimi ve işlem durumu görselleştirmeleri
7. Tanımlayıcı istatistiklerin hesaplanması
8. Min-Max, StandardScaler ve RobustScaler dönüşümleri
9. OLS ve doğrusal regresyon analizi
10. Spearman korelasyon analizi
11. Mann–Whitney U testi
12. Karar ağacıyla anomali sınıflandırması
13. Markovian sistem yaklaşımının görselleştirilmesi

## Notebook’taki mevcut sonuçlar

Notebook ile birlikte kaydedilmiş çalıştırma çıktılarında aşağıdaki sonuçlar görülür:

- IQR üst sınırı: 558,09
- Tespit edilen aykırı işlem: 13.239
- Aykırı işlem oranı: %5,52
- Aykırı değerler çıkarıldıktan sonra kalan satır: 226.761
- OLS regresyonu R²: 0,083
- Mann–Whitney U testi p-değeri: 0’a çok yakın; normal ve anomali gruplarının tutar dağılımları anlamlı biçimde farklı
- Karar ağacı doğruluk oranı: %98,39

Bu sonuçlar notebook’ta kayıtlı çalıştırmaya aittir. İlk hücredeki seed değiştirilirse veya analiz adımları düzenlenirse sonuçlar değişebilir.

## Testler

Temel proje bütünlük kontrollerini çalıştırmak için:

```bash
python -m unittest discover -s tests -v
```

Testler şunları doğrular:

- Gerekli dosyaların mevcut olması
- Her CSV’nin beklenen 14 sütunu ve 240.000 veri satırını içermesi
- Notebook’un geçerli nbformat yapısında olması
- Notebook kod hücrelerinin Python tarafından derlenebilmesi
- Kaydedilmiş notebook çıktılarında hata bulunmaması

## Veri kalitesi notları

- Veriler gerçeğe ait müşteri veya kart bilgileri içermez; notebook içinde sentetik olarak üretilir.
- `atm_islemleri_tr_1yil.csv` içinde `Ankara_Keçiören` etiketi bazı ortamlarda karakter kodlaması nedeniyle bozuk görünebilir.
- İki CSV aynı sütunları içerir ancak konum ve zaman dilimi kategorileri birebir aynı değildir.
- Sınıf dağılımı dengesizdir. Bu nedenle yalnızca accuracy değerine bakmak yerine confusion matrix, precision, recall ve F1-score birlikte değerlendirilmelidir.

## Sınırlamalar

- Proje eğitim ve analiz amaçlı sentetik veri kullanır.
- Model gerçek bankacılık işlemlerinde doğrulanmamıştır.
- Çıktılar üretim ortamında dolandırıcılık kararı vermek için kullanılmamalıdır.
- Sentetik veri üretim kuralları bazı özelliklerle hedef değişken arasında doğrudan ilişki kurduğu için model performansı gerçek veriye göre iyimser olabilir.

