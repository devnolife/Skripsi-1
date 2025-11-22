# Dashboard Klasifikasi Mahasiswa Berprestasi

## 🎯 Fitur Dashboard

### ✅ Auto-Load Data
Dashboard akan otomatis memuat data saat dibuka:
1. **Data Mahasiswa** (`mahasiswa_clean_20250913_143222.csv`) - 112 mahasiswa
2. **Data Prestasi** (`prestasi_clean_20250913_143222.csv`) - 287 prestasi

### 📊 Relasi Data
Dashboard sudah mengintegrasikan:
- **NIM → Nama Mahasiswa**: Setiap prestasi akan menampilkan nama mahasiswa yang sesuai
- **ID Mahasiswa → Data Akademik**: Otomatis mapping dari `id_mahasiswa` di prestasi ke `nim` di data mahasiswa

## 🚀 Cara Menggunakan

### Opsi 1: Buka Langsung (Rekomendasi)
```bash
# Server sudah jalan di:
http://localhost:8080/dashboard.html
```

### Opsi 2: Start Server Manual
```bash
cd /workspaces/Skripsi
python3 -m http.server 8080 --directory docs --bind 0.0.0.0
```

Kemudian buka: `http://localhost:8080/dashboard.html`

## 📋 Fitur Lengkap

### Tab Dashboard
- ✅ Total mahasiswa: 112
- ✅ Total prestasi: 287
- ✅ Rata-rata IPK
- ✅ Distribusi prestasi per tingkat

### Tab Data Mahasiswa
- ✅ Tabel lengkap dengan NIM, Nama, Jenis Kelamin
- ✅ IPK terakhir dari setiap mahasiswa
- ✅ Status kelulusan
- ✅ Filter/Search real-time

### Tab Data Prestasi
- ✅ **NIM Mahasiswa** (baru ditambahkan!)
- ✅ **Nama Mahasiswa** (relasi otomatis dari NIM)
- ✅ Judul prestasi
- ✅ Jenis prestasi (individu/tim)
- ✅ Tingkat (lokal/regional/nasional/internasional)
- ✅ Kategori (akademik/non-akademik)
- ✅ Tanggal prestasi
- ✅ Filter/Search by NIM atau Nama

### Tab Analisis
- ✅ Scatter plot: Korelasi IPK vs Jumlah Prestasi
- ✅ Chart interaktif dengan Chart.js

## 🔄 Update Terbaru

### Version 2.0 (November 2025)
✅ **Relasi NIM → Nama FIXED!**
- Setiap prestasi sekarang menampilkan NIM dan Nama Mahasiswa
- Auto-mapping dari `id_mahasiswa` (prestasi) ke `nim` (mahasiswa)
- Handle multiple NIM formats
- Fallback "Tidak ditemukan" untuk NIM yang tidak match

✅ **Auto-Load Data**
- Data mahasiswa dan prestasi dimuat otomatis saat dashboard dibuka
- Sequential loading: Mahasiswa → Prestasi → Charts
- Status indicator untuk setiap file yang dimuat

✅ **Enhanced Search**
- Search by NIM
- Search by Nama Mahasiswa
- Search by Judul Prestasi
- Search by Tingkat/Kategori

## 📂 File Dependencies

Dashboard membutuhkan file berikut di folder `/docs`:
```
docs/
├── dashboard.html (main file)
├── mahasiswa_clean_20250913_143222.csv
└── prestasi_clean_20250913_143222.csv
```

File sudah di-copy dengan command:
```bash
cp data/processed/mahasiswa_clean_20250913_143222.csv docs/
cp data/processed/prestasi_clean_20250913_143222.csv docs/
```

## 🎨 Teknologi

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Charts**: Chart.js 3.9.1
- **CSV Parser**: PapaParse 5.4.1
- **Icons**: Font Awesome 6.0.0
- **Design**: Modern Glassmorphism with Purple/Blue gradient

## 📱 Responsive Design

Dashboard fully responsive untuk:
- 💻 Desktop (1400px+)
- 📱 Tablet (768px - 1400px)
- 📱 Mobile (< 768px)

## 🐛 Troubleshooting

### Data tidak muncul?
1. Pastikan file CSV ada di folder `/docs`
2. Check console browser (F12) untuk error messages
3. Refresh page (Ctrl+R atau Cmd+R)

### Nama mahasiswa "Tidak ditemukan"?
1. Check format NIM di kedua file (harus match persis)
2. Pastikan data mahasiswa dimuat lebih dulu (auto-load sudah handle ini)
3. Check console untuk mapping errors

### Server tidak bisa diakses?
```bash
# Kill server lama dan start ulang
pkill -f "python3 -m http.server"
cd /workspaces/Skripsi
python3 -m http.server 8080 --directory docs --bind 0.0.0.0 &
```

## 📞 Support

Untuk pertanyaan atau issue, check:
- Console browser (F12 → Console tab)
- Network tab untuk file loading issues
- File paths dan permissions

---

**Last Updated**: November 15, 2025
**Version**: 2.0 (with NIM-Nama relation)
**Status**: ✅ Production Ready
