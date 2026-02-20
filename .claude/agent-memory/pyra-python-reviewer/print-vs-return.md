# Konu: print() vs return — Tekrar Eden Risk

**Ilk gorulen:** 2026-02-20, Two Sum cozumu

## Problem
Ogrenci fonksiyon sonucunu `print()` ile ekrana yaziyor, `return` ile cagirana geri gondermek yerine.

```python
# Ogrencinin yazdigi (yanlis):
def twoSum(nums, target):
    if needed in my_dict:
        print([my_dict[needed], i])  # deger kaybolur
        break
    return  # None doner
```

## Neden Kritik
- LeetCode her zaman `return` degerini test eder, stdout'u degil
- `None` donen fonksiyon hicbir test case'i gecemez
- Mypy da bunu yakaliyor: `Return value expected [return-value]`

## Dogru Form
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    if needed in seen:
        return [seen[needed], i]  # cagirana geri ver
    return []
```

## Analoji Kullanildi
"Asistan belgeyi okuyup icerigini soyledi ama kagidi geri vermedi."
Bir sonraki seansda bu analoji isledi mi takip et.

## Izleme
- Seans 1: hata mevcut
- Seans 2+: duzeltildi mi?
