
## **14: AJAX Development With JSON Renderers**
Membuat endpoint JSON untuk mendukung komunikasi AJAX dari front-end.

**Analisis:**
- Pyramid menyediakan renderer bawaan untuk JSON.
- View bisa menghasilkan JSON hanya dengan `renderer='json'`.
- Cocok untuk API dan SPA (Single Page Application).

Langkah ini memperkenalkan cara membuat endpoint JSON API menggunakan renderer='json'.
View dapat mengembalikan dictionary Python yang otomatis dikonversi ke JSON.

Kegunaan:
- AJAX frontend.
- API komunikasi antar sistem.