## **17: Transient Data Using Sessions**
Membuat sesi pengguna menggunakan `SignedCookieSessionFactory` untuk menyimpan data sementara.

**Analisis:**
- Session berfungsi menyimpan data non-permanen seperti counter, login state.
- Data disimpan di cookie dengan tanda tangan digital (secure).
- Menjadi dasar untuk fitur user-based interaction (misalnya shopping cart).

Tahap ini memperkenalkan session — data sementara yang disimpan antara request, seperti shopping cart atau user counter.

Pyramid menyediakan SignedCookieSessionFactory untuk menyimpan session secara aman di cookie.
Data bisa diakses melalui request.session.