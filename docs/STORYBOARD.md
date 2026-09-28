# Storyboard Media Interaktif: "Petualangan Energi Bersama Si Volta"

**Mata pelajaran:** IPAS, Kelas IV SD (Fase B)
**Topik:** Mengubah Bentuk Energi
**Alokasi waktu:** 2 × 35 menit
**Sasaran:** siswa usia 9-10 tahun dengan gaya belajar visual dan kinestetik
**Platform yang disarankan:** Genially, Canva Interaktif, PowerPoint dengan trigger, atau Articulate. Media bisa dijalankan di laptop, tablet, atau layar sentuh.

> Aplikasi Python pada repositori ini (`app.py`) mengimplementasikan sebagian rancangan ini. Lihat bagian *Rencana Pengembangan* di README.

## A. Konsep Dasar

**Tujuan pembelajaran** (setelah menggunakan media, siswa dapat):
1. Menyebutkan bentuk-bentuk energi: listrik, cahaya, panas, gerak, bunyi, dan kimia.
2. Menjelaskan perubahan bentuk energi pada lampu, setrika, kipas angin, radio, dan senter.
3. Mencatat energi awal dan energi akhir dari hasil pengamatan.
4. Menyusun peta konsep perubahan bentuk energi.

**Tokoh pemandu:** *Si Volta*, robot kecil berbentuk baterai dengan mata besar dan antena lampu. Ia bicara ramah dengan kalimat pendek.

**Prinsip desain untuk visual dan kinestetik:**
- Warna kode tetap di seluruh media: 🟡 cahaya, 🔴 panas, 🔵 gerak, 🟣 bunyi, ⚡ listrik (putih-biru), 🟢 kimia.
- Teks pendek, maksimal 2 kalimat per layar, dengan ikon besar dan tombol minimal 1,5 cm untuk jari anak.
- Setiap layar menuntut minimal satu aksi: klik, geser, seret, atau putar.
- Narasi suara opsional dengan tombol 🔊, supaya siswa yang lambat membaca tetap terbantu.
- Umpan balik selalu positif, misalnya "Hampir! Coba lagi ya!".

## B. Peta Navigasi

```
[1] COVER / SPLASH
        ↓
[2] PETUNJUK & TUJUAN BELAJAR
        ↓
[3] APERSEPSI (video senter + pertanyaan pemantik)
        ↓
[4] MENU UTAMA (hub) ◄────────────────────────┐
     │                                        │
     ├─► [5] EKSPLORASI MATERI                │
     │      ├ 5a Lampu   5b Setrika           │
     │      ├ 5c Kipas   5d Radio             │
     │      └ 5e Senter (kimia→listrik→cahaya)│
     │      └► [5f] Ringkasan "Rantai Energi" ├─ kembali ke menu
     │                                        │
     ├─► [6] SIMULASI PENYELIDIKAN (LKM)      │
     │      ├ 6a Misi & prosedur              │
     │      ├ 6b Lab: Senter                  │
     │      ├ 6c Lab: Kipas Angin             │
     │      ├ 6d Lab: Setrika                 │
     │      └ 6e Kesimpulan penyelidikan ─────┤
     │                                        │
     ├─► [7] EVALUASI: DRAG & DROP PETA KONSEP│
     │      └► Skor & bintang ────────────────┘
     │
     └─► [8] REFLEKSI ─► [9] PENUTUP
```

**Aturan navigasi:** menu Evaluasi (7) terkunci sampai siswa membuka minimal Eksplorasi dan Simulasi. Tombol tetap di setiap layar: 🏠 Menu, ◀ Kembali, ▶ Lanjut, 🔊 Suara, ❓ Bantuan.

## C. Alur Waktu (2 × 35 menit)

| Pertemuan | Bagian | Durasi |
|---|---|---|
| **1** | Cover, petunjuk, apersepsi (layar 1-3) | 7 menit |
| | Eksplorasi Materi (layar 4-5) | 15 menit |
| | Simulasi: misi dan Lab Senter (layar 6a-6b) | 13 menit |
| **2** | Simulasi: Lab Kipas dan Setrika, kesimpulan (6c-6e) | 15 menit |
| | Evaluasi drag-and-drop (layar 7) | 12 menit |
| | Refleksi dan penutup (layar 8-9) | 8 menit |

## D. Storyboard Per Layar

### Layar 1: Cover
| Elemen | Rancangan |
|---|---|
| **Visual** | Latar langit malam dengan lampu-lampu kota. Si Volta melayang, dengan judul besar "Petualangan Energi". |
| **Audio** | Musik ceria pendek dan suara Si Volta: "Halo, Penjelajah Energi!" |
| **Interaksi** | Tombol **MULAI** berkedip. Siswa mengetik nama pada kolom "Namaku". |
| **Navigasi** | ▶ Layar 2 |

### Layar 2: Petunjuk dan Tujuan
| Elemen | Rancangan |
|---|---|
| **Visual** | Empat ikon besar yang mewakili empat misi: 🎬 Tonton, 🔍 Jelajahi, 🧪 Selidiki, 🎮 Main. Tombol legenda menjelaskan fungsi setiap tombol. |
| **Teks** | "Hari ini kamu akan menjadi Penyelidik Energi! Kamu akan belajar bagaimana energi bisa berubah bentuk." |
| **Interaksi** | Klik tiap ikon untuk memunculkan penjelasan singkat. Tujuan belajar ditampilkan sebagai 3 "lencana" yang akan dikumpulkan. |
| **Navigasi** | ▶ Layar 3 |

### Layar 3: Apersepsi
| Elemen | Rancangan |
|---|---|
| **Visual** | Video/animasi 30-45 detik. Seorang anak masuk ke kamar gelap saat listrik padam, mengambil senter, memasukkan baterai, menggeser tombol, lalu senter menyala. Tampak dekat: baterai, kabel kecil, lampu senter. |
| **Audio** | Efek klik, dengung kecil, dan musik lembut. Tidak ada narasi selama video, supaya siswa fokus mengamati. |
| **Interaksi** | Setelah video, muncul pertanyaan pemantik: **"Dari mana energi cahaya pada senter berasal?"** Siswa memilih atau menyeret jawaban awal ke kotak "Dugaanku": 🔋 Baterai / 🌞 Matahari / 💡 Lampunya sendiri / ❓ Belum tahu. Semua jawaban diterima, karena ini hanya dugaan awal. |
| **Umpan balik** | Si Volta: "Menarik dugaanmu! Kita buktikan nanti ya." |
| **Catatan guru** | Diskusikan 2-3 menit secara klasikal dan catat dugaan siswa untuk dibandingkan di akhir. |
| **Navigasi** | ▶ Layar 4 (Menu Utama) |

### Layar 4: Menu Utama (Hub)
| Elemen | Rancangan |
|---|---|
| **Visual** | Peta pulau petualangan dengan 4 lokasi: 🏝 Pulau Jelajah (Eksplorasi), 🧪 Lab Penyelidik (Simulasi), 🎯 Arena Peta Konsep (Evaluasi, tergembok 🔒), 🪞 Cermin Refleksi. |
| **Interaksi** | Klik lokasi untuk berpindah. Bilah kemajuan berbentuk baterai yang terisi sesuai misi yang selesai. Lencana muncul di sudut layar. |
| **Navigasi** | Bercabang ke layar 5, 6, 7, 8 |

### Layar 5: Eksplorasi Materi

**5 (layar pembuka).** Lima kartu alat: Lampu, Setrika, Kipas Angin, Radio, Senter. Siswa mengklik kartu mana saja. Kartu yang sudah dibuka diberi tanda ✔.

**Pola tetap untuk layar 5a-5e:**
- *Bagian kiri:* gambar alat besar dan hidup (ilustrasi vektor).
- *Bagian tengah:* diagram panah perubahan energi, dengan ikon berwarna sesuai kode warna.
- *Bagian kanan:* satu kalimat penjelasan dan satu fakta unik.
- *Aksi kinestetik:* siswa **menekan tombol ON**, lalu animasi memperlihatkan aliran energi bergerak sepanjang panah.

| Layar | Alat | Perubahan Energi | Animasi Utama | Fakta Unik / Tugas Kecil |
|---|---|---|---|---|
| 5a | 💡 Lampu | Listrik ⚡ → Cahaya 🟡 | Lampu menyala, sinar menyebar ke sekitar | "Lampu juga menghasilkan sedikit panas. Coba sentuh lampu yang baru dimatikan (hati-hati!) di rumah bersama orang tua." Di media, siswa cukup menggeser slider "jarak tangan" untuk melihat indikator hangat. |
| 5b | ♨️ Setrika | Listrik ⚡ → Panas 🔴 | Bagian bawah setrika berubah dari abu menjadi merah-oranye, uap naik | Slider suhu: makin tinggi, makin merah. Peringatan visual: "Setrika hanya boleh disentuh orang dewasa!" |
| 5c | 🌀 Kipas Angin | Listrik ⚡ → Gerak 🔵 | Baling-baling berputar, garis angin muncul, kecepatan bisa diatur | Siswa memilih kecepatan 1, 2, atau 3 dan melihat pita kertas bergerak lebih kencang. |
| 5d | 📻 Radio | Listrik ⚡ → Bunyi 🟣 | Gelombang bunyi berbentuk lingkaran keluar dari speaker | Geser tombol volume: gelombang makin lebar. Klik saluran untuk mendengar cuplikan musik anak. |
| 5e | 🔦 Senter | Kimia 🟢 → Listrik ⚡ → Cahaya 🟡 | Tiga tahap berurutan: baterai bercahaya hijau, kilatan listrik di kabel, lampu menyala | Ini adalah **perubahan berantai (dua tahap)**. Si Volta: "Jadi baterai menyimpan energi kimia, lalu jadi listrik, lalu jadi cahaya!" Kembali ke dugaan awal di layar 3. |

**5f: Ringkasan Rantai Energi.** Tabel visual lima baris yang otomatis terisi dari kartu yang sudah dibuka. Siswa menekan tombol "Aku paham!" untuk mendapat Lencana 1 🥇 dan kembali ke Menu Utama.

### Layar 6: Simulasi Penyelidikan (Adaptasi LKM)

**6a: Misi dan Prosedur**
| Elemen | Rancangan |
|---|---|
| **Visual** | Papan "Surat Misi": "Selidiki apa yang terjadi saat alat dihidupkan!" |
| **Isi (adaptasi LKM)** | *Pertanyaan penyelidikan:* Apa yang berubah ketika alat dihidupkan? *Langkah:* ① Amati kondisi awal, ② Hidupkan alat, ③ Amati kondisi akhir, ④ Catat bentuk energinya. |
| **Interaksi** | Siswa mengeklik 4 langkah untuk melihat contoh pada ikon. |
| **Navigasi** | ▶ Menu Lab dengan 3 pintu: Senter, Kipas, Setrika |

**Pola tetap untuk layar 6b-6d (Lab Virtual)**

Layar dibagi tiga kolom: **SEBELUM | TOMBOL | SESUDAH**.

1. **SEBELUM:** alat dalam keadaan mati. Siswa mengamati dan memilih kata yang menggambarkan kondisi awal, misalnya "gelap / diam / dingin".
2. **Tombol ON/OFF** yang bisa diklik.
3. **SESUDAH:** alat menyala atau bekerja. Siswa mengamati dan memilih kata kondisi akhir.
4. **Kotak Catatan Penyelidik** (adaptasi tabel LKM):

| Alat | Kondisi Awal | Kondisi Akhir | Energi Awal | Energi Akhir |
|---|---|---|---|---|
| Diisi siswa lewat drag/dropdown | | | | |

| Layar | Alat | Aksi Kinestetik | Kondisi Awal → Akhir | Jawaban yang Diharapkan |
|---|---|---|---|---|
| 6b | 🔦 Senter | Klik untuk memasang baterai (seret ke tempatnya), lalu geser tombol ON | Gelap → terang | Energi kimia (baterai) → listrik → cahaya |
| 6c | 🌀 Kipas Angin | Tekan tombol ON, ubah kecepatan | Diam → berputar, terasa angin | Listrik → gerak |
| 6d | ♨️ Setrika | Tekan ON, lihat termometer virtual naik | Dingin (25°C) → panas (misal 120°C), kain kusut menjadi rata | Listrik → panas |

**Fitur pendukung untuk semua Lab:**
- Tombol 🔁 *Ulangi* agar siswa boleh mengulang percobaan.
- Si Volta mengajukan satu pertanyaan tantangan, misalnya "Apakah kipas juga jadi hangat? Coba rasakan!" Ini melatih pengamatan yang lebih cermat.
- Peringatan keselamatan di Lab Setrika: "Di kehidupan nyata, jangan menyentuh setrika. Ini hanya simulasi!"
- Setelah catatan lengkap dan benar, muncul stempel ✅ dan siswa mendapat Lencana 2 🥈.

**6e: Kesimpulan Penyelidikan**
Siswa melengkapi kalimat dengan pilihan kata: *"Ketika alat dihidupkan, energi ______ berubah menjadi energi ______."* Lalu muncul tabel gabungan tiga percobaan. Bagian ini juga berfungsi sebagai jembatan untuk menjawab kembali pertanyaan pemantik: **"Dari mana energi cahaya senter berasal?"** Jawaban: *dari energi kimia pada baterai.*

### Layar 7: Evaluasi Formatif (Drag-and-Drop Peta Konsep)

| Elemen | Rancangan |
|---|---|
| **Judul** | "Arena Peta Konsep: Lengkapi Rantai Energi!" |
| **Visual** | Peta konsep dengan simpul pusat **"Energi Listrik ⚡"** yang bercabang ke kotak-kotak kosong. Di bagian bawah tersedia "gudang kartu" berwarna. |
| **Aksi** | Siswa menyeret kartu ke kotak yang tepat. |

**Struktur peta konsep dan kunci jawaban:**

```
[Baterai / Energi KIMIA] ──► [ENERGI LISTRIK] ──► [Lampu senter] ──► [CAHAYA]
                                  │
        ┌───────────┬─────────────┼─────────────┐
        ▼           ▼             ▼             ▼
     [LAMPU]    [SETRIKA]    [KIPAS ANGIN]   [RADIO]
        ▼           ▼             ▼             ▼
    [CAHAYA]     [PANAS]        [GERAK]       [BUNYI]
```

**Level dan soal:**

| Level | Bentuk | Kartu yang Diseret | Poin |
|---|---|---|---|
| 1 (mudah) | Cocokkan alat dengan energi hasil | Kartu: Cahaya, Panas, Gerak, Bunyi → ke kotak di bawah Lampu, Setrika, Kipas, Radio | 4 × 10 |
| 2 (sedang) | Lengkapi rantai senter | Kartu: Energi Kimia, Energi Listrik, Cahaya → ke 3 kotak berurutan | 3 × 10 |
| 3 (tantangan) | Semua kotak pada peta lengkap, dengan 1-2 kartu pengecoh (misalnya "Energi Angin") | Peta lengkap | 30 |

**Mekanisme game:**
- Kartu yang tepat "menempel" dan menyala dengan bunyi ceria. Kartu yang salah kembali ke gudang dengan getaran lembut. Pesan: "Hampir! Coba lagi ya!"
- Petunjuk 💡 tersedia maksimal 2 kali per level. Petunjuk menyorot warna kode energi yang benar.
- Layar hasil: skor, bintang ⭐ (1-3), dan lencana 3 🥉 "Ahli Energi". Pengecoh yang salah ditampilkan kembali dengan penjelasan singkat.
- Data skor dapat dicatat guru (misalnya melalui kolom nama di layar 1 atau tangkapan layar skor).

**Kriteria ketuntasan yang disarankan:** ≥ 70 poin, atau 2 bintang ke atas. Siswa di bawah kriteria diarahkan ke tombol "Belajar lagi" menuju layar 5f.

### Layar 8: Refleksi

| Bagian | Rancangan |
|---|---|
| **Visual** | "Cermin Refleksi", dengan Si Volta duduk di depan cermin ajaib. |
| **Pertanyaan 1 (emoji)** | "Bagaimana perasaanmu belajar hari ini?" 😄 Seru / 🙂 Biasa / 😕 Sulit |
| **Pertanyaan 2 (geser)** | Slider "Seberapa paham kamu tentang perubahan energi?" (Belum paham ⟷ Paham banget). |
| **Pertanyaan 3 (seret)** | "Alat mana yang paling menarik?" Siswa menyeret bintang ke salah satu alat. |
| **Pertanyaan 4 (terbuka)** | Kolom singkat: "Satu hal baru yang kupelajari…" dan "Alat di rumahku yang mengubah energi adalah…" |
| **Perbandingan** | Menampilkan kembali dugaan awal siswa dari layar 3 berdampingan dengan kesimpulan akhir: "Dulu aku kira… sekarang aku tahu…" |
| **Navigasi** | ▶ Layar 9 |

### Layar 9: Penutup

| Elemen | Rancangan |
|---|---|
| **Visual** | Sertifikat "Penyelidik Energi" dengan nama siswa, tiga lencana yang terkumpul, dan animasi kembang api dari lampu. |
| **Teks Si Volta** | "Hebat! Sekarang kamu tahu energi tidak hilang, tapi berubah bentuk. Coba cari 3 alat lain di rumahmu dan tebak perubahan energinya!" |
| **Tantangan rumah (opsional)** | Kartu "Misi Rumah": siswa menggambar atau memotret satu alat listrik dan menuliskan perubahan energinya. |
| **Tombol** | 🔁 Main lagi, 🏠 Menu, ❌ Keluar |

## E. Rencana Aktivitas Pendukung (Kinestetik Luar Layar)

Agar tidak bergantung penuh pada layar, guru dapat menambahkan:
1. **Senter asli** pada apersepsi. Siswa memasang dan melepas baterai.
2. **Rasakan angin dan bunyi:** kipas kertas untuk merasakan gerak, dan alat musik sederhana untuk bunyi.
3. **Gerak tubuh "Patung Energi":** guru menyebut alat, siswa memeragakan energi hasilnya (lengan berputar = gerak, tangan menutup telinga = bunyi, dan seterusnya).

## F. Asesmen dan Umpan Balik

| Aspek | Instrumen | Sumber |
|---|---|---|
| Pengetahuan | Skor drag-and-drop | Layar 7 |
| Keterampilan proses (mengamati dan mencatat) | Tabel catatan penyelidikan | Layar 6b-6e |
| Sikap dan keterlibatan | Refleksi emoji dan slider | Layar 8 |

## G. Catatan Pengembangan

- **Bahasa:** kalimat pendek, kosakata sesuai kelas IV, dan istilah "energi kimia" dijelaskan dengan contoh baterai.
- **Aksesibilitas:** kontras warna tinggi, narasi audio, dan ukuran huruf minimal 20 pt. Warna tidak menjadi satu-satunya penanda, karena setiap energi juga memiliki ikon dan huruf.
- **Keselamatan:** di layar setrika dan listrik selalu ada pengingat bahwa alat listrik nyata tidak boleh disentuh tanpa pendamping dewasa.
- **Uji coba:** coba dengan 3-5 siswa sebelum digunakan, lalu perbaiki bagian yang membingungkan.
