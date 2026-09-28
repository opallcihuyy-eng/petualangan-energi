"""
Petualangan Energi - Media Pembelajaran IPAS Fase B (Kelas 4 SD)
Topik: Mengubah Bentuk Energi

Struktur file:
  1. DATA         -> isi materi (alat, energi) dan soal kuis. Edit di sini untuk mengubah isi.
  2. TEMA         -> warna, font, dan ukuran. Edit di sini untuk mengubah tampilan.
  2b. ANIMASI     -> fungsi gambar Canvas per alat (ANIMASI).
  3. HALAMAN      -> satu class per layar (Menu, Simulasi, Kuis, Hasil).
  4. APLIKASI     -> class App yang mengatur perpindahan halaman.

Hanya memakai library bawaan Python (tkinter), jadi tidak perlu pip install.
"""

import tkinter as tk
from tkinter import messagebox

# =====================================================================
# 1. DATA MATERI
# =====================================================================

# Warna khusus tiap bentuk energi (dipakai konsisten di seluruh aplikasi)
WARNA_ENERGI = {
    "kimia":   "#4CAF50",  # hijau
    "listrik": "#29B6F6",  # biru muda
    "cahaya":  "#FFC107",  # kuning
    "panas":   "#F44336",  # merah
    "gerak":   "#3F51B5",  # biru tua
    "bunyi":   "#9C27B0",  # ungu
}

# Setiap alat: ikon, rantai perubahan energi (urut dari awal ke akhir), kalimat penjelasan.
# Untuk menambah alat baru, cukup tambahkan satu entri baru di sini.
ALAT = {
    "Senter": {
        "ikon": "🔦",
        "rantai": ["kimia", "listrik", "cahaya"],
        "kalimat": "Baterai pada senter mengubah energi kimia -> energi listrik -> energi cahaya.",
    },
    "Kipas Angin": {
        "ikon": "🌀",
        "rantai": ["listrik", "gerak"],
        "kalimat": "Kipas angin mengubah energi listrik menjadi energi gerak.",
    },
    "Setrika": {
        "ikon": "♨️",
        "rantai": ["listrik", "panas"],
        "kalimat": "Setrika mengubah energi listrik menjadi energi panas.",
    },
    "Radio": {
        "ikon": "📻",
        "rantai": ["listrik", "bunyi"],
        "kalimat": "Radio mengubah energi listrik menjadi energi bunyi.",
    },
}

# Soal kuis pilihan ganda.
# "jawaban" adalah indeks pilihan yang benar (mulai dari 0).
KUIS = [
    {
        "soal": "Dari mana energi cahaya pada senter berasal?",
        "pilihan": ["Dari energi kimia pada baterai", "Dari energi angin", "Dari energi gerak", "Dari matahari"],
        "jawaban": 0,
        "bahas": "Baterai menyimpan energi kimia, lalu berubah menjadi listrik, lalu cahaya.",
    },
    {
        "soal": "Setrika listrik mengubah energi listrik menjadi energi ...",
        "pilihan": ["Bunyi", "Panas", "Gerak", "Cahaya"],
        "jawaban": 1,
        "bahas": "Bagian bawah setrika menjadi panas sehingga kain menjadi rata.",
    },
    {
        "soal": "Radio menghasilkan suara. Perubahan energi pada radio adalah ...",
        "pilihan": ["Listrik -> Panas", "Kimia -> Gerak", "Listrik -> Bunyi", "Cahaya -> Listrik"],
        "jawaban": 2,
        "bahas": "Energi listrik pada radio diubah menjadi energi bunyi.",
    },
]

# =====================================================================
# 2. TEMA TAMPILAN
# =====================================================================

BG = "#FFF8E1"          # latar krem lembut
BG_KARTU = "#FFFFFF"
WARNA_UTAMA = "#FF7043"  # oranye
WARNA_TEKS = "#37474F"
FONT_JUDUL = ("Comic Sans MS", 28, "bold")
FONT_SUB = ("Comic Sans MS", 18, "bold")
FONT_TEKS = ("Comic Sans MS", 16)
FONT_TOMBOL = ("Comic Sans MS", 16, "bold")


def buat_tombol(induk, teks, perintah, warna=WARNA_UTAMA, lebar=18):
    """Membuat tombol besar berwarna, ramah untuk jari/kursor anak."""
    return tk.Button(
        induk, text=teks, command=perintah, font=FONT_TOMBOL, width=lebar,
        bg=warna, fg="white", activebackground=warna, activeforeground="white",
        relief="raised", bd=4, cursor="hand2", pady=6,
    )


def nama_energi(kunci):
    """Mengubah kunci 'kimia' menjadi teks 'Energi Kimia'."""
    return f"Energi {kunci.capitalize()}"


# =====================================================================
# 2b. ANIMASI CANVAS
# =====================================================================
# Setiap alat punya satu fungsi gambar(c, t, nyala):
#   c     = objek Canvas
#   t     = nomor frame (bertambah setiap 50 ms, mulai dari 0 saat alat dihidupkan)
#   nyala = True jika alat sedang dihidupkan, False jika dimatikan (kondisi awal)
# Fungsi menghapus dan menggambar ulang setiap frame. Untuk alat baru, buat fungsi
# serupa lalu daftarkan di dictionary ANIMASI di bawah.

def campur_warna(w1, w2, h):
    """Campuran dua warna RGB (tuple) sesuai h (0..1), hasilnya teks '#rrggbb'."""
    return "#%02x%02x%02x" % tuple(int(a + (b - a) * h) for a, b in zip(w1, w2))


def gambar_senter(c, t, nyala):
    """Senter: titik listrik mengalir dari baterai ke lampu, lalu sinar keluar."""
    if nyala:  # sinar berkedip lembut
        c.create_polygon(240, 75, 310, 25, 310, 175, 240, 125,
                         fill="#FFF59D" if t % 10 < 5 else "#FFEE58", outline="")
    c.create_rectangle(40, 80, 200, 120, fill="#90A4AE", outline="#546E7A", width=3)   # badan
    c.create_rectangle(60, 87, 125, 113, fill="#4CAF50" if nyala else "#A5D6A7",
                       outline="#2E7D32", width=2)                                    # baterai
    c.create_text(92, 100, text="Baterai", font=("Arial", 9, "bold"), fill="white")
    c.create_polygon(200, 75, 240, 65, 240, 135, 200, 125, fill="#546E7A")            # kepala
    c.create_oval(190, 88, 222, 112, fill="#FFEB3B" if nyala else "#CFD8DC",
                  outline="#F9A825", width=2)                                        # lampu
    if nyala:  # titik listrik bergerak ke kanan
        for i in range(3):
            x = 128 + (t * 4 + i * 25) % 60
            c.create_oval(x - 4, 96, x + 4, 104, fill="#29B6F6", outline="")


def gambar_kipas(c, t, nyala):
    """Kipas angin: baling-baling berputar dan garis angin bergerak."""
    cx, cy = 150, 85
    c.create_rectangle(143, 130, 157, 172, fill="#90A4AE", outline="#546E7A")          # tiang
    c.create_rectangle(110, 170, 190, 182, fill="#78909C", outline="#546E7A")          # alas
    sudut = (t * 18) % 360 if nyala else 30                                            # sudut putar
    for i in range(3):
        c.create_arc(cx - 58, cy - 58, cx + 58, cy + 58, start=sudut + i * 120,
                     extent=55, fill="#3F51B5", outline="#283593")
    c.create_oval(cx - 10, cy - 10, cx + 10, cy + 10, fill="#FFC107", outline="#F9A825")
    c.create_oval(cx - 65, cy - 65, cx + 65, cy + 65, outline="#78909C", width=3)      # kerangka
    if nyala:  # garis angin
        for i in range(3):
            x0 = 225 + (t * 7 + i * 22) % 70
            c.create_line(x0, 55 + i * 30, x0 + 25, 55 + i * 30, fill="#81D4FA", width=3)


def gambar_setrika(c, t, nyala):
    """Setrika: alas berubah dari abu-abu menjadi merah, termometer naik, uap muncul."""
    h = min(1.0, t / 50) if nyala else 0.0                                            # tingkat panas 0..1
    c.create_polygon(50, 150, 240, 150, 205, 112, 50, 112, outline="#37474F", width=3,
                     fill=campur_warna((158, 158, 158), (244, 67, 54), h))             # alas
    c.create_polygon(60, 112, 205, 112, 185, 80, 60, 80, fill="#FF8A65",
                     outline="#37474F", width=3)                                       # badan
    c.create_rectangle(85, 50, 175, 80, outline="#37474F", width=6)                    # pegangan
    if h > 0.6:  # uap naik
        for i in range(3):
            y = 100 - (t * 2 + i * 22) % 70
            c.create_oval(89 + i * 40, y - 6, 101 + i * 40, y + 6, outline="#B0BEC5", width=2)
    c.create_rectangle(275, 30, 291, 150, fill="white", outline="#37474F", width=2)   # termometer
    c.create_rectangle(277, 148 - (15 + h * 100), 289, 148, fill="#F44336", outline="")
    c.create_text(283, 166, text=f"{25 + int(h * 95)}°C", font=("Arial", 10, "bold"), fill="#37474F")


def gambar_radio(c, t, nyala):
    """Radio: gelombang bunyi melebar dari speaker."""
    sx, sy = 100, 105
    if nyala:  # gelombang digambar lebih dulu agar terlihat keluar dari badan radio
        for i in range(3):
            r = 40 + (t * 3 + i * 20) % 60
            c.create_oval(sx - r, sy - r, sx + r, sy + r, outline="#BA68C8", width=3)
    c.create_line(230, 60, 285, 15, fill="#546E7A", width=3)                          # antena
    c.create_rectangle(45, 60, 275, 150, fill="#7E57C2", outline="#4527A0", width=3)   # badan
    c.create_oval(sx - 32, sy - 32, sx + 32, sy + 32, fill="#311B92", outline="#D1C4E9", width=2)
    c.create_oval(sx - 12, sy - 12, sx + 12, sy + 12, fill="#5E35B1", outline="")
    c.create_oval(205, 80, 227, 102, fill="#FFCA28" if nyala else "#BDBDBD", outline="#37474F")  # tombol
    c.create_oval(235, 80, 257, 102, fill="#E0E0E0", outline="#37474F")


# Daftar fungsi animasi. Kunci harus sama dengan nama alat pada ALAT.
ANIMASI = {
    "Senter": gambar_senter,
    "Kipas Angin": gambar_kipas,
    "Setrika": gambar_setrika,
    "Radio": gambar_radio,
}


# =====================================================================
# 3. HALAMAN-HALAMAN
# =====================================================================

class Halaman(tk.Frame):
    """Kelas dasar semua halaman. Menyimpan referensi ke App agar bisa berpindah halaman."""

    def __init__(self, app):
        super().__init__(app.wadah, bg=BG)
        self.app = app

    def saat_tampil(self):
        """Dipanggil setiap kali halaman ditampilkan. Override jika perlu reset."""
        pass

    def saat_sembunyi(self):
        """Dipanggil saat pindah ke halaman lain. Override untuk menghentikan animasi."""
        pass


class HalamanMenu(Halaman):
    """Menu utama: pilih Simulasi Alat atau Kuis."""

    def __init__(self, app):
        super().__init__(app)
        tk.Label(self, text="⚡ Petualangan Energi ⚡", font=FONT_JUDUL, bg=BG, fg=WARNA_UTAMA).pack(pady=(60, 5))
        tk.Label(self, text="Ayo belajar Mengubah Bentuk Energi!", font=FONT_SUB, bg=BG, fg=WARNA_TEKS).pack(pady=5)
        tk.Label(self, text="🤖", font=("Arial", 70), bg=BG).pack(pady=10)
        buat_tombol(self, "🧪 Simulasi Alat", lambda: app.tampilkan("simulasi"), "#29B6F6", 22).pack(pady=10)
        buat_tombol(self, "📝 Mini Kuis", lambda: app.tampilkan("kuis"), "#66BB6A", 22).pack(pady=10)
        buat_tombol(self, "Keluar", app.destroy, "#90A4AE", 22).pack(pady=10)


class HalamanSimulasi(Halaman):
    """Murid memilih alat, melihat animasi Canvas, energi awal/akhir, dan kalimat penjelasan."""

    def __init__(self, app):
        super().__init__(app)
        self.alat = None    # nama alat yang sedang dipilih
        self.nyala = False  # status saklar
        self.t = 0          # nomor frame animasi
        self.job = None     # id jadwal after(), disimpan agar bisa dibatalkan

        tk.Label(self, text="🧪 Simulasi Alat", font=FONT_JUDUL, bg=BG, fg=WARNA_UTAMA).pack(pady=(15, 3))
        tk.Label(self, text="Pilih alat, lalu lihat energinya berubah!", font=FONT_TEKS, bg=BG, fg=WARNA_TEKS).pack()

        # Baris tombol pilihan alat (dibuat otomatis dari data ALAT)
        baris = tk.Frame(self, bg=BG)
        baris.pack(pady=10)
        for nama, data in ALAT.items():
            buat_tombol(baris, f"{data['ikon']}\n{nama}", lambda n=nama: self.pilih(n), "#FFA726", 12).pack(side="left", padx=8)

        # Area tengah: Canvas animasi (kiri) dan kartu hasil (kanan)
        tengah = tk.Frame(self, bg=BG)
        tengah.pack(fill="x", padx=30, pady=5)
        kiri = tk.Frame(tengah, bg=BG)
        kiri.pack(side="left")
        self.kanvas = tk.Canvas(kiri, width=320, height=190, bg="white",
                                highlightthickness=4, highlightbackground="#FFA726")
        self.kanvas.pack()
        self.btn_saklar = buat_tombol(kiri, "⏻ Hidupkan", self.saklar, "#66BB6A", 16)
        self.btn_saklar.pack(pady=8)

        self.kartu = tk.Frame(tengah, bg=BG_KARTU, bd=4, relief="groove")
        self.kartu.pack(side="left", fill="both", expand=True, padx=(20, 0))
        self.lbl_judul = tk.Label(self.kartu, font=FONT_SUB, bg=BG_KARTU, fg=WARNA_TEKS)
        self.lbl_judul.pack(pady=8)
        self.baris_energi = tk.Frame(self.kartu, bg=BG_KARTU)  # tempat "chip" energi
        self.baris_energi.pack(pady=5)
        self.lbl_awal = tk.Label(self.kartu, font=FONT_TEKS, bg=BG_KARTU, fg=WARNA_TEKS)
        self.lbl_awal.pack()
        self.lbl_akhir = tk.Label(self.kartu, font=FONT_TEKS, bg=BG_KARTU, fg=WARNA_TEKS)
        self.lbl_akhir.pack()
        self.lbl_kalimat = tk.Label(self.kartu, font=FONT_SUB, bg=BG_KARTU, fg=WARNA_UTAMA,
                                    wraplength=430, justify="center")
        self.lbl_kalimat.pack(pady=10, padx=10)

        buat_tombol(self, "🏠 Kembali ke Menu", lambda: app.tampilkan("menu"), "#90A4AE", 20).pack(pady=10)

    def saat_tampil(self):
        self.pilih(None)  # reset tampilan

    def saat_sembunyi(self):
        self.berhenti()   # hentikan animasi saat pindah halaman

    def berhenti(self):
        """Membatalkan jadwal animasi yang sedang berjalan."""
        if self.job is not None:
            self.after_cancel(self.job)
            self.job = None

    def pilih(self, nama):
        """Menampilkan hasil untuk alat yang dipilih (atau mengosongkan jika nama=None)."""
        self.berhenti()
        self.alat = nama
        for w in self.baris_energi.winfo_children():
            w.destroy()
        if nama is None:
            self.lbl_judul.config(text="Belum ada alat dipilih 👆")
            for lbl in (self.lbl_awal, self.lbl_akhir, self.lbl_kalimat):
                lbl.config(text="")
            self.kanvas.delete("all")
            self.btn_saklar.config(state="disabled", text="⏻ Hidupkan")
            return

        data = ALAT[nama]
        rantai = data["rantai"]
        self.lbl_judul.config(text=f"{data['ikon']} {nama} dihidupkan!")

        # Gambar rantai energi: [Kimia] -> [Listrik] -> [Cahaya]
        for i, kunci in enumerate(rantai):
            tk.Label(self.baris_energi, text=nama_energi(kunci), font=("Comic Sans MS", 12, "bold"),
                     bg=WARNA_ENERGI[kunci], fg="white", padx=8, pady=5).pack(side="left")
            if i < len(rantai) - 1:
                tk.Label(self.baris_energi, text=" ➜ ", font=FONT_SUB, bg=BG_KARTU).pack(side="left")

        self.lbl_awal.config(text=f"Kondisi awal: {nama_energi(rantai[0])}")
        self.lbl_akhir.config(text=f"Kondisi akhir: {nama_energi(rantai[-1])}")
        self.lbl_kalimat.config(text=data["kalimat"])

        # Alat langsung menyala; murid boleh mematikannya dengan tombol saklar
        self.nyala = True
        self.t = 0
        self.btn_saklar.config(state="normal", text="⏻ Matikan")
        self.animasi()

    def saklar(self):
        """Menghidupkan / mematikan alat (mengulang animasi dari awal)."""
        if self.alat is None:
            return
        self.berhenti()
        self.nyala = not self.nyala
        self.t = 0
        self.btn_saklar.config(text="⏻ Matikan" if self.nyala else "⏻ Hidupkan")
        self.animasi()

    def animasi(self):
        """Menggambar satu frame, lalu menjadwalkan frame berikutnya (20 frame/detik)."""
        c = self.kanvas
        c.delete("all")
        ANIMASI[self.alat](c, self.t, self.nyala)
        c.create_text(160, 12, font=("Comic Sans MS", 11, "bold"), fill=WARNA_TEKS,
                      text="Alat menyala (kondisi akhir)" if self.nyala else "Alat mati (kondisi awal)")
        self.t += 1
        self.job = self.after(50, self.animasi) if self.nyala else None


class HalamanKuis(Halaman):
    """Kuis pilihan ganda. Soal diambil dari list KUIS."""

    def __init__(self, app):
        super().__init__(app)
        self.no = 0
        self.skor = 0
        self.dijawab = False
        self.pilihan = tk.IntVar(value=-1)

        self.lbl_no = tk.Label(self, font=FONT_SUB, bg=BG, fg=WARNA_UTAMA)
        self.lbl_no.pack(pady=(30, 5))
        self.lbl_soal = tk.Label(self, font=FONT_SUB, bg=BG, fg=WARNA_TEKS, wraplength=800, justify="center")
        self.lbl_soal.pack(pady=15)

        self.opsi = []
        for i in range(4):  # maksimal 4 pilihan
            rb = tk.Radiobutton(self, variable=self.pilihan, value=i, font=FONT_TEKS, bg=BG_KARTU,
                                fg=WARNA_TEKS, anchor="w", indicatoron=False, width=50, pady=8,
                                selectcolor="#FFE082", cursor="hand2")
            rb.pack(pady=4)
            self.opsi.append(rb)

        self.lbl_umpan = tk.Label(self, font=FONT_TEKS, bg=BG, wraplength=800)
        self.lbl_umpan.pack(pady=10)
        self.tombol = buat_tombol(self, "Periksa Jawaban", self.aksi, "#66BB6A", 20)
        self.tombol.pack(pady=5)

    def saat_tampil(self):
        """Reset kuis setiap kali dibuka."""
        self.no = 0
        self.skor = 0
        self.tampil_soal()

    def tampil_soal(self):
        soal = KUIS[self.no]
        self.dijawab = False
        self.pilihan.set(-1)
        self.lbl_no.config(text=f"Soal {self.no + 1} dari {len(KUIS)}")
        self.lbl_soal.config(text=soal["soal"])
        for i, rb in enumerate(self.opsi):
            rb.config(text=f"{'ABCD'[i]}.  {soal['pilihan'][i]}", state="normal", bg=BG_KARTU)
        self.lbl_umpan.config(text="")
        self.tombol.config(text="Periksa Jawaban")

    def aksi(self):
        """Satu tombol dengan dua fungsi: periksa jawaban, lalu lanjut ke soal berikutnya."""
        if not self.dijawab:
            self.periksa()
        else:
            self.no += 1
            if self.no < len(KUIS):
                self.tampil_soal()
            else:
                self.app.halaman["hasil"].set_skor(self.skor, len(KUIS))
                self.app.tampilkan("hasil")

    def periksa(self):
        pilih = self.pilihan.get()
        if pilih == -1:
            messagebox.showinfo("Ups!", "Pilih salah satu jawaban dulu ya 😊")
            return
        soal = KUIS[self.no]
        self.dijawab = True
        for rb in self.opsi:
            rb.config(state="disabled")
        self.opsi[soal["jawaban"]].config(bg="#A5D6A7")  # jawaban benar = hijau
        if pilih == soal["jawaban"]:
            self.skor += 1
            self.lbl_umpan.config(text=f"🎉 Benar! {soal['bahas']}", fg="#2E7D32")
        else:
            self.opsi[pilih].config(bg="#EF9A9A")  # jawaban salah = merah muda
            self.lbl_umpan.config(text=f"Hampir! {soal['bahas']}", fg="#C62828")
        akhir = self.no == len(KUIS) - 1
        self.tombol.config(text="Lihat Hasil" if akhir else "Soal Berikutnya ➜")


class HalamanHasil(Halaman):
    """Menampilkan skor akhir dan pesan penyemangat."""

    def __init__(self, app):
        super().__init__(app)
        tk.Label(self, text="🏆 Hasil Kuis", font=FONT_JUDUL, bg=BG, fg=WARNA_UTAMA).pack(pady=(60, 10))
        self.lbl_bintang = tk.Label(self, font=("Arial", 48), bg=BG)
        self.lbl_bintang.pack(pady=10)
        self.lbl_skor = tk.Label(self, font=FONT_SUB, bg=BG, fg=WARNA_TEKS)
        self.lbl_skor.pack(pady=5)
        self.lbl_pesan = tk.Label(self, font=FONT_TEKS, bg=BG, fg=WARNA_TEKS, wraplength=700)
        self.lbl_pesan.pack(pady=10)
        buat_tombol(self, "🔁 Ulangi Kuis", lambda: app.tampilkan("kuis"), "#66BB6A", 20).pack(pady=8)
        buat_tombol(self, "🏠 Kembali ke Menu", lambda: app.tampilkan("menu"), "#90A4AE", 20).pack(pady=8)

    def set_skor(self, skor, total):
        nilai = round(skor / total * 100)
        self.lbl_bintang.config(text="⭐" * skor + "☆" * (total - skor))
        self.lbl_skor.config(text=f"Skor: {skor} dari {total}  (Nilai {nilai})")
        if skor == total:
            pesan = "Luar biasa! Kamu Ahli Energi! 🎉"
        elif skor >= 2:
            pesan = "Bagus sekali! Sedikit lagi jadi Ahli Energi."
        else:
            pesan = "Ayo coba lagi! Buka menu Simulasi Alat dulu untuk belajar. 💪"
        self.lbl_pesan.config(text=pesan)


# =====================================================================
# 4. APLIKASI UTAMA
# =====================================================================

class App(tk.Tk):
    """Jendela utama. Menyimpan semua halaman dan menampilkan satu per satu."""

    def __init__(self):
        super().__init__()
        self.title("Petualangan Energi - IPAS Kelas 4 SD")
        self.geometry("980x680")
        self.minsize(900, 640)
        self.configure(bg=BG)

        self.wadah = tk.Frame(self, bg=BG)
        self.wadah.pack(fill="both", expand=True)

        # Daftarkan halaman di sini. Kunci dipakai pada self.tampilkan("kunci").
        self.halaman = {
            "menu": HalamanMenu(self),
            "simulasi": HalamanSimulasi(self),
            "kuis": HalamanKuis(self),
            "hasil": HalamanHasil(self),
        }
        for h in self.halaman.values():
            h.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.tampilkan("menu")

    def tampilkan(self, kunci):
        """Menampilkan halaman dengan kunci tertentu di depan."""
        for k, hal in self.halaman.items():
            if k != kunci:
                hal.saat_sembunyi()
        h = self.halaman[kunci]
        h.saat_tampil()
        h.tkraise()


if __name__ == "__main__":
    App().mainloop()
