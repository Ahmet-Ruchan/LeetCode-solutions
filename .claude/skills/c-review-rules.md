# C Code Review Kuralları

## SEVİYE 1 — KRİTİK (Kod çalışmaz veya güvensiz)
- [ ] malloc/calloc dönüş değeri NULL kontrolü yapılmamış
- [ ] free() sonrası pointer NULL'a set edilmemiş (dangling pointer)
- [ ] Buffer sınır kontrolü yok (gets, strcpy kullanımı yasak)
- [ ] Uninitialized variable kullanımı
- [ ] Integer overflow riski olan aritmetik

## SEVİYE 2 — UYARI (Çalışır ama kötü pratik)
- [ ] Fonksiyon 40 satırdan uzun
- [ ] Magic number kullanımı (#define veya const kullanılmalı)
- [ ] Global değişken gereksiz kullanımı
- [ ] Tek harfli değişken adı (loop dışında)
- [ ] Yorum satırı hiç yok veya anlamsız
- [ ] typedef kullanılmadan struct tag ile çalışma

## SEVİYE 3 — ÖNERİ (Style ve okunabilirlik)
- [ ] Camel case yerine snake_case kullanılmalı
- [ ] Fonksiyon adı fiil ile başlamalı (get_, set_, calc_, is_)
- [ ] Header guard eksik (.h dosyalarında)
- [ ] const kullanılabilecek yerde kullanılmamış

## YASAKLI FONKSİYONLAR
gets(), sprintf() (snprintf kullan), strcpy() (strncpy kullan), scanf("%s") 

## ZORUNLU PRATİKLER
- Her .h dosyasında include guard
- main() dönüş tipi int olmalı
- Tüm switch-case'lerde default olmalı
```

---

### 3. Agent'ı Tetikleme

Kodunu Claude Code'a şöyle verebilirsin:
```
/agent c-reviewer

Şu kodu review et:
[kodun buraya]
```

Ya da agent'a doğrudan dosya yolu verebilirsin:
```
/agent c-reviewer main.c dosyamı incele