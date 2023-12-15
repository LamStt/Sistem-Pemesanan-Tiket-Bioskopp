import mysql.connector

class Database:
    def __init__(self, host="localhost", user="root", passwd="", database="db_bioskop4"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.connect()

    def connect(self):
        try:
            self.db = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd
            )
            self.cur = self.db.cursor()

            # Pindahkan inisialisasi koneksi ke database ke sini
            self.db.database = self.database
            self.cur.execute(f"USE {self.database}")

        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.create_database()
            else:
                raise

    def create_database(self):
        try:
            create_db_query = f"CREATE DATABASE {self.database}"
            create_db_cursor = self.db.cursor()
            create_db_cursor.execute(create_db_query)
            create_db_cursor.close()

            # Setelah membuat database, gunakan database yang baru dibuat
            self.db.database = self.database
            self.cur.execute(f"USE {self.database}")

        except mysql.connector.Error as err:
            print(f"Gagal membuat database: {err}")
            raise

    def create_tables(self):
        self.create_table_admin()
        self.create_table_film()
        self.create_table_studio()
        self.create_table_jadwal()
        self.create_table_pemesan()
        self.create_table_pemesanan()
        
    def create_table_admin(self):
        query = '''
            CREATE TABLE IF NOT EXISTS admin (
                ID_Admin INT AUTO_INCREMENT PRIMARY KEY,
                Username VARCHAR(255) NOT NULL,
                Password VARCHAR(255) NOT NULL
            );
        '''
        self.cur.execute(query)
        self.db.commit()

    def create_table_film(self):
        query = '''
            CREATE TABLE IF NOT EXISTS film (
                ID_Film INT AUTO_INCREMENT PRIMARY KEY,
                Judul VARCHAR(255) NOT NULL,
                Genre VARCHAR(255) NOT NULL,
                Durasi INT NOT NULL,
                Tanggal_Rilis DATE NOT NULL,
                Harga_Film INT(10) NOT NULL
            );
        '''
        self.cur.execute(query)
        self.db.commit()

    def create_table_studio(self):
        query = '''
            CREATE TABLE IF NOT EXISTS studio (
                ID_Studio INT AUTO_INCREMENT PRIMARY KEY,
                Nama_Studio VARCHAR(255) NOT NULL,
                Kapasitas INT NOT NULL,
                Lokasi VARCHAR(255) NOT NULL
            );
        '''
        self.cur.execute(query)
        self.db.commit()

    def create_table_jadwal(self):
        query = '''
            CREATE TABLE IF NOT EXISTS jadwal (
                ID_Jadwal INT AUTO_INCREMENT PRIMARY KEY,
                ID_Film INT NOT NULL,
                ID_Studio INT NOT NULL,
                Jam_Tayang TIME NOT NULL,
                Tanggal_Tayang DATE NOT NULL,
                FOREIGN KEY (ID_Film) REFERENCES film(ID_Film),
                FOREIGN KEY (ID_Studio) REFERENCES studio(ID_Studio)
            );
        '''
        self.cur.execute(query)
        self.db.commit()

    def create_table_pemesan(self):
        query = '''
            CREATE TABLE IF NOT EXISTS pemesan (
                ID_Pemesan INT AUTO_INCREMENT PRIMARY KEY,
                Nama_Lengkap VARCHAR(255) NOT NULL,
                Email VARCHAR(255) NOT NULL,
                Nomor_Telepon VARCHAR(15) NOT NULL
            );
        '''
        self.cur.execute(query)
        self.db.commit()

    def create_table_pemesanan(self):
        query = '''
            CREATE TABLE IF NOT EXISTS pemesanan (
                ID_Pemesanan INT AUTO_INCREMENT PRIMARY KEY,
                ID_Jadwal INT NOT NULL,
                ID_Pemesan INT NOT NULL,
                Harga_Tiket INT(10) NOT NULL,
                Jumlah_Tiket INT NOT NULL,
                Total_Harga INT(10) NOT NULL,
                Status_Pemesanan VARCHAR(20) NOT NULL,
                Tanggal_Pemesanan DATE NOT NULL,
                FOREIGN KEY (ID_Jadwal) REFERENCES jadwal(ID_Jadwal),
                FOREIGN KEY (ID_Pemesan) REFERENCES pemesan(ID_Pemesan)
            );
        '''
        self.cur.execute(query)
        self.db.commit()


    def close_connection(self):
        self.cur.close()
        self.db.close()

if __name__ == "__main__":
    db = Database()
    db.create_tables()
    db.close_connection()
