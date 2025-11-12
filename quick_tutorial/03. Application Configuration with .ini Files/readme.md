## **03: Application Configuration with .ini Files**
Konfigurasi aplikasi dipindahkan ke file `.ini` menggunakan format PasteDeploy. File ini mengatur pengaturan server, logging, dan pengaturan aplikasi Pyramid.

**Analisis:**
Pyramid memanfaatkan file konfigurasi .ini (seperti development.ini) untuk mengatur aplikasi tanpa perlu mengubah kode.

File .ini memuat:
- Informasi server (waitress, port).
- Pengaturan Pyramid (pyramid.reload_templates, logging, debug toolbar, dll.).
- Opsi tambahan seperti environment variables dan pengaturan database.

Keuntungan: konfigurasi dan kode dipisahkan.
Hal ini memudahkan pengaturan production dan development environment dengan file konfigurasi berbeda.