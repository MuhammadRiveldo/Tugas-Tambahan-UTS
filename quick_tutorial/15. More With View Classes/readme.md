## **15: More With View Classes**
Mendemonstrasikan pemanfaatan `@view_defaults`, `@property`, dan method POST pada class-based view.

**Analisis:**
- Satu kelas bisa menangani berbagai aksi (GET, POST, DELETE).
- Menunjukkan konsep *predicate dispatching* berdasarkan method/parameter.
- Kode menjadi lebih rapi dan mudah di-maintain.

Langkah ini memperdalam penggunaan view class — memisahkan berbagai metode (GET, POST, dll) dalam satu class.

Kelebihannya:
- Dapat menyimpan state request.
- Mudah diperluas (inheritance antar class).

Digunakan untuk aplikasi kompleks dengan banyak endpoint terkait satu resource