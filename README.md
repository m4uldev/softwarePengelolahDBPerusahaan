### Aplikasi Pengelola Data Barang dan Pembuatan Database/Tabel di MySQL

Program ini adalah sebuah aplikasi Python yang menggunakan antarmuka grafis PyQt5 untuk mengelola data barang dalam sebuah perusahaan dan untuk membuat database serta tabel yang diperlukan di MySQL. Berikut adalah penjelasan singkat mengenai program ini:

- **Aplikasi Pengelola Data Barang**:
  - Aplikasi ini memungkinkan pengguna untuk menambah, mengedit, dan menghapus data barang melalui antarmuka grafis yang mudah digunakan.
  - Informasi server MySQL (seperti host, user, password, dan nama database) dibaca dari file `data.log`.
  - Setelah mendapatkan informasi server, aplikasi mencoba untuk terhubung ke server MySQL dan mengambil semua data barang dari tabel `db_produk`.
  - Validasi dilakukan untuk memastikan bahwa input yang dimasukkan oleh pengguna sesuai dengan yang diharapkan.
  - Aplikasi memberi tahu pengguna tentang hasil operasi yang dilakukan menggunakan pesan peringatan sederhana.

- **Pembuatan Database dan Tabel di MySQL**:
  - Program ini bertanggung jawab untuk membuat database baru dan tabel yang diperlukan di server MySQL.
  - Pengguna diminta untuk memasukkan informasi seperti host, nama pengguna, kata sandi, dan nama database melalui input.
  - Informasi yang diberikan oleh pengguna disimpan ke dalam file `data.log`.
  - Setelah mendapatkan informasi yang diperlukan, program membuat database baru dan tabel `db_produk` dengan kolom-kolom yang sesuai di server MySQL yang ditentukan.

Dengan demikian, program ini memungkinkan pengguna untuk mengelola data barang melalui antarmuka grafis yang disediakan, sambil juga menyediakan fitur untuk membuat database dan tabel yang diperlukan di MySQL.
