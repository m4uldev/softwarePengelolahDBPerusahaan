### 🏬 Aplikasi Pengelola Data Barang dan Pembuatan Database/Tabel di MySQL

Program ini terdiri dari dua bagian utama: pembuatan database dan tabel di MySQL serta aplikasi pengelola data barang menggunakan antarmuka grafis PyQt5. Berikut adalah penjelasan singkat mengenai program ini:

- **Pembuatan Database dan Tabel di MySQL**:
  - Program ini bertanggung jawab untuk membuat database baru dan tabel yang diperlukan di server MySQL.
  - Pengguna diminta untuk memasukkan informasi seperti host, nama pengguna, kata sandi, dan nama database melalui input.
  - Informasi yang diberikan oleh pengguna disimpan ke dalam file `data.log`.
  - Setelah mendapatkan informasi yang diperlukan, program membuat database baru dan tabel `db_produk` dengan kolom-kolom yang sesuai di server MySQL yang ditentukan.

- **Aplikasi Pengelola Data Barang**:
  - Aplikasi ini memungkinkan pengguna untuk menambah, mengedit, dan menghapus data barang melalui antarmuka grafis yang mudah digunakan. 🛍️
  - Informasi server MySQL (seperti host, user, password, dan nama database) dibaca dari file `data.log`. 🔍
  - Setelah mendapatkan informasi server, aplikasi mencoba untuk terhubung ke server MySQL dan mengambil semua data barang dari tabel `db_produk`. 📊
  - Validasi dilakukan untuk memastikan bahwa input yang dimasukkan oleh pengguna sesuai dengan yang diharapkan. ✅
  - Aplikasi memberi tahu pengguna tentang hasil operasi yang dilakukan menggunakan pesan peringatan sederhana. 📢

### 🌐 Aplikasi Web Pengelola Data Barang

Selain itu, terdapat aplikasi web sederhana yang memungkinkan pengguna untuk mencari dan melihat detail barang menggunakan input pencarian. Berikut adalah penjelasan singkat mengenai aplikasi web ini:

- **Aplikasi Web Pengelola Data Barang**:
  - Aplikasi web ini memungkinkan pengguna untuk mencari nama barang yang diinginkan menggunakan input pencarian.
  - Data barang yang sesuai dengan kriteria pencarian ditampilkan dalam bentuk kotak-kotak yang menampilkan detail barang seperti harga, stok, dan deskripsi.
  - Pengguna juga dapat melihat jumlah data yang sesuai dengan kriteria pencarian di bagian bawah halaman.

Dengan demikian, kedua program ini memberikan berbagai cara bagi pengguna untuk mengelola dan mengakses data barang, baik melalui antarmuka grafis yang disediakan oleh aplikasi PyQt5 maupun melalui antarmuka web yang sederhana. 🚀
