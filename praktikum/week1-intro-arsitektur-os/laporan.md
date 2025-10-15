
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
  - uname -a Artinya, sistem operasi ini berbasis Linux modern yang sudah dioptimasi agar stabil dan cepat.
  
  - whoami artinya menunjukkan nama user yang sedang aktif. Ini membuktikan bahwa sistem operasi bisa mengenali dan membedakan setiap pengguna yang login.
  
  - lsmod artinya menampilkan daftar modul tambahan kernel yang sedang aktif dalam system.
  
  - dmesg artinya menunjukkan bahwa kernel bekerja dengan baik dalam mengatur dan mengenali perangkat keras. Jadi, percobaan ini membuktikan bahwa kernel merupakan bagian penting dari sistem operasi yang mengatur komunikasi antara hardware dan software sejak sistem pertama kali aktif.
 
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).

  - uname -a nunjukin versi kernel dan jenis sistem yang dipakai. Ini berhubungan dengan arsitektur OS, karena kita bisa mengetahui sistem ini menggunakan Linux 64-bit dan semua komponennya bekerjasama dari user, system call, sampai kernel.
    
  - whoami menunjukkan siapa user yang sedang aktif. Ini berhubungan dengan system call, karena waktu menjalankan perintah itu, sistem meminta info dari kernel melalui system call untuk tahu identitas user.
  
  - lsmod menampilkan daftar modul yang sedang aktif di kernel. Ini sesuai dengan fungsi kernel, yang bisa menambah atau melepas modul sesuai kebutuhan. Jadi kernel itu seperti pengatur utama yang mengatur semua “fitur tambahan” agar sistem tetap efisien.
  
  - dmesg menampilkan log dari kernel saat sistem menyala. Dari sini kita tahu bahwa kernel mengatur dan mengenali perangkat keras seperti CPU, RAM, atau jaringan agar semuanya siap untuk dipakai.
    
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?

  Di Linux prosesnya lebih terbuka dan bisa dipantau melalui terminal, sedangkan di Windows lebih tertutup dan berbasis GUI. Keduanya sama-sama memakai system call tapi cara kerjanya berbeda sesuai desain sistemnya.

---

## Kesimpulan
1. Kernel adalah inti dari sistem operasi yang mengatur seluruh aktivitas komputer, termasuk manajemen memori, proses, dan perangkat keras.
2. Arsitektur sistem operasi menentukan bagaimana kernel dan komponen lain saling berinteraksi, seperti pada model monolithic, microkernel, dan layered architecture.
3. Pemilihan arsitektur kernel sangat berpengaruh terhadap kinerja, keamanan, dan kemudahan pengembangan sistem. Misalnya, monolithic kernel cenderung lebih cepat tapi sulit diperbarui, sedangkan microkernel lebih aman dan mudah dikembangkan karena setiap komponennya terpisah.
---

## TUGAS
Ringkasan (±500 kata). 
1. Dalam dunia sistem operasi, kernel memegang peran sentral sebagai jembatan yang menghubungkan perangkat keras dan perangkat lunak. Tugas utamanya adalah mengoptimalkan pemanfaatan sumber daya komputer oleh berbagai aplikasi. Tanpa kehadiran kernel, mustahil bagi sistem operasi untuk mengoordinasi komunikasi antarkomponen atau mengeksekusi perintah dari pengguna. Secara arsitektur, kernel umumnya dikategorikan menjadi tiga jenis yaitu monolithic kernel, microkernel, dan layered architecture. Meski fungsinya sama, ketiganya menerapkan pendekatan organisasi komponen dan mekanisme kerja yang berbeda.
   
   •	Pada monolithic kernel, seluruh layanan inti sistem operasi seperti manajemen memori, sistem file, penjadwalan proses, dan driver perangkat keras disatukan dalam satu ruang kernel yang besar. Integrasi penuh ini menghasilkan kinerja yang sangat cepat karena komunikasi internal berlangsung tanpa hambatan. Sayangnya, desain ini rentan terhadap masalah keamanan dan stabilitas. Satu saja komponen mengandung bug atau rusak, seluruh sistem dapat mengalami kegagalan total. Kerumitan dalam memperbarui atau memperbaiki sistem juga menjadi kelemahan utamanya.
   
   •	Sebaliknya, microkernel menganut filosofi minimalis dan modular. Hanya fungsi-fungsi paling fundamental, seperti komunikasi antarproses (IPC) dan penjadwalan proses dasar, yang ditempatkan di dalam kernel. Layanan lain seperti driver dan sistem file dioperasikan di luar kernel, sebagai proses independen. Pendekatan ini menjadikan sistem lebih stabil dan aman; kegagalan pada satu modul tidak akan menjatuhkan seluruh sistem. Kelemahannya, kinerja sistem sedikit lebih lambat akibat mekanisme pertukaran pesan yang diperlukan untuk komunikasi antarmodul.
   
   •	Sementara itu, arsitektur berlapis (layered architecture) menyusun sistem operasi dalam lapisan-lapisan hierarkis. Lapisan terbawah berurusan langsung dengan hardware, sedangkan lapisan teratas berinteraksi dengan pengguna. Setiap lapisan hanya dapat berkomunikasi dengan lapisan yang bertetangga, baik di atas maupun di bawahnya, sehingga menciptakan alur kerja yang sangat terstruktur. Keunggulan model ini terletak pada kemudahan pemeliharaan, sebab modifikasi pada satu lapisan tidak akan mengganggu lapisan lain. Yang menjadi trade-off adalah penurunan efisiensi, karena setiap permintaan harus melalui banyak lapisan sebelum diproses.
   
2. Sebagai ilustrasi, sistem operasi seperti Linux dan UNIX adalah contoh monolithic kernel. QNX dan kernel Mach (yang menjadi dasar macOS) mewakili microkernel. Adapun sistem seperti THE OS dan MULTICS menerapkan arsitektur berlapis.

3. Dalam konteks sistem modern, microkernel sering dianggap sebagai pilihan yang paling relevan. Desain modularnya mendukung pengembangan dan pemeliharaan 
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
