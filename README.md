# HASIL RUNNING

## Pertemuan 2

(Praktikum 1)
<img width="1920" height="1080" alt="Praktikum1" src="https://github.com/user-attachments/assets/3bda67ae-baa9-4dac-a623-c7ca9c4ca306" />
(Praktikum 2)
<img width="1920" height="1080" alt="Praktikum2" src="https://github.com/user-attachments/assets/507fa15a-c302-447e-98ff-ecbc851796e7" />
(Praktikum 3)
<img width="1920" height="1080" alt="Praktikum3" src="https://github.com/user-attachments/assets/3dc69088-a5ba-495e-931b-26995d4a8a81" />
(Praktikum 4)
<img width="1920" height="1080" alt="Praktikum4" src="https://github.com/user-attachments/assets/004b9fa8-4dee-48f7-a020-0d7bb9a9d8e3" />
(Praktikum 5)
<img width="1920" height="1080" alt="Praktikum5" src="https://github.com/user-attachments/assets/72fc7d1f-7dc6-48be-9070-5b025c681602" />


## Pertemuan 3

(Praktikum Koordinat 1)
<img width="1920" height="1080" alt="PraktikumKoordinat1" src="https://github.com/user-attachments/assets/92073516-bf72-455e-9d31-337281ede003" />
(Praktikum Koordinat 2)
<img width="1920" height="1080" alt="PraktikumKoordinat2" src="https://github.com/user-attachments/assets/d26b5e71-a3a7-4c1b-837b-49bd5a4d97ef" />
(Praktikum Koordinat 3)
<img width="1920" height="1080" alt="PraktikumKoordinat3" src="https://github.com/user-attachments/assets/00bdc6ed-fc83-4cb5-8c40-a505185ab9e2" />
(Praktikum Gambar 1)
<img width="1920" height="1080" alt="PraktikumGambar1" src="https://github.com/user-attachments/assets/e613d67f-b870-4962-bfe7-14eb34b6018a" />
(Praktikum Gambar 2)
<img width="1920" height="1080" alt="PraktikumGambar2" src="https://github.com/user-attachments/assets/f37e9e50-f0ad-4e80-8582-cab7aa0aec2a" />


## Pertemuan 5

(Garis)
<img width="1920" height="1080" alt="Garis" src="https://github.com/user-attachments/assets/3742b432-83c6-4dbe-be21-a0906531c8c4" />
(Lingkaran)
<img width="1920" height="1080" alt="Lingkaran" src="https://github.com/user-attachments/assets/cbce24e8-80f5-4499-91a8-16052ace7e39" />
(Polygon)
<img width="1920" height="1080" alt="Pentagon" src="https://github.com/user-attachments/assets/92da8440-7667-4759-ab7d-edf9a57af1d0" />


## UTS
### Aplikasi Rumah 2D

Aplikasi desktop interaktif untuk mendemonstrasikan konsep dasar grafika komputer menggunakan Python dan Tkinter. Program ini menampilkan gambar rumah 2D lengkap dengan berbagai transformasi geometris.

Aplikasi ini dibuat sebagai implementasi pembelajaran grafika komputer yang mencakup:
- Algoritma gambar garis Bresenham
- Algoritma gambar lingkaran Midpoint Circle
- Transformasi geometris 2D (translasi, rotasi, dan scaling)
- Rendering objek 2D kompleks

#### Visualisasi Rumah 2D
Menampilkan gambar rumah lengkap dengan elemen-elemen:
- Badan rumah dengan atap merah
- Pintu dengan gagang
- Jendela dengan bingkai
- Cerobong asap dengan efek asap
- Pagar kiri dan kanan
- Pohon dengan daun bulat
- Matahari dengan sinar
- Awan
- Bunga-bunga dekoratif
- Jalan dan rumput

#### Transformasi Geometris
| Tombol | Fungsi | Deskripsi |
|--------|--------|-----------|
| 🏠 Gambar Rumah | Render | Menggambar ulang rumah dengan transformasi saat ini |
| ➡️ Translasi | Pergeseran | Menggeser posisi rumah (+40px horizontal, +30px vertikal) |
| 🔄 Rotasi | Rotasi | Memutar rumah sebesar 15° searah jarum jam |
| 🔼 Skala + | Pembesaran | Memperbesar ukuran rumah sebesar 115% |
| 🔽 Skala - | Pengecilan | Memperkecil ukuran rumah sebesar 85% |
| 🔄 Reset | Reset | Mengembalikan rumah ke posisi dan ukuran awal |

#### Algoritma yang Digunakan

1. Algoritma Bresenham Line
   Digunakan untuk menggambar garis lurus dengan efisien menggunakan operasi integer. Algoritma ini menghitung piksel-piksel
   yang paling mendekati garis ideal antara dua titik.
2. Algoritma Midpoint Circle
   Digunakan untuk menggambar lingkaran dengan memanfaatkan simetri 8 oktan. Algoritma ini menghitung titik-titik lingkaran     berdasarkan persamaan lingkaran dan decision parameter.
3. Transformasi Geometris 2D
   a. Translasi
   Menggeser objek ke posisi baru dengan menambahkan offset pada koordinat x dan y:
   ```
   x' = x + tx
   y' = y + ty
   ```
   b. Rotasi
   Memutar objek terhadap titik pusat (400, 300) dengan sudut θ:
   ```
   x' = x * cos(θ) - y * sin(θ)
   y' = x * sin(θ) + y * cos(θ)
   ```
   c. Scaling
   Mengubah ukuran objek dengan faktor skala:
   ```
   x' = x * sx
   y' = y * sy
   ```

   #### Hasil Running

   (Tampilan Awal)
   <img width="1920" height="1080" alt="Normal" src="https://github.com/user-attachments/assets/08e63a37-3673-468b-b241-       550eacb20b8f" />
   (Translasi)
   <img width="1920" height="1080" alt="Transisi" src="https://github.com/user-attachments/assets/602307ee-0bb3-4869-af67-     53604bf1fb09" />
   (Rotasi)
   <img width="1920" height="1080" alt="Rotasi" src="https://github.com/user-attachments/assets/f788f653-dadf-4afc-aa4b-       776a02373101" />
   (Skala Plus)
   <img width="1920" height="1080" alt="SkalaPlus" src="https://github.com/user-attachments/assets/068d4d7a-3055-4fb6-8fcc-    238816889840" />
   (Skala Minus)
   <img width="1920" height="1080" alt="SkalaMinus" src="https://github.com/user-attachments/assets/5964dc7d-1edd-4551-9806-24e3bcb8933e" />
