# Pyra Kod Inceleme Raporu

**Dosya:** LeetCode Solutions/With Python/Two Sum/two_sum.py
**Tarih:** 2026-02-20

## Skorlar
| Kategori | Skor |
|---|---|
| Guvenlik | 7/10 |
| Kod Kalitesi | 3/10 |
| Okunabilirlik | 5/10 |

## Genel Ozet
Algoritmanin temeli dogru kurulmus; hash map (dictionary) ile O(n) cozum yaklasimi LeetCode Two Sum icin en iyi pratik yontemdir ve bu dogru secilmis. Ancak fonksiyon bir deger dondurmek yerine `print()` kullaniyor, bu LeetCode ortaminda hicbir zaman gecmez. Ek olarak `if __name__ == "__main__":` guard eksik, fonksiyon adi Python isimlendirme kurallarina (snake_case) aykiri, ve `range(len())` yerine `enumerate()` kullanilmali.

## Statik Analiz Sonucu

### py_compile
```
py_compile: OK (syntax hatasi yok)
```

### pylint (0.00/10)
```
/tmp/two_sum_review.py:5:0: C0303: Trailing whitespace (trailing-whitespace)
/tmp/two_sum_review.py:8:0: C0303: Trailing whitespace (trailing-whitespace)
/tmp/two_sum_review.py:10:0: C0303: Trailing whitespace (trailing-whitespace)
/tmp/two_sum_review.py:12:0: C0303: Trailing whitespace (trailing-whitespace)
/tmp/two_sum_review.py:18:0: C0303: Trailing whitespace (trailing-whitespace)
/tmp/two_sum_review.py:22:0: C0303: Trailing whitespace (trailing-whitespace)
/tmp/two_sum_review.py:23:0: C0304: Final newline missing (missing-final-newline)
/tmp/two_sum_review.py:1:0: C0114: Missing module docstring (missing-module-docstring)
/tmp/two_sum_review.py:2:0: C0103: Constant name "target" doesn't conform to UPPER_CASE naming style (invalid-name)
/tmp/two_sum_review.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
/tmp/two_sum_review.py:4:0: C0103: Function name "twoSum" doesn't conform to snake_case naming style (invalid-name)
/tmp/two_sum_review.py:4:11: W0621: Redefining name 'nums' from outer scope (line 1) (redefined-outer-name)
/tmp/two_sum_review.py:4:23: W0621: Redefining name 'target' from outer scope (line 2) (redefined-outer-name)
/tmp/two_sum_review.py:9:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
/tmp/two_sum_review.py:13:8: R1723: Unnecessary "else" after "break", remove the "else" and de-indent the code inside it (no-else-break)
/tmp/two_sum_review.py:4:0: R1711: Useless return at end of function or method (useless-return)
-----------------------------------
Your code has been rated at 0.00/10
```

### mypy
```
/tmp/two_sum_review.py:7: error: Need type annotation for "my_dict" (hint: "my_dict: dict[<type>, <type>] = ...")  [var-annotated]
/tmp/two_sum_review.py:19: error: Return value expected  [return-value]
Found 2 errors in 1 file (checked 1 source file)
```

## Kritik Hatalar

### 1 — Fonksiyon Deger Dondurmunyor (Usulsuz `return` ve `print`)

**Ne yanlis:** Fonksiyon imzasi `-> list` diye tanimlaniyor ama icinde `return` bos birakilmis. Sonuc ekrana `print()` ile yaziliyor. LeetCode her zaman `return` degerini degerlendirir; `print()` ciktiyi gormez, test hep basarisiz olur.

**Neden onemli:** Bu hatayla hicbir test case gecmez. `None` donan bir fonksiyon, beklenen `[int, int]` listesini karsilamaz.

**Duzeltme:**
```python
# ONCE (yanlis):
def twoSum(nums: list, target: int) -> list:
    ...
    if needed in my_dict:
        print([my_dict[needed], i])   # sadece ekrana yazar, deger dondurmez
        break
    ...
    return   # None doner

# SONRA (dogru):
def two_sum(nums: list[int], target: int) -> list[int]:
    ...
    if needed in seen:
        return [seen[needed], i]   # degeri geri dondur
    ...
    return []   # eslesmeme durumu icin guveli fallback
```

### 2 — `if __name__ == "__main__":` Guard Eksik (Ozel Kural — UYARI seviyesine yukseldi)

**Ne yanlis:** Fonksiyon cagrilari modül seviyesinde bekle duruyor. Baska bir dosya bu modulu `import` ederse `twoSum(nums, target)` satiri otomatik calisir.

**Neden onemli:** Bu ozel kural dosyasinda (`python-review-rules.md`) SEVİYE 2 olarak listelenmistir ve tum runnable script'ler icin zorunludur.

**Duzeltme:**
```python
# ONCE (yanlis):
twoSum(nums, target)

# SONRA (dogru):
if __name__ == "__main__":
    result = two_sum(NUMS, TARGET)
    print(result)
```

## Uyarilar

### 1 — `range(len(nums))` yerine `enumerate` kullanilmali

**Ne yanlis:** `for i in range(len(nums))` ve ardindan `nums[i]` indeksleme — hem gereksiz hem de Pythonic degil.

**Duzeltme:**
```python
# ONCE:
for i in range(len(nums)):
    needed = target - nums[i]

# SONRA:
for i, num in enumerate(nums):
    needed = target - num
```

### 2 — Gereksiz `else` after `break`

**Ne yanlis:** `if ... break / else:` yapisi — `else` blogu her zaman `break` olmadigi durumda calisir; bu Python'da gecerlidir ama okunabilirlik acisindan kafa karisikligina yol acar ve pylint uyari uretir.

**Duzeltme:**
```python
# ONCE:
if needed in my_dict:
    return [my_dict[needed], i]
else:
    my_dict[nums[i]] = i

# SONRA (else'i kaldir, de-indent et):
if needed in seen:
    return [seen[needed], i]
my_dict[nums[i]] = i
```

### 3 — `needed = 0` Gereksiz Baslangic Atamasi

**Ne yanlis:** `needed = 0` ile baslangic degeri ataniyor ama bu degisken loop'un ilk iterasyonunda her seferinde uzerine yaziliyor. Anlamsiz bir atama.

**Duzeltme:**
```python
# ONCE:
needed = 0
for i in range(len(nums)):
    needed = target - nums[i]

# SONRA:
for i, num in enumerate(nums):
    needed = target - num
```

### 4 — Dis Kapsamdaki Degiskenler Fonksiyon Parametreleriyle Golgeleniyor (Shadow)

**Ne yanlis:** `nums` ve `target` hem modül seviyesinde hem de fonksiyon parametresi olarak tanimlanmis. Pylint bunu `W0621: redefined-outer-name` olarak isaretler. Bu dogrudan bir hata degil ama kafa karistirici.

**Duzeltme:** Modül seviyesindeki degiskenleri `UPPER_SNAKE_CASE` ile sabit olarak adlandir; bu hem golgeleme sorununu cozer hem de Python isimlendirme kuralina uyar.

```python
# ONCE:
nums = [2, 4, 5]
target = 7

# SONRA:
NUMS = [2, 4, 5]
TARGET = 7
```

## Oneriler

### 1 — Fonksiyon Adi snake_case Olmali

**Ne yanlis:** `twoSum` camelCase — Java/C konvansiyonu. Python'da `two_sum` olmali (PEP 8).

```python
# ONCE:
def twoSum(...)

# SONRA:
def two_sum(...)
```

### 2 — Type Hint'ler Daha Kesin Olmali

**Ne yanlis:** `list` yerine `list[int]` — Python 3.9+ ve ozellikle 3.12+ icin generic type hint kullanilmali.

```python
# ONCE:
def twoSum(nums: list, target: int) -> list:

# SONRA:
def two_sum(nums: list[int], target: int) -> list[int]:
```

### 3 — Degisken Adi `my_dict` Anlamli Degil

**Ne yanlis:** `my_dict` ne sakladigini anlatmiyor. `seen` veya `num_to_index` daha aciklayici.

```python
# ONCE:
my_dict = {}
my_dict[nums[i]] = i

# SONRA:
seen: dict[int, int] = {}
seen[num] = i
```

### 4 — Docstring Eksik

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given a list of integers and a target, return indices of the two numbers
    that add up to the target. Assumes exactly one solution exists.

    Time complexity: O(n)
    Space complexity: O(n)
    """
```

## Duzeltilmis Kod

```python
"""Two Sum — LeetCode #1 (hash map yaklasimiyla O(n) cozum)."""

# Modül seviyesi sabitler UPPER_SNAKE_CASE ile isimlendirilir
NUMS = [2, 4, 5]
TARGET = 7


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given a list of integers and a target, return indices of the two numbers
    that add up to the target. Assumes exactly one solution exists.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    seen: dict[int, int] = {}  # sayi -> indeks eslestirmesi

    for i, num in enumerate(nums):          # range(len()) yerine enumerate
        needed = target - num               # baslangic atamasi gereksizdi

        if needed in seen:
            return [seen[needed], i]        # print yerine return — LeetCode bunu bekler

        seen[num] = i                       # else gereksiz; break yoksa zaten devam eder

    return []                               # eslesen cift bulunamazsa bos liste donder


if __name__ == "__main__":                  # modül dogrudan calistirildiginda test et
    result = two_sum(NUMS, TARGET)
    print(result)                           # cikti: [1, 2]
```

## Bugunun Dersi

En onemli ders: **`print()` bir cevap degildir; `return` bir cevaptir.**

Bir fonksiyon her zaman sonucunu cagirana geri vermelidir. `print()`, sonucu terminale yazar ve yok eder — cagiran kod onu bir degiskene atayamaz, test edemez, baska fonksiyona gonderemez.

Analoji: Bir asistan sana bir belgeyi okuyup icerigini soyler ama elindeki kagidi geri vermez. Belgeyi aldiktan sonra yapabilecegin hicbir sey kalmaz. `return`, o kagidi geri uzatmaktir.

LeetCode'da `print()` kullanan her cozum, her test case icin `None` dondurur ve hic gecmez.

## Ilerleme Notu

Bu, bu ogrencinin ilk incelenen Python dosyasidir. Sonraki oturumlarda bu puanlar baz alinacak ve trend takip edilecektir.

- Baslangic skorlari: Guvenlik 7/10 | Kod Kalitesi 3/10 | Okunabilirlik 5/10
- En kritik sorun: Fonksiyonun deger dondurmemesi — algoritma dogru, arayuz yanlis
- Dikkat edilmesi gereken tekrar eden riskler: `range(len())` kullanimi, eksik `__main__` guard, camelCase isimlendirme
- Algoritma secimi (hash map, O(n)) gercekten iyi — bu pozitif bir baslangic noktasi
