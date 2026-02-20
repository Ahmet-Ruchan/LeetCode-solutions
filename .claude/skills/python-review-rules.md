# Python Kod İnceleme Kuralları
# Pyra tarafından her review'da bu dosya okunur ve kurallar uygulanır.
# Bu dosyadaki kurallar Pyra'nın varsayılan kurallarından önce gelir.

---

## SEVİYE 1 — KRİTİK (Kod çalışmaz, güvensiz veya crash üretir)

- [ ] Mutable default argument kullanımı: `def f(x=[])` veya `def f(data={})` — her çağrıda aynı nesne paylaşılır
- [ ] Bare `except:` — `KeyboardInterrupt`, `SystemExit` dahil her şeyi yutar, hiçbir zaman kullanılmaz
- [ ] `eval()` veya `exec()` kullanıcı girdisiyle kullanılıyor
- [ ] Dosya/network işlemlerinde exception handling hiç yok — program çöker
- [ ] SQL sorgusu string format ile oluşturuluyor: `f"SELECT * FROM users WHERE id={user_id}"` → SQL injection
- [ ] `os.system(user_input)` veya `subprocess.call(shell=True, args=user_input)` → shell injection
- [ ] Hardcoded credentials: şifre, API key, token doğrudan kodda yazılmış

---

## SEVİYE 2 — UYARI (Çalışır ama hata üretmeye aday)

- [ ] `except Exception as e: pass` — hata sessizce yutulmuş, debug edilemez
- [ ] `with` kullanmadan dosya açmak: `f = open(...)` → kaynak sızıntısı
- [ ] Iterate ederken listeyi değiştirmek: `for item in my_list: my_list.remove(item)`
- [ ] `== None`, `== True`, `== False` karşılaştırması — `is None`, `is True`, `is False` kullanılmalı
- [ ] `global` keyword olmadan global değişkeni fonksiyon içinde modify etmek
- [ ] Fonksiyon 30 satırdan uzun — parçalanmalı
- [ ] Runnable script'te `if __name__ == "__main__":` guard yok
- [ ] `range(len(x))` kullanımı — `enumerate(x)` kullanılmalı
- [ ] Loop içinde string birleştirme: `result += str` → `"".join()` kullanılmalı
- [ ] Standart kütüphane yerine elle yazılmış: `itertools`, `collections`, `pathlib` zaten bunu yapıyor

---

## SEVİYE 3 — ÖNERİ (Okunabilirlik ve Pythonic stil)

- [ ] List/dict/set comprehension kullanılabilecek yerde `for` loop var
- [ ] Type hint eksik: `def hesapla(x, y):` yerine `def hesapla(x: int, y: int) -> int:`
- [ ] Public fonksiyon veya class'ta docstring yok
- [ ] Magic number: `if status == 3:` yerine `if status == STATUS_ACTIVE:` gibi sabit kullanılmalı
- [ ] `type(x) == int` yerine `isinstance(x, int)` kullanılmalı
- [ ] f-string yerine eski `%s` veya `.format()` kullanımı (Python 3.6+ için f-string tercih edilir)
- [ ] Tek harfli değişken adı (döngü index `i`, `j` dışında)
- [ ] Gereksiz `else` after `return`: `if x: return True \n else: return False`

---

## İSİMLENDİRME KURALLARI (Zorunlu)

```
değişken / fonksiyon    →  snake_case         (örn: user_count, calculate_total)
class                   →  PascalCase          (örn: UserManager, DataProcessor)
sabit                   →  UPPER_SNAKE_CASE    (örn: MAX_RETRY_COUNT, BASE_URL)
private method/attr     →  _single_underscore  (örn: _validate, _cache)
name mangling           →  __double_underscore sadece gerektiğinde
```

---

## YASAKLI PATTERN'LAR (Her kullanım KRİTİK sayılır)

| Yasaklı | Zorunlu Alternatif |
|---|---|
| `eval(user_input)` | Asla eval'a kullanıcı girdisi verilmez |
| `except:` bare | `except Exception as e:` minimum |
| `open(f)` without `with` | `with open(f) as fh:` |
| `os.system(cmd)` | `subprocess.run([...], check=True)` |
| `type(x) == SomeType` | `isinstance(x, SomeType)` |
| `import *` | Explicit import: `from module import func` |

---

## ZORUNLU PRATİKLER

- Her runnable `.py` dosyasında `if __name__ == "__main__":` bloğu olmalı
- Kaynak yönetimi (dosya, bağlantı, kilit) her zaman `with` bloğuyla yapılmalı
- Exception yakalarken mutlaka loglama veya anlamlı bir hata mesajı olmalı
- Public API fonksiyonlarında type hint zorunlu
- `requirements.txt` veya `pyproject.toml` varsa import edilen kütüphaneler orada tanımlı olmalı

---

## PYTHON VERSİYON NOTU

Bu proje Python 3.12+ hedefliyor (macOS Apple Silicon). Buna göre:
- `match/case` (structural pattern matching) kullanılabilir
- `tomllib` built-in olarak mevcut
- `typing` modülünden `Optional`, `Union` yerine `X | Y` syntax tercih edilir
- `asyncio.run()` doğrudan kullanılabilir