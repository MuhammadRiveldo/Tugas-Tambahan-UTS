## **12: Templating With jinja2**
Mengganti templating engine menjadi **Jinja2** yang lebih populer dan fleksibel.

**Analisis:**
- Pyramid mendukung multi-template system.
- Instalasi `pyramid_jinja2` menambahkan renderer otomatis untuk `.jinja2` files.
- Memperlihatkan fleksibilitas Pyramid terhadap berbagai template library.

Langkah ini mengganti Chameleon dengan Jinja2, template engine populer (juga digunakan di Flask dan Django).
Keunggulannya:
- Sintaks mirip Python.
- Dukungan inheritance template.
- Fitur filters dan loops.

Kita mempelajari integrasi Jinja2 melalui config.include('pyramid_jinja2').