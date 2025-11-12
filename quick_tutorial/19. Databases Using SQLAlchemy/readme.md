## **19: Databases Using SQLAlchemy**
Menghubungkan aplikasi ke database SQLite menggunakan **SQLAlchemy ORM**.

**Analisis:**
- Data disimpan secara permanen dalam database.
- ORM mengubah tabel menjadi objek Python.
- Integrasi dengan `pyramid_tm` dan `zope.sqlalchemy` untuk manajemen transaksi otomatis.
- Disertai script inisialisasi database (`initialize_tutorial_db`).

Langkah ini menambahkan SQLAlchemy ORM dan SQLite sebagai penyimpanan data.
Kita belajar membuat model (Page), menginisialisasi DB, serta melakukan operasi CRUD.

Konsep penting:
- Base dan DBSession untuk ORM binding.
- Integrasi pyramid_tm dan zope.sqlalchemy untuk transaksi otomatis.
- Console script initialize_tutorial_db untuk setup database.

Hasilnya: aplikasi Pyramid kini berbasis database dengan ORM modern.