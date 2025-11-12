## **05: Unit Tests and pytest**
Mengenalkan pengujian unit menggunakan **pytest**. View diuji untuk memastikan data yang dikembalikan sesuai dengan yang diharapkan.

**Analisis:**
Langkah ini memperkenalkan testing unit menggunakan pytest dan integrasi dengan Pyramid.
Unit test fokus pada logika kecil (fungsi/view tertentu) tanpa menjalankan seluruh server.

Kita menggunakan:
- testing.DummyRequest() untuk mensimulasikan request. 
- unittest atau pytest untuk memeriksa output view.

Tujuan: memastikan setiap komponen berfungsi benar secara terisolasi.
Testing dini membuat kode lebih stabil dan mudah dipelihara.