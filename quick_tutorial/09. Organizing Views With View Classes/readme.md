## **09: Organizing Views With View Classes**
View diubah menjadi metode dalam satu kelas (class-based views), memungkinkan berbagi konfigurasi dan state antar view.

**Analisis:**
- Memudahkan pengelompokan view yang berkaitan.
- Mendukung prinsip OOP untuk reusabilitas kode.
- Menggunakan `@view_defaults` untuk konfigurasi bersama.

Pyramid mendukung class-based views untuk mengorganisir logika dalam bentuk objek.
Setiap method dalam class mewakili satu endpoint.

Keuntungannya:
- Reusabilitas tinggi.
- Dapat berbagi state antar-view (misal, request, session).
- Lebih rapi untuk proyek besar.

Kita menggunakan @view_defaults dan @view_config untuk mengatur renderer dan route.