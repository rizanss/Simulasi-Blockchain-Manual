# Simulasi Blockchain Manual

Ini adalah simulasi sederhana blockchain menggunakan Python. Project ini dibuat untuk memahami konsep dasar blockchain, seperti blok, hash, dan validasi rantai.

## Fitur
- Menambahkan blok baru ke dalam blockchain.
- Memvalidasi keaslian blockchain.
- Menampilkan informasi setiap blok dalam blockchain.

## Cara Menggunakan
1. Clone repository ini.
2. Install Python (jika belum ada).
3. Jalankan file `blockchain.py` untuk melihat cara kerja blockchain.

## Struktur File
- `blockchain.py`: Kode utama untuk membuat dan mengelola blockchain.

## Contoh Output
Saat menjalankan simulasi, kamu akan melihat output seperti berikut:

Index: 0
Previous Hash: 0
Data: Genesis Block
Timestamp: 1739785869.0481796
Hash: 8dc4d4e186a124d78c52ba830f76ba5b076b056cc02efd2987f6d4837e3e02fd

Index: 1
Previous Hash: 8dc4d4e186a124d78c52ba830f76ba5b076b056cc02efd2987f6d4837e3e02fd
Data: Transaksi 1: Alice kirim 10 BTC ke Bob
Timestamp: 1739785869.0483334
Hash: 794d4295175a931e2dcbc8f8410e4c4085511becc62cbf6973385c2a70cb5212

Index: 2
Previous Hash: 794d4295175a931e2dcbc8f8410e4c4085511becc62cbf6973385c2a70cb5212
Data: Transaksi 2: Bob kirim 5 BTC ke Charlie
Timestamp: 1739785869.0483804
Hash: 827415b1f0a8c07e86f064c463b373ac1f56852359f870c5e5ff880b9e9ee716

Blockchain Valid? True
