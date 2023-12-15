class Film:
    def __init__(self, ID_Film, Judul, Genre, Durasi, Tanggal_Rilis, Harga_Film):
        self.ID_Film = ID_Film
        self.Judul = Judul
        self.Genre = Genre
        self.Durasi = Durasi
        self.Tanggal_Rilis = Tanggal_Rilis
        self.Harga_Film = Harga_Film

class Studio:
    def __init__(self, ID_Studio, Nama_Studio, Kapasitas, Lokasi):
        self.ID_Studio = ID_Studio
        self.Nama_Studio = Nama_Studio
        self.Kapasitas = Kapasitas
        self.Lokasi = Lokasi

class Jadwal:
    def __init__(self, ID_Jadwal, ID_Film, ID_Studio, Jam_Tayang, Tanggal_Tayang):
        self.ID_Jadwal = ID_Jadwal
        self.ID_Film = ID_Film
        self.ID_Studio = ID_Studio
        self.Jam_Tayang = Jam_Tayang
        self.Tanggal_Tayang = Tanggal_Tayang

class Pemesan:
    def __init__(self, ID_Pemesan, Nama_Lengkap, Email, Nomor_Telepon):
        self.ID_Pemesan = ID_Pemesan
        self.Nama_Lengkap = Nama_Lengkap
        self.Email = Email
        self.Nomor_Telepon = Nomor_Telepon

class Pemesanan:
    def __init__(self, ID_Pemesanan, ID_Jadwal, ID_Pemesan, Harga_Tiket, Jumlah_Tiket, Total_Harga, Status_Pemesanan, Tanggal_Pemesanan):
        self.ID_Pemesanan = ID_Pemesanan
        self.ID_Jadwal = ID_Jadwal
        self.ID_Pemesan = ID_Pemesan
        self.Harga_Tiket = Harga_Tiket
        self.Jumlah_Tiket = Jumlah_Tiket
        self.Total_Harga = Total_Harga
        self.Status_Pemesanan = Status_Pemesanan
        self.Tanggal_Pemesanan = Tanggal_Pemesanan

class Admin:
    def __init__(self, ID_Admin, Username, Password):
        self.ID_Admin = ID_Admin
        self.Username = Username
        self.Password = Password