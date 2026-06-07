'''
Christian Gilbert Rusianto (202565001)
https://github.com/Rick-beep
'''

import json
class Ebook():
    def __init__(self, data_dic):
        self.data = data_dic
        self.load()
    
    def __str__(self):
        return f"kode: {self.kode}, \njudul: {self.judul}, \npenulis: {self.penulis}, \nkategori: {self.kategori}, \ntahun: {self.tahun}, \nstok: {self.stok}"
    
    def get_data(self):
        return self.data
    
    def load(self):
        self.kode = self.data["kode"]
        self.judul = self.data["judul"]
        self.penulis = self.data["penulis"]
        self.kategori = self.data["kategori"]
        self.tahun = self.data["tahun"]
        self.stok = self.data["stok"]

class Perpus():
    def __init__(self):
        self.daftar_buku = []
        self.load_json()
        self.kategori_tetap = ("Pemrograman", "Jaringan", "Basis Data", "AI")
        self.kategori = None
        self.main()
            
    def load_json(self):
        with open("data.json", "r") as f:
            data = json.load(f)
        for i in data:
            self.daftar_buku.append(Ebook(i))
            
    def dump_json():
        pass
    
    def update_kode_daftar_buku(self):
        counter = 1
        for buku in self.daftar_buku:
            kode = f"BK{counter:03d}"
            buku.kode = kode
            counter += 1
        
    def main(self):
        self.cmd_list()
        while True:
            self.update_kode_daftar_buku()
            self.cli()
    
    def cmd_list(self):
        print("****************************")
        print("SISTEM PERPUSTAKAAN DIGITAL")
        print("\nMenu: ")
        print("0. Tambah Buku")
        print("1. Tampilkan Semua Buku")
        print("2. Cari Buku")
        print("3. Urutkan Buku")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Statistik Perpustakaan")
        print("7. Simpan Data")
        print("8. Baca Data")
        print("9. Keluar")
        print("****************************")
        
    def cli(self):
        def command_0():
            print("-------------------")
            print("Masukan data buku")
            print("-------------------\n")
            while True:
                try:
                    judul = input("judul buku: ")
                    penulis = input("penulis buku: ")
                    kategori = input("kategori buku: ")
                    tahun = int(input("tahun buku: "))
                    stok = int(input("stok buku: "))
                    print()
                except ValueError:
                    print("\n!!!Tahun dan stok harus berbentuk angka!!!")
                    continue
                
                buku = {"kode": None,"judul": judul,"penulis": penulis,"kategori": kategori,"tahun": tahun,"stok": stok}
                
                buku = Ebook(buku)
                print(buku)
                print("-------------------")    
                print("Apakah data yang di masukan sudah benar?")
                print("-------------------")
                
                hasil = False
                while True:
                    confirmasi = str(input("Y/N: ")).lower()
                    if confirmasi == "y" or confirmasi == "yes":
                        hasil = True
                        break
                    elif confirmasi == "n" or confirmasi == "no":
                        break
                print("-------------------")
                
                if hasil:
                    break
            self.daftar_buku.append(buku)
            print("-------------------")
            print(">>> Berhasil menambahkan buku ke daftar buku <<<")   
            print("-------------------")
            print("****************************")
            
            
        def command_1():
            print("****************************")
            for i in self.daftar_buku:
                print("-------------------")
                print("Judul: " + i.judul)
                print("Penulis: " + i.penulis)
                print("kategori: " + i.kategori)
                print("-------------------")
            print("****************************")

        def command_2():
            print("****************************")
            buku_dicari = input("Masukan nama buku: ")
            hasil = None
            for buku in self.daftar_buku:
                if buku.judul.lower() == buku_dicari.lower():
                    hasil = buku
            
            if hasil:
                print("Hasil pencarian: ")
                print()
                print("-------------------")
                print(hasil)
                print("-------------------")
                
            else:
                print("\n>>> Buku tidak di temukan <<<")
            print("****************************")
            
        def command_3():
            self.update_kode_daftar_buku()
            print("-------------------")
            print(f"{len(self.daftar_buku)} buku telah di urutkan")
            print("-------------------")
            
        def command_4():
            print("-------------------")    
            buku_dicari = input("Masukan nama buku: ")
            print("-------------------")    
            
            hasil = None
            for buku in self.daftar_buku:
                if buku.judul.lower() == buku_dicari.lower():
                    hasil = buku
            
            if hasil:
                print("-------------------")
                print(hasil)
                print("-------------------")
                
                meminjam = False
                while True:
                    print("-------------------")    
                    print("Apakah data yang di masukan sudah benar?")
                    print("-------------------")
                    confirmasi = str(input("Y/N: ")).lower()
                    if confirmasi == "y" or confirmasi == "yes":
                        meminjam = True
                        break
                    elif confirmasi == "n" or confirmasi == "no":
                        break
                
                print("-------------------")
                if meminjam and hasil.stok > 0:
                    hasil.stok -= 1
                    print(">>> Berhasil meminjam buku <<<")
                    print(f"stok: {hasil.stok + 1} --> {hasil.stok}")
                elif meminjam and hasil.stok <= 0:
                    print(f'>>> Stok buku "{hasil.judul}" telah habis <<<')
                else:
                    print(">>> Peminjaman di batalkan <<<")
                print("-------------------")    
            else:
 
                print(">>> Buku tidak di temukan <<<")
            print("****************************")
            
        def command_5():
            print("-------------------")    
            buku_dicari = input("Masukan nama buku: ")
            print("-------------------")    
            
            hasil = None
            for buku in self.daftar_buku:
                if buku.judul.lower() == buku_dicari.lower():
                    hasil = buku
            
            if hasil:
                print("-------------------")
                print(hasil)
                print("-------------------")
                
                kembalikan = False
                while True:
                    print("-------------------")    
                    print("Apakah data yang di masukan sudah benar?")
                    print("-------------------")
                    confirmasi = str(input("Y/N: ")).lower()
                    if confirmasi == "y" or confirmasi == "yes":
                        kembalikan = True
                        break
                    elif confirmasi == "n" or confirmasi == "no":
                        break
                
                print("-------------------")
                if kembalikan:
                    hasil.stok += 1
                    print(">>> Berhasil kembalikan buku <<<")
                    print(f"stok: {hasil.stok - 1} --> {hasil.stok}")
                else:
                    print(">>> Pengembalian di batalkan <<<")
                print("-------------------")    
            else:
                print(">>> Buku tidak di temukan <<<")
            print("****************************")     
        def command_6():
            pass        
        def command_7():
            pass        
        def command_8():
            pass
        def command_9():
            pass 
        
        command = input("Command: ")
        print()
        
        match command:
            case "0":
                command_0()
            case "1":
                command_1()
            case "2":
                command_2()
            case "3":
                command_3()
            case "4":
                command_4()
            case "5":
                command_5()
            case "6":
                command_6()
            case "7":
                command_7()
            case "8":
                command_8()
            case "9":
                command_9()
        

if __name__ == "__main__":
    Perpus()


# TODO: BUAT SET untuk Menampilkan kategori unik
{
"kode": "BK001",
"judul": "Python Dasar",
"penulis": "Andi",
"kategori": "Pemrograman",
"tahun": 2024,
"stok": 5
}