## **06: Functional Testing with WebTest**
Menambahkan *functional test* menggunakan **WebTest** untuk mensimulasikan HTTP request nyata ke aplikasi Pyramid.

**Analisis:**
Functional test mensimulasikan interaksi nyata antara pengguna dan aplikasi (layaknya browser).
Menggunakan WebTest, kita bisa mengirim request ke server Pyramid dan memeriksa response lengkap (status code, body, headers).

Perbedaannya dari unit test:
- Unit test → logika internal fungsi
- Functional test → perilaku aplikasi secara utuh.

Tahap ini memastikan aplikasi berfungsi dari perspektif pengguna.