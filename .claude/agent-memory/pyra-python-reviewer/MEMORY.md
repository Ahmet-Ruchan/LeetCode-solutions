# Pyra Python Reviewer — Agent Memory
# Son guncelleme: 2026-02-20
# Maksimum 200 satir

## Ogrenci Profili
- Ogrenme deposu: CS50 + LeetCode, Python 3.12+, macOS Apple Silicon
- Baslangic seviyesi: Temel Python bilgisi var, algoritmik dusunce gelisiyor
- Ilk inceleme: 2026-02-20

## Puanlama Gecmisi
| Tarih | Dosya | Guvenlik | Kod Kalitesi | Okunabilirlik |
|---|---|---|---|---|
| 2026-02-20 | LeetCode/Two Sum/two_sum.py | 7/10 | 3/10 | 5/10 |

## Tekrar Eden Hatalar (seans numarasiyla)
- `range(len(x))` yerine `enumerate` kullanmamak: seans 1
- `if __name__ == "__main__":` guard eksikligi: seans 1
- Fonksiyon sonucunu `return` yerine `print()` ile vermek: seans 1
- camelCase fonksiyon adi (`twoSum` yerine `two_sum`): seans 1
- Modül seviyesi degiskenleri UPPER_SNAKE_CASE yazmamak: seans 1
- Gereksiz baslangic atamalari (`needed = 0`): seans 1
- `else` after `break` gereksiz kullanim: seans 1

## Dogru Yapilan Seyler (seans numarasiyla)
- Hash map (dictionary) ile O(n) Two Sum cozumu: seans 1 — algoritma secimi mukemmel
- Type hint kullanimi denemesi (eksik ama girisim var): seans 1
- Inline yorum yazma aliskanligi: seans 1

## Sonraki Seansa Not
- `print` vs `return` farki pekistirilmeli
- `enumerate` kullanimini takip et — ogrenildi mi?
- `if __name__ == "__main__":` guard her dosyada var mi kontrol et
- Naming conventions (snake_case, UPPER_SNAKE_CASE) pekistirilmeli

## Guclu Yonler
- Algoritma secimi (hash map) dogru ve verimli

## Arac Durumu
- pylint: kurulu (pip3 --break-system-packages ile, 2026-02-20)
- mypy: kurulu (pip3 --break-system-packages ile, 2026-02-20)
- py_compile: Python stdlib, her zaman mevcut
