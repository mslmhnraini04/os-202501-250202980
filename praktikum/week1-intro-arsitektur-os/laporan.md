
# Laporan Praktikum Minggu [X]
Topik: Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Muslimah Nuraini
- **NIM**   : 250202980
- **Kelas** : 1IKRB

---

## Tujuan
Praktikum ini bertujuan agar dapat memahami peran sistem operasi sebagai penghubung antara pengguna dan perangkat keras, serta mengenal fungsi kernel dan system call dalam mengatur dan menjalankan perintah di sistem operasi.

---

## Dasar Teori
1. Kernel adalah bagian utama sistem operasi yang mengatur jalannya proses, memori, dan perangkat keras.
2. Arsitektur kernel dibagi jadi beberapa jenis, yaitu monolithic, microkernel, dan hybrid.
3. Setiap arsitektur punya kelebihan dan kekurangan, tergantung kebutuhan sistem yang digunakan.

---

## Langkah Praktikum
1. Setup Environment
Pastikan Linux (Ubuntu/WSL) sudah terinstal.
Pastikan Git sudah dikonfigurasi dengan benar:
git config --global user.name "Nama Anda"
git config --global user.email "email@contoh.com"
2. Diskusi Konsep
Baca materi pengantar tentang komponen OS.
Identifikasi komponen yang ada pada Linux/Windows/Android.
Eksperimen Dasar Jalankan perintah berikut di terminal:
uname -a
whoami
lsmod | head
dmesg | head
Catat dan analisis modul kernel yang tampil.
3. Membuat Diagram Arsitektur
Buat diagram hubungan antara User → System Call → Kernel → Hardware.
Gunakan draw.io atau Mermaid.
Simpan hasilnya di:
praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
4. Penulisan Laporan
Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam laporan.md.
Tambahkan screenshot hasil terminal ke folder screenshots/.
5. Commit & Push
git add .
git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a = muslimahnuraini2007@cloudshell:~$ uname -a
lsmod | head = muslimahnuraini2007@cloudshell:~$ lsmod | head
dmesg | head = muslimahnuraini2007@cloudshell:~$ sudo dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![alt text](<screenshots/Diagram Arsitektur.drawio.png>)
![alt text](<code/Eksperimen Dasar.png>)


---

## Analisis
- Makna hasil percobaan
Percobaan menunjukkan bahwa kernel berperan penting dalam mengatur komunikasi antara perangkat keras dan perangkat lunak melalui system call.
- Hubungkan hasil dengan teori
Hasil ini sesuai dengan teori bahwa kernel adalah inti sistem operasi yang mengatur proses dan sumber daya, sedangkan system call jadi penghubung antara user dan kernel sesuai arsitektur OS-nya.
-Perbedaan Linux vs Windows
Di Linux prosesnya lebih terbuka dan bisa dipantau melalui terminal, sedangkan di Windows lebih tertutup dan berbasis GUI. Keduanya sama-sama memakai system call tapi cara kerjanya berbeda sesuai desain sistemnya.  

---

## Kesimpulan
1. Kernel adalah inti dari sistem operasi yang mengatur seluruh aktivitas komputer, termasuk manajemen memori, proses, dan perangkat keras.
2. Arsitektur sistem operasi menentukan bagaimana kernel dan komponen lain saling berinteraksi, seperti pada model monolithic, microkernel, dan layered architecture.
3. Pemilihan arsitektur kernel sangat berpengaruh terhadap kinerja, keamanan, dan kemudahan pengembangan sistem. Misalnya, monolithic kernel cenderung lebih cepat tapi sulit diperbarui, sedangkan microkernel lebih aman dan mudah dikembangkan karena setiap komponennya terpisah.
---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi
   **Jawaban:**
   1. Mengatur proses agar semua program dapat berjalan barsama tanpa bertabrakan.
   2. Mengatur memori supaya setiap aplikasi memiliki ruang tersendiri.
   3. Mengatur perangkat keras seperti keyboard, printer, dan lain-lain agar bisa menyambung ke sistem.
2. Jelaskan perbedaan antara kernel mode dan user mode.
   **Jawaban:**
   Kernel mode: Sistem punya akses penuh ke semua bagian komputer, kayak otak utama yang ngatur semuanya.
   User mode: Mode buat aplikasi biasa, aksesnya terbatas supaya kalau ada error, gak bikin seluruh sistem rusak.
4. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
   **Jawaban:**
   Monolithic kernel: Linux, MS-DOS, UNIX tradisional.
   Microkernel: macOS (berbasis XNU, kombinasi dengan microkernel Mach), QNX, dan Minix.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  1. Mengunduh aplikasi gitHub, karena laptop kurang mendukung
  2. Membuat diagram arsitektur, karena tidak dapat di screenshot
  3. Commit & push
- Bagaimana cara Anda mengatasinya?
  1. uprade laptop ke spek yang lebih mendukung
  2. dengan di download kemudian di foto menggunakan handphone sebagai buktinya
  3. dikerjakan secara bertahap dengan jangka waktu beberapa hari 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
