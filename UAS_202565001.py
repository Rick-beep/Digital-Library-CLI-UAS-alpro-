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
        self.kategori = None
        self.load_json()
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
            self.update_daftar_buku()
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
                
                print("-------------------")    
                print("Apakah data yang di masukan sudah benar?")
                print("-------------------")
                buku = Ebook(buku)
                print(buku)
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
            print("\n-------------------")
            print("Berhasil menambahkan ke daftar buku")   
            print("-------------------\n")
            
        def command_1():
            print("****************************")
            for i in self.daftar_buku:
                print("-------------------")
                print(i)
                print("-------------------")
                print()
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
                print("\n---Buku tidak di temukan---")
            print("****************************")
            
        def command_3():
            pass
        def command_4():
            pass        
        def command_5():
            pass        
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


{
"kode": "BK001",
"judul": "Python Dasar",
"penulis": "Andi",
"kategori": "Pemrograman",
"tahun": 2024,
"stok": 5
}