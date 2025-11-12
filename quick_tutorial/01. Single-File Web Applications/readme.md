## **01: Single-File Web Applications**
Pada tahap ini, kita membuat aplikasi web sederhana hanya dengan satu file Python. Pyramid digunakan untuk menangani request dan response HTTP dasar. Langkah ini memperkenalkan konsep WSGI dan bagaimana Pyramid dapat dijalankan langsung dengan `pserve`.

**Analisis:**
Langkah pertama memperkenalkan konsep dasar single-file application di Pyramid.
Di sini, aplikasi web sepenuhnya ditulis dalam satu file Python (biasanya __init__.py atau app.py) untuk memahami alur minimal aplikasi Pyramid tanpa struktur folder kompleks.

Pyramid memungkinkan developer membuat aplikasi web dengan cepat menggunakan Configurator untuk mengatur routes, views, dan renderers.
Langkah ini menyoroti konsep inti:
- Routing: Menghubungkan URL dengan fungsi Python.
- View Callables: Fungsi yang menangani permintaan (request) dan mengembalikan respons.
- Response Object: Output yang dikirim kembali ke browser.
- Server bawaan: Menggunakan pserve untuk menjalankan aplikasi.

Dengan langkah ini, kita memahami dasar arsitektur Pyramid — ringan, modular, dan mudah dikembangkan lebih lanjut.