from classmain import Film
from classmain import Studio

class Query:
    def __init__(self, db) -> None:
        self.db = db

    def insert_admin(self, username, password):
        try:
            sql_admin = "INSERT INTO admin (Username, Password) VALUES (%s, %s)"
            values = (username, password)
            self.db.cur.execute(sql_admin, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_admin: {e}")
            self.db.db.rollback()
            
    def login_admin(self, username, password):
        try:
            sql_login = "SELECT * FROM admin WHERE Username = %s AND Password = %s"
            values = (username, password)
            self.db.cur.execute(sql_login, values)
            result = self.db.cur.fetchone()

            return result is not None
        except Exception as e:
            print(f"Error during login_admin: {e}")
            return False
    
    def insert_film(self, judul, genre, durasi, tanggal_rilis, harga_film):
        try:
            sql_film = "INSERT INTO Film (Judul, Genre, Durasi, Tanggal_Rilis, Harga_Film) VALUES (%s, %s, %s, %s, %s)"
            values = (judul, genre, durasi, tanggal_rilis, harga_film)
            self.db.cur.execute(sql_film, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_film: {e}")
            self.db.db.rollback()
            
    def get_data(self, model):
        try:
            sql_select_all = f"SELECT * FROM {model.__name__}"
            self.db.cur.execute(sql_select_all)

            # Menghasilkan objek model (Film, Studio, dll.) dari setiap baris hasil query
            columns = [column[0] for column in self.db.cur.description]
            data = [model(**dict(zip(columns, row))) for row in self.db.cur.fetchall()]

            return data
        except Exception as e:
            print(f"Error during get_data: {e}")
            
    def cari_data(self, model, field, value):
        try:
            # Construct the SQL query based on the model, field, and value
            sql_query = f"SELECT * FROM {model.__name__} WHERE {field} = %s"
            self.db.cur.execute(sql_query, (value,))
            result = self.db.cur.fetchone()

            if result:
                # Create an instance of the model class using the values from the tuple
                instance = model(*result)
                return instance
            else:
                return None
        except Exception as e:
            print(f"Error during cari_data: {e}")
            return None

    def insert_studio(self, nama_studio, kapasitas, lokasi):
        try:
            sql_studio = "INSERT INTO Studio (Nama_Studio, Kapasitas, Lokasi) VALUES (%s, %s, %s)"
            values = (nama_studio, kapasitas, lokasi)
            self.db.cur.execute(sql_studio, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_studio: {e}")
            self.db.db.rollback()
            
    def get_studio_data(self):
        sql_get_studio = "SELECT * FROM Studio"
        self.db.cur.execute(sql_get_studio)
        results = self.db.cur.fetchall()

        # Convert the tuples to Studio objects
        data_studio = [Studio(*result) for result in results]

        return data_studio
    
    def update_studio(self, id_studio, nama_studio, kapasitas, lokasi):
        try:
            sql_studio = "UPDATE Studio SET Nama_Studio = %s, Kapasitas = %s, Lokasi = %s WHERE ID_Studio = %s"
            values = (nama_studio, kapasitas, lokasi, id_studio)
            self.db.cur.execute(sql_studio, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_studio: {e}")
            self.db.db.rollback()

    def tambah_kapasitas_studio(self, id_studio, jumlah_tiket):
        try:
            # Increase the capacity of the studio based on the number of tickets sold
            query = f"UPDATE Studio SET Kapasitas = Kapasitas + {jumlah_tiket} WHERE ID_Studio = {id_studio};"
            self.db.cur.execute(query)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during tambah_kapasitas_studio: {e}")
            self.db.db.rollback()
    
    def kurangi_kapasitas_studio(self, id_studio, jumlah_tiket):
        try:
        # Mengurangi kapasitas studio berdasarkan jumlah tiket yang dibeli
            query = f"UPDATE Studio SET Kapasitas = Kapasitas - {jumlah_tiket} WHERE ID_Studio = {id_studio};"
            self.db.cur.execute(query)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during kurangi_kapasitas_studio: {e}")
            self.db.db.rollback()
        
    def insert_jadwal(self, id_film, id_studio, jam_tayang, tanggal_tayang):
        try:
            sql_jadwal = "INSERT INTO Jadwal (ID_Film, ID_Studio, Jam_Tayang, Tanggal_Tayang) VALUES (%s, %s, %s, %s)"
            values = (id_film, id_studio, jam_tayang, tanggal_tayang)
            self.db.cur.execute(sql_jadwal, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_jadwal: {e}")
            self.db.db.rollback()

    def insert_pemesan(self, nama_lengkap, email, nomor_telepon):
        try:
            sql_pemesan = "INSERT INTO Pemesan (Nama_Lengkap, Email, Nomor_Telepon) VALUES (%s, %s, %s)"
            values = (nama_lengkap, email, nomor_telepon)
            self.db.cur.execute(sql_pemesan, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_pemesan: {e}")
            self.db.db.rollback()

    def insert_pemesanan(self, id_jadwal, id_pemesan, harga_tiket, jumlah_tiket, total_harga, status_pemesanan, tanggal_pemesanan):
        try:
            sql_pemesanan = "INSERT INTO Pemesanan (ID_Jadwal, ID_Pemesan, Harga_Tiket, Jumlah_Tiket, Total_Harga, Status_Pemesanan, Tanggal_Pemesanan) " \
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (id_jadwal, id_pemesan, harga_tiket, jumlah_tiket, total_harga, status_pemesanan, tanggal_pemesanan)
            self.db.cur.execute(sql_pemesanan, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_pemesanan: {e}")
            self.db.db.rollback()

    def insert_pembatalan_pesanan(self, id_pemesanan, alasan_pembatalan, tanggal_pembatalan):
        try:
            sql_pembatalan = "INSERT INTO Pembatalan_Pesanan (ID_Pemesanan, Alasan_Pembatalan, Tanggal_Pembatalan) " \
                              "VALUES (%s, %s, %s)"
            values = (id_pemesanan, alasan_pembatalan, tanggal_pembatalan)
            self.db.cur.execute(sql_pembatalan, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_pembatalan_pesanan: {e}")
            self.db.db.rollback()

    def select_film(self, judul):
        sql_film = "SELECT * FROM Film WHERE Judul = %s"
        self.db.cur.execute(sql_film, (judul,))
        result = self.db.cur.fetchone()

        if result:
            film = Film(*result)
            return film
        else:
            return None

    def select_studio(self, id_studio):
        sql_studio = "SELECT * FROM Studio WHERE ID_Studio = %s"
        self.db.cur.execute(sql_studio, (id_studio,))
        return self.db.cur.fetchone()

    def select_jadwal(self, id_jadwal):
        sql_jadwal = "SELECT * FROM Jadwal WHERE ID_Jadwal = %s"
        self.db.cur.execute(sql_jadwal, (id_jadwal,))
        return self.db.cur.fetchone()

    def select_pemesan(self, id_pemesan):
        sql_pemesan = "SELECT * FROM Pemesan WHERE ID_Pemesan = %s"
        self.db.cur.execute(sql_pemesan, (id_pemesan,))
        return self.db.cur.fetchone()

    def select_pemesanan(self, id_pemesanan):
        sql_pemesanan = "SELECT * FROM Pemesanan WHERE ID_Pemesanan = %s"
        self.db.cur.execute(sql_pemesanan, (id_pemesanan,))
        return self.db.cur.fetchone()

    def select_pembatalan_pesanan(self, id_pembatalan):
        sql_pembatalan = "SELECT * FROM Pembatalan_Pesanan WHERE ID_Pembatalan = %s"
        self.db.cur.execute(sql_pembatalan, (id_pembatalan,))
        return self.db.cur.fetchone()

    def select_all_film(self):
        sql_all_film = "SELECT * FROM Film"
        self.db.cur.execute(sql_all_film)
        return self.db.cur.fetchall()

    def select_all_studio(self):
        sql_all_studio = "SELECT * FROM Studio"
        self.db.cur.execute(sql_all_studio)
        return self.db.cur.fetchall()

    def select_all_jadwal(self):
        sql_all_jadwal = "SELECT * FROM Jadwal"
        self.db.cur.execute(sql_all_jadwal)
        return self.db.cur.fetchall()

    def select_all_pemesan(self):
        sql_all_pemesan = "SELECT * FROM Pemesan"
        self.db.cur.execute(sql_all_pemesan)
        return self.db.cur.fetchall()

    def select_all_pemesanan(self):
        sql_all_pemesanan = "SELECT * FROM Pemesanan"
        self.db.cur.execute(sql_all_pemesanan)
        return self.db.cur.fetchall()

    def select_all_pembatalan_pesanan(self):
        sql_all_pembatalan_pesanan = "SELECT * FROM Pembatalan_Pesanan"
        self.db.cur.execute(sql_all_pembatalan_pesanan)
        return self.db.cur.fetchall()

    def update_film(self, id_film, judul, genre, durasi, tanggal_rilis):
        try:
            sql_film = "UPDATE Film SET Judul = %s, Genre = %s, Durasi = %s, Tanggal_Rilis = %s WHERE ID_Film = %s"
            values = (judul, genre, durasi, tanggal_rilis, id_film)
            self.db.cur.execute(sql_film, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_film: {e}")
            self.db.db.rollback()

    def update_jadwal(self, id_jadwal, jam_tayang, tanggal_tayang):
        try:
            sql_jadwal = "UPDATE Jadwal SET Jam_Tayang = %s, Tanggal_Tayang = %s WHERE ID_Jadwal = %s"
            values = (jam_tayang, tanggal_tayang, id_jadwal)
            self.db.cur.execute(sql_jadwal, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_jadwal: {e}")
            self.db.db.rollback()

    def update_pemesan(self, id_pemesan, nama_lengkap, email, nomor_telepon):
        try:
            sql_pemesan = "UPDATE Pemesan SET Nama_Lengkap = %s, Email = %s, Nomor_Telepon = %s WHERE ID_Pemesan = %s"
            values = (nama_lengkap, email, nomor_telepon, id_pemesan)
            self.db.cur.execute(sql_pemesan, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_pemesan: {e}")
            self.db.db.rollback()

    def update_pemesanan(self, id_pemesanan, status_pemesanan):
        try:
            sql_pemesanan = "UPDATE Pemesanan SET Status_Pemesanan = %s WHERE ID_Pemesanan = %s"
            values = (status_pemesanan, id_pemesanan)
            self.db.cur.execute(sql_pemesanan, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_pemesanan: {e}")
            self.db.db.rollback()

    def delete_film(self, id_film):
        try:
            sql_film = "DELETE FROM Film WHERE ID_Film = %s"
            self.db.cur.execute(sql_film, (id_film,))
            self.db.db.commit()
        except Exception as e:
            print(f"Error during delete_film: {e}")
            self.db.db.rollback()

    def delete_studio(self, id_studio):
        try:
            sql_studio = "DELETE FROM Studio WHERE ID_Studio = %s"
            self.db.cur.execute(sql_studio, (id_studio,))
            self.db.db.commit()
        except Exception as e:
            print(f"Error during delete_studio: {e}")
            self.db.db.rollback()

    def delete_jadwal(self, id_jadwal):
        try:
            sql_jadwal = "DELETE FROM Jadwal WHERE ID_Jadwal = %s"
            self.db.cur.execute(sql_jadwal, (id_jadwal,))
            self.db.db.commit()
        except Exception as e:
            print(f"Error during delete_jadwal: {e}")
            self.db.db.rollback()

    def delete_pemesan(self, id_pemesan):
        try:
            sql_pemesan = "DELETE FROM Pemesan WHERE ID_Pemesan = %s"
            self.db.cur.execute(sql_pemesan, (id_pemesan,))
            self.db.db.commit()
        except Exception as e:
            print(f"Error during delete_pemesan: {e}")
            self.db.db.rollback()

    def delete_pemesanan(self, id_pemesanan):
        try:
            sql_pemesanan = "DELETE FROM Pemesanan WHERE ID_Pemesanan = %s"
            self.db.cur.execute(sql_pemesanan, (id_pemesanan,))
            self.db.db.commit()
        except Exception as e:
            print(f"Error during delete_pemesanan: {e}")
            self.db.db.rollback()

    