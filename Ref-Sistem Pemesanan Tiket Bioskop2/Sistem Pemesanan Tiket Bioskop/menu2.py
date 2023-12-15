from connect import Database
from query import Query
from classmain import Film, Studio, Jadwal, Pemesan, Pemesanan

class Menu:
    def __init__(self):
        self.db = Database()
        self.query = Query(self.db)

    def main_menu(self):
        while True:
            print("\n===== Menu Utama =====")
            print("1. Registrasi Admin")
            print("2. Admin")
            print("3. User")
            print("4. Keluar")

            choice = input("Pilih menu (1-4): ")

            if choice == "1":
                self.registrasi_admin()
            elif choice == "2":
                self.menu_admin()
            elif choice == "3":
                self.menu_user()
            elif choice == "4":
                print("Terimakasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def registrasi_admin(self):
        print("\n===== Registrasi Admin =====")
        username = input("Masukkan Username Admin: ")
        password = input("Masukkan Password Admin: ")

        # Insert admin registration logic here
        self.query.insert_admin(username, password)
        print("Admin berhasil diregistrasi!")

    def menu_admin(self):
        username = input("Masukkan Username Admin: ")
        password = input("Masukkan Password Admin: ")

        # Check if the entered username and password match the admin records
        if self.query.login_admin(username, password):
            print("Login berhasil!")

            while True:
                print("\n===== Menu Admin =====")
                print("a. Film")
                print("b. Studio")
                print("c. Jadwal Film")
                print("d. Data Pemesan")
                print("e. Pemesanan Tiket Film")
                print("f. Kembali ke Menu Admin")
                print("g. Keluar")

                choice_admin = input("Pilih menu (a-g): ")

                if choice_admin == "a":
                    self.menu_film()
                elif choice_admin == "b":
                    self.menu_studio()
                elif choice_admin == "c":
                    self.menu_jadwal()
                elif choice_admin == "d":
                    self.menu_pemesan()
                elif choice_admin == "e":
                    self.menu_pemesanan()
                elif choice_admin == "f":
                    self.main_menu()
                elif choice_admin == "g":
                    print("Terimakasih!")
                    exit()
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
        else:
            print("Username atau password salah. Silakan coba lagi.")
            
    def menu_user(self):
        while True:
            print("\n===== Menu User =====")
            print("a. Data Pemesan")
            print("b. Pemesanan Tiket Film")
            print("c. Kembali ke Menu Utama")
            print("d. Keluar")
                
            choice_user = input("Pilih menu (a-g): ")

            if choice_user == "a":
                self.menu_pemesan()
            elif choice_user == "b":
                self.menu_pemesanan()
            elif choice_user == "c":
                self.main_menu()
            elif choice_user == "d":
                print("Terimakasih!")
                exit()
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
       
    def menu_film(self):
        while True:
            print("\n===== Menu Film =====")
            print("1. Tambah Film")
            print("2. Tampilkan Seluruh Film")
            print("3. Ubah Film")
            print("4. Hapus Film")
            print("5. Kembali ke Menu Utama")

            choice = input("Pilih menu (1-5): ")

            if choice == "1":
                self.tambah_film()
            elif choice == "2":
                self.tampilkan_seluruh_film()
            elif choice == "3":
                self.ubah_film()
            elif choice == "4":
                self.hapus_film()
            elif choice == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def tambah_film(self):
        judul = input("Masukkan Judul Film: ")
        genre = input("Masukkan Genre Film: ")
        durasi = int(input("Masukkan Durasi Film (dalam menit): "))
        tanggal_rilis = input("Masukkan Tanggal Rilis Film (YYYY-MM-DD): ")
        harga_film = float(input("Masukkan Harga Film: "))

        self.query.insert_film(judul, genre, durasi, tanggal_rilis, harga_film)
        print("Film berhasil ditambahkan!")

    def tampilkan_seluruh_film(self):
        print("\n===== Seluruh Film =====")
        data_film = self.query.get_data(Film)

        if not data_film:
            print("Tidak ada data film.")
        else:
            for film in data_film:
                # Menampilkan seluruh atribut film
                print(f"ID_Film: {film.ID_Film}, Judul: {film.Judul}, Genre: {film.Genre}, Durasi: {film.Durasi} menit, Tanggal Rilis: {film.Tanggal_Rilis}, Harga Film: {film.Harga_Film}")
                
    def ubah_film(self):
        print("\n===== Ubah Film =====")
        judul = input("Masukkan judul film yang ingin diubah: ")

        # Mengecek apakah film dengan judul tersebut ada
        film = self.query.select_film(judul)

        if film:
            # Menampilkan data film sebelum diubah
            print(f"Data film sebelum diubah: ID_Film: {film.ID_Film}, Judul: {film.Judul}, Genre: {film.Genre}, Durasi: {film.Durasi} menit, Tanggal Rilis: {film.Tanggal_Rilis}, Harga Film: {film.Harga_Film}")

            # Mengambil input baru dari pengguna
            new_judul = input("Masukkan judul baru (kosongkan jika tidak diubah): ")
            new_genre = input("Masukkan genre baru (kosongkan jika tidak diubah): ")
            new_durasi = input("Masukkan durasi baru (kosongkan jika tidak diubah): ")
            new_tanggal_rilis = input("Masukkan tanggal rilis baru (YYYY-MM-DD) (kosongkan jika tidak diubah): ")

            # Mengubah data film
            if new_judul:
                film.Judul = new_judul
            if new_genre:
                film.Genre = new_genre
            if new_durasi:
                film.Durasi = new_durasi
            if new_tanggal_rilis:
                film.Tanggal_Rilis = new_tanggal_rilis

            # Menyimpan perubahan ke database
            self.query.update_film(film.ID_Film, film.Judul, film.Genre, film.Durasi, film.Tanggal_Rilis)

            print("Data film berhasil diubah!")
        else:
            print(f"Film dengan judul {judul} tidak ditemukan.")

    def hapus_film(self):
        print("\n===== Hapus Film =====")
        judul = input("Masukkan judul film yang ingin dihapus: ")

        # Mengecek apakah film dengan judul tersebut ada
        film = self.query.cari_data(Film, "Judul", judul)

        if film:
            # Menampilkan data film sebelum dihapus
            print(f"Data film sebelum dihapus: ID_Film: {film.ID_Film}, Judul: {film.Judul}, Genre: {film.Genre}, Durasi: {film.Durasi} menit")

            # Konfirmasi pengguna
            konfirmasi = input("Apakah Anda yakin ingin menghapus film ini? (y/n): ")

            if konfirmasi.lower() == "y":
                # Menghapus film dari database
                self.query.delete_film(film.ID_Film)

                print("Film berhasil dihapus!")
        else:
            print(f"Film dengan judul {judul} tidak ditemukan.")

    def menu_studio(self):
        while True:
            print("\n===== Menu Studio =====")
            print("1. Tambah Studio")
            print("2. Tampilkan Studio")
            print("3. Ubah Studio")
            print("4. Hapus Studio")
            print("5. Kembali ke Menu Utama")

            choice = input("Pilih menu (1-5): ")

            if choice == "1":
                self.tambah_studio()
            elif choice == "2":
                self.tampilkan_studio()
            elif choice == "3":
                self.ubah_studio()
            elif choice == "4":
                self.hapus_studio()
            elif choice == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def tambah_studio(self):
        print("\n===== Tambah Studio =====")
        nama_studio = input("Masukkan Nama Studio: ")
        kapasitas = int(input("Masukkan Kapasitas Studio: "))
        lokasi = input("Masukkan Lokasi Studio: ")  # Add this line to get the missing 'lokasi'

        # Modify the call to include the missing 'lokasi' argument
        self.query.insert_studio(nama_studio, kapasitas, lokasi)
        print("Studio berhasil ditambahkan!")

    def tampilkan_studio(self):
        print("\n===== Seluruh Studio =====")
        data_studio = self.query.get_studio_data()

        if not data_studio:
            print("Tidak ada data studio.")
        else:
            for studio in data_studio:
                # Print the studio information directly
                print(f"ID_Studio: {studio.ID_Studio}, Nama Studio: {studio.Nama_Studio}, Kapasitas: {studio.Kapasitas}, Lokasi: {studio.Lokasi}")

    def ubah_studio(self):
        print("\n===== Ubah Studio =====")
        id_studio = int(input("Masukkan ID Studio yang ingin diubah: "))

    # Mengecek apakah studio dengan ID tersebut ada
        studio = self.query.cari_data(Studio, "ID_Studio", id_studio)

        if studio:
        # Menampilkan data studio sebelum diubah
            print(f"Data studio sebelum diubah: Nama Studio: {studio.Nama_Studio}, Kapasitas: {studio.Kapasitas}, Lokasi: {studio.Lokasi}")

        # Mengambil input baru dari pengguna
            new_nama_studio = input("Masukkan nama studio baru (kosongkan jika tidak diubah): ")
            new_kapasitas = input("Masukkan kapasitas baru (kosongkan jika tidak diubah): ")
            new_lokasi = input("Masukkan lokasi baru (kosongkan jika tidak diubah): ")

        # Mengubah data studio
            if new_nama_studio:
                studio.Nama_Studio = new_nama_studio
            if new_kapasitas:
                studio.Kapasitas = new_kapasitas
            if new_lokasi:
                studio.Lokasi = new_lokasi

        # Menyimpan perubahan ke database
            self.query.update_studio(studio.ID_Studio, studio.Nama_Studio, studio.Kapasitas, studio.Lokasi)

            print("Data studio berhasil diubah!")
        else:
            print(f"Studio dengan ID {id_studio} tidak ditemukan.")


    def hapus_studio(self):
        print("\n===== Hapus Studio =====")
        id_studio = int(input("Masukkan ID Studio yang ingin dihapus: "))

        # Mengecek apakah studio dengan ID tersebut ada
        studio = self.query.cari_data(Studio, "ID_Studio", id_studio)

        if studio:
            # Menampilkan data studio sebelum dihapus
            print(f"Data studio sebelum dihapus: Nama Studio: {studio.Nama_Studio}, Kapasitas: {studio.Kapasitas}, Lokasi: {studio.Lokasi}")

            # Konfirmasi pengguna
            konfirmasi = input("Apakah Anda yakin ingin menghapus studio ini? (y/n): ")

            if konfirmasi.lower() == "y":
                # Menghapus studio dari database
                self.query.delete_studio(id_studio)

                print("Studio berhasil dihapus!")
        else:
            print(f"Studio dengan ID {id_studio} tidak ditemukan.")

    def menu_jadwal(self):
        while True:
            print("\n===== Menu Jadwal Film =====")
            print("1. Tambah Jadwal Film")
            print("2. Tampilkan Jadwal Film")
            print("3. Ubah Jadwal Film")
            print("4. Hapus Jadwal Film")
            print("5. Kembali ke Menu Utama")

            choice = input("Pilih menu (1-5): ")

            if choice == "1":
                self.tambah_jadwal()
            elif choice == "2":
                self.tampilkan_jadwal()
            elif choice == "3":
                self.ubah_jadwal()
            elif choice == "4":
                self.hapus_jadwal()
            elif choice == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def tambah_jadwal(self):
        print("\n===== Tambah Jadwal Film =====")
    
    # Display existing films for user reference
        self.tampilkan_seluruh_film()

    # Get the film ID from the user
        id_film = int(input("Masukkan ID Film yang ingin ditambahkan jadwal: "))
    
    # Check if the film with the given ID exists
        film = self.query.cari_data(Film, "ID_Film", id_film)

        if not film:
            print(f"Film dengan ID {id_film} tidak ditemukan.")
            return

    # Display existing studios for user reference
        self.tampilkan_studio()

    # Get the studio ID from the user
        id_studio = int(input("Masukkan ID Studio yang ingin ditambahkan jadwal: "))
    
    # Check if the studio with the given ID exists
        studio = self.query.cari_data(Studio, "ID_Studio", id_studio)

        if not studio:
            print(f"Studio dengan ID {id_studio} tidak ditemukan.")
            return

    # Get the remaining input from the user
        tanggal_tayang = input("Masukkan Tanggal Tayang (YYYY-MM-DD): ")
        jam_tayang = input("Masukkan Jam Tayang (HH:MM): ")

    # Insert the new schedule into the database
        self.query.insert_jadwal(id_film, id_studio, jam_tayang, tanggal_tayang)

        print("Jadwal Film berhasil ditambahkan!")


    def tampilkan_jadwal(self):
        print("\n===== Seluruh Jadwal Film =====")
    
    # Retrieve all schedules from the database
        data_jadwal = self.query.get_data(Jadwal)

        if not data_jadwal:
            print("Tidak ada jadwal film.")
        else:
            for jadwal in data_jadwal:
            # Retrieve film information
                film = self.query.cari_data(Film, "ID_Film", jadwal.ID_Film)

            # Retrieve studio information
                studio = self.query.cari_data(Studio, "ID_Studio", jadwal.ID_Studio)

                if film and studio:
                # Print the schedule information along with film and studio details
                    print(f"ID_Jadwal: {jadwal.ID_Jadwal}, Tanggal Tayang: {jadwal.Tanggal_Tayang}, Jam Tayang: {jadwal.Jam_Tayang}")
                    print(f"   Film: {film.Judul}, Genre: {film.Genre}, Durasi: {film.Durasi} menit")
                    print(f"   Studio: {studio.Nama_Studio}, Kapasitas: {studio.Kapasitas}, Lokasi: {studio.Lokasi}")
                    print()
                else:
                    print(f"Jadwal dengan ID {jadwal.ID_Jadwal} memiliki ID_Film atau ID_Studio yang tidak valid.")

    def ubah_jadwal(self):
        print("\n===== Ubah Jadwal Film =====")
        id_jadwal = int(input("Masukkan ID Jadwal yang ingin diubah: "))

    # Mengecek apakah jadwal dengan ID tersebut ada
        jadwal = self.query.cari_data(Jadwal, "ID_Jadwal", id_jadwal)

        if jadwal:
        # Menampilkan data jadwal sebelum diubah
            print(f"Data jadwal sebelum diubah: Tanggal Tayang: {jadwal.Tanggal_Tayang}, Jam Tayang: {jadwal.Jam_Tayang}")

        # Mengambil input baru dari pengguna
            new_tanggal_tayang = input("Masukkan tanggal tayang baru (YYYY-MM-DD) (kosongkan jika tidak diubah): ")
            new_jam_tayang = input("Masukkan jam tayang baru (HH:MM) (kosongkan jika tidak diubah): ")

        # Mengubah data jadwal
            if new_tanggal_tayang:
                jadwal.Tanggal_Tayang = new_tanggal_tayang
            if new_jam_tayang:
                jadwal.Jam_Tayang = new_jam_tayang

        # Menyimpan perubahan ke database
            self.query.update_jadwal(jadwal.ID_Jadwal, jadwal.Tanggal_Tayang, jadwal.Jam_Tayang)

            print("Data jadwal berhasil diubah!")
        else:
            print(f"Jadwal dengan ID {id_jadwal} tidak ditemukan.")

    def hapus_jadwal(self):
        print("\n===== Hapus Jadwal Film =====")
        id_jadwal = int(input("Masukkan ID Jadwal yang ingin dihapus: "))

    # Mengecek apakah jadwal dengan ID tersebut ada
        jadwal = self.query.cari_data(Jadwal, "ID_Jadwal", id_jadwal)

        if jadwal:
        # Menampilkan data jadwal sebelum dihapus
            print(f"Data jadwal sebelum dihapus: Tanggal Tayang: {jadwal.Tanggal_Tayang}, Jam Tayang: {jadwal.Jam_Tayang}")

        # Konfirmasi pengguna
            konfirmasi = input("Apakah Anda yakin ingin menghapus jadwal ini? (y/n): ")

            if konfirmasi.lower() == "y":
            # Menghapus jadwal dari database
                self.query.delete_jadwal(id_jadwal)

                print("Jadwal berhasil dihapus!")
        else:
            print(f"Jadwal dengan ID {id_jadwal} tidak ditemukan.")

    def menu_pemesan(self):
        while True:
            print("\n===== Menu Data Pemesan =====")
            print("1. Tambah Data Pemesan")
            print("2. Tampilkan Data Pemesan")
            print("3. Ubah Data Pemesan")
            print("4. Hapus Data Pemesan")
            print("5. Kembali ke Menu Utama")

            choice = input("Pilih menu (1-5): ")

            if choice == "1":
                self.tambah_pemesan()
            elif choice == "2":
                self.tampilkan_pemesan()
            elif choice == "3":
                self.ubah_pemesan()
            elif choice == "4":
                self.hapus_pemesan()
            elif choice == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def tambah_pemesan(self):
        print("\n===== Tambah Data Pemesan =====")
        nama = input("Masukkan Nama Lengkap Pemesan: ")
        email = input("Masukkan Alamat Email: ")
        no_telepon = input("Masukkan Nomor Telepon Pemesan: ")

        self.query.insert_pemesan(nama, email, no_telepon)
        print("Data Pemesan berhasil ditambahkan!")

    def tampilkan_pemesan(self):
        print("\n===== Seluruh Data Pemesan =====")
        data_pemesan = self.query.get_data(Pemesan)

        if not data_pemesan:
            print("Tidak ada data pemesan.")
        else:
            for pemesan in data_pemesan:
                # Menampilkan seluruh atribut pemesan
                print(f"ID_Pemesan: {pemesan.ID_Pemesan}, Nama: {pemesan.Nama_Lengkap}, Email: {pemesan.Email}, No. Telepon: {pemesan.Nomor_Telepon}")
    
    def ubah_pemesan(self):
        print("\n===== Ubah Data Pemesan =====")
        id_pemesan = int(input("Masukkan ID Pemesan yang ingin diubah: "))

        # Mengecek apakah pemesan dengan ID tersebut ada
        pemesan = self.query.cari_data(Pemesan, "ID_Pemesan", id_pemesan)

        if pemesan:
            # Menampilkan data pemesan sebelum diubah
            print(f"Data pemesan sebelum diubah: Nama: {pemesan.Nama_Lengkap}, Email: {pemesan.Email}, No. Telepon: {pemesan.Nomor_Telepon}")

            # Mengambil input baru dari pengguna
            new_nama = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
            new_email = input("Masukkan email baru (kosongkan jika tidak diubah): ")
            new_no_telepon = input("Masukkan nomor telepon baru (kosongkan jika tidak diubah): ")

            # Mengubah data pemesan
            if new_nama:
                pemesan.Nama_Lengkap = new_nama
            if new_email:
                pemesan.Email = new_email
            if new_no_telepon:
                pemesan.Nomor_Telepon = new_no_telepon

            # Menyimpan perubahan ke database
            self.query.update_pemesan(pemesan.ID_Pemesan, pemesan.Nama_Lengkap, pemesan.Email, pemesan.Nomor_Telepon)

            print("Data pemesan berhasil diubah!")
        else:
            print(f"Pemesan dengan ID {id_pemesan} tidak ditemukan.")


    def hapus_pemesan(self):
        print("\n===== Hapus Data Pemesan =====")
        id_pemesan = int(input("Masukkan ID Pemesan yang ingin dihapus: "))

        # Mengecek apakah pemesan dengan ID tersebut ada
        pemesan = self.query.cari_data(Pemesan, "ID_Pemesan", id_pemesan)

        if pemesan:
            # Menampilkan data pemesan sebelum dihapus
            print(f"Data pemesan sebelum dihapus: Nama: {pemesan.Nama_Lengkap}, Email: {pemesan.Email}, No. Telepon: {pemesan.Nomor_Telepon}")

            # Konfirmasi pengguna
            konfirmasi = input("Apakah Anda yakin ingin menghapus pemesan ini? (y/n): ")

            if konfirmasi.lower() == "y":
                # Menghapus pemesan dari database
                self.query.delete_pemesan(id_pemesan)

                print("Data pemesan berhasil dihapus!")
        else:
            print(f"Pemesan dengan ID {id_pemesan} tidak ditemukan.")

    def menu_pemesanan(self):
        while True:
            print("\n===== Menu Pemesanan Tiket Film =====")
            print("1. Beli Tiket")
            print("2. Tampilkan Data Pembeli")
            print("3. Tampilkan Data Seluruh Pembeli")
            print("4. Batalkan Pesanan")
            print("5. Kembali ke Menu Utama")

            choice = input("Pilih menu (1-5): ")

            if choice == "1":
                self.beli_tiket()
            elif choice == "2":
                self.tampilkan_data_pembeli()
            elif choice == "3":
                self.tampilkan_data_seluruh_pembeli()
            elif choice == "4":
                self.batalkan_pesanan()
            elif choice == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def beli_tiket(self):
        print("\n===== Beli Tiket =====")

        # Menampilkan seluruh daftar film
        self.tampilkan_seluruh_film()

        # Menampilkan seluruh daftar studio
        self.tampilkan_studio()

        # Menampilkan seluruh jadwal film
        self.tampilkan_jadwal()

        # Memasukkan ID_Jadwal yang ingin dibeli tiket
        id_jadwal = int(input("Masukkan ID Jadwal yang ingin dibeli tiket: "))

        # Menampilkan keterangan lengkap film, jadwal, studio, dan jam tayang
        jadwal = self.query.cari_data(Jadwal, "ID_Jadwal", id_jadwal)

        if jadwal:
            film = self.query.cari_data(Film, "ID_Film", jadwal.ID_Film)
            studio = self.query.cari_data(Studio, "ID_Studio", jadwal.ID_Studio)

            if film and studio:
                print("\n===== Detail Pembelian =====")
                print(f"Nama Film: {film.Judul}")
                print(f"Jadwal: {jadwal.Tanggal_Tayang} {jadwal.Jam_Tayang}")
                print(f"Studio: {studio.Nama_Studio} (Kapasitas: {studio.Kapasitas} kursi)")
                print(f"Harga Tiket: {film.Harga_Film}")
                print("\n===== Data Pemesan =====")

                # Menampilkan seluruh daftar pemesan
                self.tampilkan_pemesan()

                # Memasukkan ID_Pemesan yang sudah ada
                id_pemesan = int(input("Masukkan ID Pemesan yang ingin membeli tiket: "))

                # Menentukan jumlah tiket yang ingin dibeli
                jumlah_tiket = int(input("Masukkan Jumlah Tiket yang Ingin Dibeli: "))

                # Mengecek apakah jumlah tiket yang ingin dibeli tidak melebihi kapasitas studio
                if jumlah_tiket > studio.Kapasitas:
                    print("Maaf, jumlah tiket melebihi kapasitas studio yang tersedia.")
                    return


                # Mengurangi kapasitas studio
                self.query.kurangi_kapasitas_studio(jadwal.ID_Studio, jumlah_tiket)

                # Menghitung total harga tiket
                total_harga = jumlah_tiket * film.Harga_Film

                # Memasukkan tanggal_pemesanan
                tanggal_pemesanan = input("Masukkan Tanggal Pemesanan (YYYY-MM-DD): ")

                # Menambah data pemesanan
                self.query.insert_pemesanan(id_jadwal, id_pemesan, film.Harga_Film, jumlah_tiket, total_harga, 'berhasil', tanggal_pemesanan)

                # Menampilkan seluruh daftar pembelian total
                print("\n===== Daftar Pembelian Total =====")
                data_pembelian = self.query.get_data(Pemesanan)

                for pembelian in data_pembelian:    
                # Menampilkan keterangan lengkap pembelian
                    jadwal_pembelian = self.query.cari_data(Jadwal, "ID_Jadwal", pembelian.ID_Jadwal)
                    film_pembelian = self.query.cari_data(Film, "ID_Film", jadwal_pembelian.ID_Film)
                    studio_pembelian = self.query.cari_data(Studio, "ID_Studio", jadwal_pembelian.ID_Studio)
                    pemesan_pembelian = self.query.cari_data(Pemesan, "ID_Pemesan", pembelian.ID_Pemesan)

                    if jadwal_pembelian and film_pembelian and studio_pembelian and pemesan_pembelian:
                        print(f"ID_Pemesanan: {pembelian.ID_Pemesanan}, Nama Pemesan: {pemesan_pembelian.Nama_Lengkap}, Film: {film_pembelian.Judul}, Studio: {studio_pembelian.Nama_Studio}, Jumlah Tiket: {pembelian.Jumlah_Tiket}, Total Harga: {pembelian.Total_Harga}, Tanggal Pemesanan: {pembelian.Tanggal_Pemesanan}")
                    else:
                        print(f"Pemesanan dengan ID {pembelian.ID_Pemesanan} memiliki ID_Jadwal, ID_Pemesan, atau ID_Studio yang tidak valid.")

                # Konfirmasi pembelian
                konfirmasi = input("Apakah Anda yakin ingin melanjutkan pembelian? (y/n): ")

                if konfirmasi.lower() == "y":
                    print("Pembelian berhasil!")
                else:
                    # Mengembalikan kapasitas studio jika pembelian dibatalkan
                    self.query.tambah_kapasitas_studio(jadwal.ID_Studio, jumlah_tiket)
                    print("Pembelian dibatalkan.")
            else:
                print(f"Jadwal dengan ID {id_jadwal} memiliki ID_Film atau ID_Studio yang tidak valid.")
        else:
            print(f"Jadwal dengan ID {id_jadwal} tidak ditemukan.")

    def tampilkan_data_pembeli(self):
        print("\n===== Tampilkan Data Pembeli =====")
        id_pemesanan = int(input("Masukkan ID Pemesanan yang ingin ditampilkan: "))

    # Mengecek apakah pemesanan dengan ID tersebut ada
        pemesanan = self.query.cari_data(Pemesanan, "ID_Pemesanan", id_pemesanan)

        if pemesanan:
        # Menampilkan keterangan lengkap pembelian
            jadwal_pembelian = self.query.cari_data(Jadwal, "ID_Jadwal", pemesanan.ID_Jadwal)
            film_pembelian = self.query.cari_data(Film, "ID_Film", jadwal_pembelian.ID_Film)
            studio_pembelian = self.query.cari_data(Studio, "ID_Studio", jadwal_pembelian.ID_Studio)
            pemesan_pembelian = self.query.cari_data(Pemesan, "ID_Pemesan", pemesanan.ID_Pemesan)

            if jadwal_pembelian and film_pembelian and studio_pembelian and pemesan_pembelian:
                print(f"ID_Pemesanan: {pemesanan.ID_Pemesanan}, Nama Pemesan: {pemesan_pembelian.Nama_Lengkap}, Film: {film_pembelian.Judul}, Studio: {studio_pembelian.Nama_Studio}, Jumlah Tiket: {pemesanan.Jumlah_Tiket}, Total Harga: {pemesanan.Total_Harga}, Tanggal Pemesanan: {pemesanan.Tanggal_Pemesanan}")
            else:
                print(f"Pemesanan dengan ID {pemesanan.ID_Pemesanan} memiliki ID_Jadwal, ID_Pemesan, atau ID_Studio yang tidak valid.")
        else:
            print(f"Pemesanan dengan ID {id_pemesanan} tidak ditemukan.")

    def tampilkan_data_seluruh_pembeli(self):
        print("\n===== Tampilkan Data Seluruh Pembeli =====")
    
    # Mengambil seluruh data pemesanan
        data_pemesanan = self.query.get_data(Pemesanan)

        if not data_pemesanan:
            print("Tidak ada data pemesanan.")
        else:
            for pemesanan in data_pemesanan:
            # Menampilkan keterangan lengkap pembelian
                jadwal_pembelian = self.query.cari_data(Jadwal, "ID_Jadwal", pemesanan.ID_Jadwal)
                film_pembelian = self.query.cari_data(Film, "ID_Film", jadwal_pembelian.ID_Film)
                studio_pembelian = self.query.cari_data(Studio, "ID_Studio", jadwal_pembelian.ID_Studio)
                pemesan_pembelian = self.query.cari_data(Pemesan, "ID_Pemesan", pemesanan.ID_Pemesan)

            if jadwal_pembelian and film_pembelian and studio_pembelian and pemesan_pembelian:
                print(f"ID_Pemesanan: {pemesanan.ID_Pemesanan}, Nama Pemesan: {pemesan_pembelian.Nama_Lengkap}, Film: {film_pembelian.Judul}, Studio: {studio_pembelian.Nama_Studio}, Jumlah Tiket: {pemesanan.Jumlah_Tiket}, Total Harga: {pemesanan.Total_Harga}, Tanggal Pemesanan: {pemesanan.Tanggal_Pemesanan}")
            else:
                print(f"Pemesanan dengan ID {pemesanan.ID_Pemesanan} memiliki ID_Jadwal, ID_Pemesan, atau ID_Studio yang tidak valid.")

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()

       