## **11: Dispatching URLs To Views With Routing**
Menambahkan parameter dinamis pada URL dan mengaksesnya melalui `request.matchdict`.

**Analisis:**
- Memperkenalkan *replacement patterns* dalam routes.
- Mendukung dynamic routing seperti `/user/{id}`.
- Meningkatkan fleksibilitas dalam desain URL.

Routing adalah mekanisme yang menghubungkan URL dengan view.
Dengan config.add_route('name', '/path'), kita mendefinisikan rute aplikasi.

Pyramid mendukung:
- Static routes (/home)
- Dynamic routes (/items/{id})

Rute membuat aplikasi modular dan URL menjadi intuitif.