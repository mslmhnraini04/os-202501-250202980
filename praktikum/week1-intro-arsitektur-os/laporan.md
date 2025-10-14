
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
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

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
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
