# ⚡ Petualangan Energi

Aplikasi desktop media pembelajaran **IPAS Fase B (Kelas 4 SD)** dengan topik **Mengubah Bentuk Energi**. Dibuat dengan Python dan `tkinter`, berwarna dan bertombol besar agar ramah untuk anak usia 9-10 tahun yang belajar secara visual dan kinestetik.

Rancangan lengkap media (navigasi, alur waktu 2 × 35 menit, dan storyboard per layar) ada di [`docs/STORYBOARD.md`](docs/STORYBOARD.md).

## Fitur Utama

- **Simulasi Alat.** Murid memilih Senter, Kipas Angin, Setrika, atau Radio, lalu melihat kondisi awal energi, kondisi akhir energi, dan kalimat penjelasannya. Contoh: *"Setrika mengubah energi listrik menjadi energi panas."*
- **Animasi Canvas.** Baling-baling kipas berputar, termometer setrika naik, gelombang bunyi radio melebar, dan listrik mengalir di senter. Tombol saklar ⏻ membandingkan kondisi awal (mati) dan akhir (menyala).
- **Kode warna energi.** Setiap bentuk energi (kimia, listrik, cahaya, panas, gerak, bunyi) punya warna tetap.
- **Mini kuis pilihan ganda.** Tiga soal dengan umpan balik langsung, pembahasan singkat, dan skor akhir berbentuk bintang.
- **Mudah dimodifikasi.** Materi, soal, dan animasi dipisahkan dari logika program.

## Tangkapan Layar

Tambahkan gambar di folder `docs/` lalu tampilkan di sini:

```markdown
![Menu utama](docs/menu.png)
![Simulasi alat](docs/simulasi.png)
```

## Prasyarat

- Python **3.8 atau lebih baru**
- `tkinter` (sudah termasuk pada instalasi Python di Windows dan macOS)
- Tidak ada library tambahan yang perlu di-install

Pada Linux (Debian/Ubuntu), jika `tkinter` belum ada:

```bash
sudo apt install python3-tk
```

## Cara Menjalankan

```bash
git clone https://github.com/<username>/petualangan-energi.git
cd petualangan-energi
python app.py
```

Pada macOS/Linux gunakan `python3 app.py`. Pada Windows, jika `python` tidak dikenali, coba `py app.py`.

## Struktur Repositori

```
petualangan-energi/
├── app.py              # aplikasi utama
├── README.md
├── LICENSE
├── .gitignore
└── docs/
    └── STORYBOARD.md   # rancangan media interaktif lengkap
```

## Struktur Kode `app.py`

| Bagian | Fungsi |
|---|---|
| `ALAT`, `KUIS`, `WARNA_ENERGI` | Data materi, soal, dan warna |
| `gambar_*` dan `ANIMASI` | Fungsi animasi Canvas untuk tiap alat |
| Konstanta tema (`BG`, `FONT_*`) | Warna dan font |
| `HalamanMenu`, `HalamanSimulasi`, `HalamanKuis`, `HalamanHasil` | Satu class per layar |
| `App` | Jendela utama dan perpindahan halaman |

## Cara Memodifikasi

**Menambah alat baru:** tambahkan entri pada dictionary `ALAT`.

```python
"Lampu": {
    "ikon": "💡",
    "rantai": ["listrik", "cahaya"],
    "kalimat": "Lampu mengubah energi listrik menjadi energi cahaya.",
},
```

**Menambah animasi alat baru:** buat fungsi `gambar_lampu(c, t, nyala)` yang menggambar satu frame di Canvas (`t` = nomor frame, `nyala` = status saklar), lalu daftarkan di dictionary `ANIMASI` dengan kunci yang sama dengan nama alat pada `ALAT`.

**Menambah soal:** tambahkan dictionary baru pada list `KUIS`. Nilai `jawaban` adalah indeks pilihan benar (mulai dari 0), maksimal 4 pilihan.

**Mengubah tampilan:** ubah warna dan font pada bagian *TEMA TAMPILAN*.

## Rencana Pengembangan

- [x] Simulasi alat dengan animasi Canvas
- [x] Mini kuis pilihan ganda (3 soal)
- [ ] Layar apersepsi dan pertanyaan pemantik
- [ ] Eksplorasi materi (termasuk Lampu)
- [ ] Evaluasi drag-and-drop peta konsep
- [ ] Layar refleksi dan sertifikat penutup
- [ ] Pencatatan skor untuk guru

## Catatan

- Font *Comic Sans MS* dipilih agar ramah anak. Jika tidak tersedia, tkinter memakai font bawaan sistem.
- Emoji dapat tampil berbeda antarsistem operasi.

## Lisensi

[MIT](LICENSE). Ganti `<Nama Anda>` pada berkas `LICENSE` dengan nama Anda.
