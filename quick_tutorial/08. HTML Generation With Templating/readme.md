## **08: HTML Generation With Templating**
Menambahkan templating engine (Chameleon) untuk menghasilkan HTML dari template eksternal.

**Analisis:**
- Memisahkan logic dan tampilan (presentation layer).
- Pyramid mendukung berbagai template engine (Chameleon, Jinja2, Mako).
- Testing menjadi lebih mudah karena view hanya mengembalikan data.

Di tahap ini, kita menggunakan template engine (seperti Chameleon) untuk menghasilkan HTML dari data Python.
Template memisahkan logic (Python) dari presentation (HTML), meningkatkan keterbacaan dan pemeliharaan.

Pyramid mendukung berbagai template engine: Chameleon, Jinja2, Mako, dsb.
Kita juga mempelajari bagaimana variabel Python disisipkan ke HTML (${name}, ${value}).