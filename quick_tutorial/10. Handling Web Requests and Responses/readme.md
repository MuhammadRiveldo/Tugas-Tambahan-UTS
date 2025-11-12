## **10: Handling Web Requests and Responses**
Mempelajari cara menangani objek request dan response menggunakan WebOb.

**Analisis:**
- Pyramid menggunakan WebOb untuk request/response.
- Dapat mengambil parameter URL dan query string dengan mudah.
- Menunjukkan bagaimana membuat redirect (`HTTPFound`) dan respon plain text.

Tahap ini menjelaskan bagaimana Pyramid memproses request HTTP:

1. User mengakses URL.
2. Request dikirim ke Pyramid.
3. Router mencari view sesuai route
4. View mengembalikan response.

Kita juga belajar menggunakan pyramid.response.Response untuk mengontrol output manual — cocok untuk REST API atau AJAX endpoint