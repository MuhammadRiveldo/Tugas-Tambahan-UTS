## **20: Logins with Authentication**
Menambahkan sistem login menggunakan cookie berbasis **AuthTktCookieHelper**.

**Analisis:**
- Memperkenalkan konsep **authentication** (menentukan siapa user-nya).
- Menggunakan `bcrypt` untuk hashing password dengan aman.
- Menambahkan view login/logout dengan form sederhana.
- Session cookie digunakan untuk melacak identitas pengguna.

Tahap ini menambahkan fitur login dan logout menggunakan AuthTktCookieHelper.
Autentikasi dilakukan dengan hashing password (bcrypt) dan penyimpanan state di cookie.

Fitur utama:
- Login dengan username dan password.
- Logout yang menghapus cookie.
- @view_config(route_name='login') untuk form login.

Autentikasi ini adalah dasar keamanan sebelum menambahkan authorization.
