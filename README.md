# CS50 & LeetCode Learning Repository

Bu repo, CS50 ders alıştırmalarını ve LeetCode algoritma sorularını çözdüğüm kişisel öğrenme alanımdır. Kodlar **C** ve **Python** dillerinde yazılmaktadır.

---

## İçerik

### CS50 — C Programming

CS50 derslerini takip ederek yazdığım C programları, ders bazında klasörlenmiştir.

```
CS50/
└── Lecture-1/
    └── main.c
```

Derleme (macOS / Apple Silicon):
```bash
clang -o output/<isim> "CS50/<Lecture-N>/main.c"
```

### LeetCode Solutions — Python

Her LeetCode problemi kendi klasöründe, tek bir `main.py` dosyasıyla çözülmüştür. Dosyanın altında test girişi hardcoded olarak bulunur.

```
LeetCode Solutions/
└── With Python/
    ├── Two Sum/
    │   └── main.py
    └── 1-bit and 2-bit Characters/
        └── main.py
```

Çalıştırma:
```bash
python3 "LeetCode Solutions/With Python/<Problem Adı>/main.py"
```

---

## AI Agents

Bu repo, kod inceleme süreçlerini otomatikleştiren iki özel Claude ajanıyla donatılmıştır. Her ajan, ilgili bir dosya yazıldığında veya paylaşıldığında **otomatik olarak devreye girer**.

---

### Rex — C Kod İnceleme Ajanı

> *20+ yıllık sistem programlama deneyimine sahip, katı ama eğitici bir C kod gözlemcisi.*

**Ne zaman çalışır:**
- Bir `.c` veya `.h` dosyası yazıldığında ya da değiştirildiğinde
- C kodu paylaşıldığında veya hata ayıklama istendiğinde

**Ne yapar:**
- Kodu `clang -fsanitize=address,undefined` ile derler ve sanitizer çıktısını raporlar
- Bellek sızıntısı, buffer overflow, dangling pointer, format string açığı gibi **kritik güvenlik hatalarını** tespit eder
- Kod kalitesi, isimlendirme kuralları, hata yönetimi gibi uyarı ve önerileri listeler
- Güvenlik, Kod Kalitesi ve Okunabilirlik için **10 üzerinden puanlar verir**
- Düzeltilmiş kodu ve öğrenme notunu sunar
- Her inceleme sonunda `.claude/reports/` altına **Türkçe rapor** kaydeder

**Yasaklı fonksiyonları işaretler:** `gets()`, `strcpy()`, `sprintf()`, `scanf("%s", ...)`

---

### Pyra — Python Kod İnceleme Ajanı

> *15+ yıllık Python deneyimiyle, PEP 8 ve idiomatic Python'u içselleştirmiş kıdemli bir mühendis.*

**Ne zaman çalışır:**
- Bir `.py` dosyası yazıldığında ya da değiştirildiğinde
- Python kodu paylaşıldığında veya hata ayıklama istendiğinde

**Ne yapar:**
- `py_compile`, `ruff` ve `mypy` ile **statik analiz** yapar; çıktıları olduğu gibi raporlar
- Mutable default argument, bare `except:`, `eval()` kullanımı gibi **kritik hataları** yakalar
- Context manager eksikliği, `range(len(x))` yerine `enumerate`, gereksiz global değişken gibi **kötü pratikleri** işaretler
- Type hint, f-string, list comprehension gibi **Pythonic iyileştirmeleri** önerir
- Safety, Kod Kalitesi ve Okunabilirlik için **10 üzerinden puanlar verir**
- Düzeltilmiş kodu ve öğrenme notunu sunar
- Her inceleme sonunda `.claude/reports/` altına **Türkçe rapor** kaydeder (`py_` önekiyle)

**Yasaklı patternleri işaretler:** `eval(user_input)`, bare `except:`, `open()` without `with`, `os.system()`, `from module import *`

---

## Raporlar

Her ajan inceleme sonunda otomatik olarak ilgili alt klasöre Türkçe rapor kaydeder.

| Kaynak Dosya | Rapor Yolu |
|---|---|
| `CS50/Lecture-1/main.c` | `.claude/reports/c/lecture-1_main.md` |
| `LeetCode Solutions/With Python/Two Sum/main.py` | `.claude/reports/python/py_leetcode_two-sum.md` |

---

## Teknolojiler

| Alan | Araç |
|---|---|
| Dil (C) | C99/C11, clang (macOS arm64) |
| Dil (Python) | Python 3.12+ |
| C Linting | clang -Wall -Wextra -fsanitize=address,undefined |
| Python Linting | ruff, mypy, py_compile |
| AI Kod İnceleme | Claude Sonnet (Rex + Pyra agents) |
