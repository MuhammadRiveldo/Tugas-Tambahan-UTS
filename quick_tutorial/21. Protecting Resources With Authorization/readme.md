## **21: Protecting Resources With Authorization**
Menambahkan **authorization** untuk membatasi aksi berdasarkan peran dan izin (permission).

**Analisis:**
- Menambahkan ACL (Access Control List) pada root resource.
- Membedakan user berdasarkan grup dan role (`group:editors`).
- View tertentu membutuhkan permission seperti `permission='edit'`.
- Menangani akses tidak sah dengan `@forbidden_view_config`.
- Menggabungkan konsep Authentication + Authorization = Secure Access Control.

Langkah terakhir memperkenalkan authorization — menentukan siapa yang boleh melakukan apa.

Konsep penting:
- Root memiliki ACL (__acl__) yang menentukan izin.
- SecurityPolicy menilai effective_principals pengguna.
- permission='edit' pada view mengatur siapa yang bisa mengakses.