# Pyramid Web Framework Tutorial

Nama: Muhammad Riveldo Hermawan Putra \
NIM: 122140037 \
Mata Kuliah: Pengembangan Aplikasi Web RB \
Pertemuan 9 - Pemrograman Python \
Tugas Tambahan Nilai UTS 

---

## **01: Single-File Web Applications**
Pada tahap ini, kita membuat aplikasi web sederhana hanya dengan satu file Python. Pyramid digunakan untuk menangani request dan response HTTP dasar. Langkah ini memperkenalkan konsep WSGI dan bagaimana Pyramid dapat dijalankan langsung dengan `pserve`.

**Analisis:**
- Cocok untuk pemahaman dasar arsitektur Pyramid.
- Belum modular, semua logika masih dalam satu file.
- Ideal untuk tahap eksplorasi dan prototyping.

---

## **02: Python Packages for Pyramid Applications**
Aplikasi dipecah menjadi paket Python agar lebih terstruktur dan mudah dikembangkan. Setiap bagian aplikasi (views, routes, templates) disusun dalam direktori khusus.

**Analisis:**
- Meningkatkan modularitas aplikasi.
- Memudahkan maintenance dan distribusi melalui `setuptools`.
- Struktur proyek mulai menyerupai aplikasi produksi nyata.

---

## **03: Application Configuration with .ini Files**
Konfigurasi aplikasi dipindahkan ke file `.ini` menggunakan format PasteDeploy. File ini mengatur pengaturan server, logging, dan pengaturan aplikasi Pyramid.

**Analisis:**
- Memisahkan konfigurasi dari kode.
- Mempermudah pengelolaan environment (development, production).
- Menggunakan `pserve` untuk menjalankan aplikasi dengan konfigurasi yang fleksibel.

---

## **04: Easier Development with debugtoolbar**
Menambahkan **Pyramid Debug Toolbar** untuk membantu debugging dan inspeksi request, routes, serta konfigurasi aplikasi secara langsung di browser.

**Analisis:**
- Memudahkan developer melacak error.
- Menampilkan informasi lengkap tentang request, template, dan SQL.
- Hanya digunakan di mode pengembangan (development mode).

---

## **05: Unit Tests and pytest**
Mengenalkan pengujian unit menggunakan **pytest**. View diuji untuk memastikan data yang dikembalikan sesuai dengan yang diharapkan.

**Analisis:**
- Mengajarkan pentingnya *test-driven development*.
- Unit test memastikan stabilitas fungsi view.
- Pyramid menyediakan integrasi mudah dengan `pyramid.testing`.

---

## **06: Functional Testing with WebTest**
Menambahkan *functional test* menggunakan **WebTest** untuk mensimulasikan HTTP request nyata ke aplikasi Pyramid.

**Analisis:**
- Menguji aplikasi dari sisi pengguna (end-to-end).
- Membantu memastikan view, routes, dan template terhubung dengan benar.
- Meningkatkan keandalan aplikasi.

---

## **07: Basic Web Handling With Views**
Memperkenalkan konsep view dan route di Pyramid. Setiap URL dipetakan ke fungsi view tertentu.

**Analisis:**
- Menjelaskan hubungan antara URL dan fungsi view.
- Memberikan pondasi konsep MVC di Pyramid.
- View berperan sebagai penghubung antara request dan response.

---

## **08: HTML Generation With Templating**
Menambahkan templating engine (Chameleon) untuk menghasilkan HTML dari template eksternal.

**Analisis:**
- Memisahkan logic dan tampilan (presentation layer).
- Pyramid mendukung berbagai template engine (Chameleon, Jinja2, Mako).
- Testing menjadi lebih mudah karena view hanya mengembalikan data.

---

## **09: Organizing Views With View Classes**
View diubah menjadi metode dalam satu kelas (class-based views), memungkinkan berbagi konfigurasi dan state antar view.

**Analisis:**
- Memudahkan pengelompokan view yang berkaitan.
- Mendukung prinsip OOP untuk reusabilitas kode.
- Menggunakan `@view_defaults` untuk konfigurasi bersama.

---

## **10: Handling Web Requests and Responses**
Mempelajari cara menangani objek request dan response menggunakan WebOb.

**Analisis:**
- Pyramid menggunakan WebOb untuk request/response.
- Dapat mengambil parameter URL dan query string dengan mudah.
- Menunjukkan bagaimana membuat redirect (`HTTPFound`) dan respon plain text.

---

## **11: Dispatching URLs To Views With Routing**
Menambahkan parameter dinamis pada URL dan mengaksesnya melalui `request.matchdict`.

**Analisis:**
- Memperkenalkan *replacement patterns* dalam routes.
- Mendukung dynamic routing seperti `/user/{id}`.
- Meningkatkan fleksibilitas dalam desain URL.

---

## **12: Templating With jinja2**
Mengganti templating engine menjadi **Jinja2** yang lebih populer dan fleksibel.

**Analisis:**
- Pyramid mendukung multi-template system.
- Instalasi `pyramid_jinja2` menambahkan renderer otomatis untuk `.jinja2` files.
- Memperlihatkan fleksibilitas Pyramid terhadap berbagai template library.

---

## **13: CSS/JS/Images Files With Static Assets**
Menambahkan direktori `static/` untuk menyimpan file seperti CSS, JS, dan gambar.

**Analisis:**
- `config.add_static_view()` memetakan folder statis ke URL tertentu.
- Menggunakan `request.static_url()` agar link file dinamis.
- Mendukung arsitektur aplikasi dengan front-end resources.

---

## **14: AJAX Development With JSON Renderers**
Membuat endpoint JSON untuk mendukung komunikasi AJAX dari front-end.

**Analisis:**
- Pyramid menyediakan renderer bawaan untuk JSON.
- View bisa menghasilkan JSON hanya dengan `renderer='json'`.
- Cocok untuk API dan SPA (Single Page Application).

---

## **15: More With View Classes**
Mendemonstrasikan pemanfaatan `@view_defaults`, `@property`, dan method POST pada class-based view.

**Analisis:**
- Satu kelas bisa menangani berbagai aksi (GET, POST, DELETE).
- Menunjukkan konsep *predicate dispatching* berdasarkan method/parameter.
- Kode menjadi lebih rapi dan mudah di-maintain.

---

## **16: Collecting Application Info With Logging**
Menambahkan sistem logging standar Python untuk debugging dan monitoring.

**Analisis:**
- Menggunakan konfigurasi logging di `development.ini`.
- Memudahkan pelacakan error dan alur eksekusi.
- Logging disimpan di konsol atau file tergantung konfigurasi.

---

## **17: Transient Data Using Sessions**
Membuat sesi pengguna menggunakan `SignedCookieSessionFactory` untuk menyimpan data sementara.

**Analisis:**
- Session berfungsi menyimpan data non-permanen seperti counter, login state.
- Data disimpan di cookie dengan tanda tangan digital (secure).
- Menjadi dasar untuk fitur user-based interaction (misalnya shopping cart).

---

## **18: Forms and Validation with Deform**
Mengenalkan **Deform** dan **Colander** untuk membuat form otomatis dengan validasi schema-driven.

**Analisis:**
- Membuat form dinamis dengan validasi otomatis.
- Menunjukkan integrasi Pyramid dengan pustaka eksternal.
- Deform menyediakan widget interaktif (RichText, Select, dsb.).

---

## **19: Databases Using SQLAlchemy**
Menghubungkan aplikasi ke database SQLite menggunakan **SQLAlchemy ORM**.

**Analisis:**
- Data disimpan secara permanen dalam database.
- ORM mengubah tabel menjadi objek Python.
- Integrasi dengan `pyramid_tm` dan `zope.sqlalchemy` untuk manajemen transaksi otomatis.
- Disertai script inisialisasi database (`initialize_tutorial_db`).

---

## **20: Logins with Authentication**
Menambahkan sistem login menggunakan cookie berbasis **AuthTktCookieHelper**.

**Analisis:**
- Memperkenalkan konsep **authentication** (menentukan siapa user-nya).
- Menggunakan `bcrypt` untuk hashing password dengan aman.
- Menambahkan view login/logout dengan form sederhana.
- Session cookie digunakan untuk melacak identitas pengguna.

---

## **21: Protecting Resources With Authorization**
Menambahkan **authorization** untuk membatasi aksi berdasarkan peran dan izin (permission).

**Analisis:**
- Menambahkan ACL (Access Control List) pada root resource.
- Membedakan user berdasarkan grup dan role (`group:editors`).
- View tertentu membutuhkan permission seperti `permission='edit'`.
- Menangani akses tidak sah dengan `@forbidden_view_config`.
- Menggabungkan konsep Authentication + Authorization = Secure Access Control.

---

## ✅ **Kesimpulan Akhir**
Dari langkah 01 hingga 21, aplikasi berkembang dari:
- Single-file demo → Modular package
- Static HTML → Dynamic Templating
- Dummy data → Database SQLAlchemy
- Tanpa keamanan → Login dan Authorization penuh

Pyramid menyediakan arsitektur fleksibel, scalable, dan Pythonic untuk membangun aplikasi web profesional dengan pendekatan *explicit is better than implicit*. 🚀

