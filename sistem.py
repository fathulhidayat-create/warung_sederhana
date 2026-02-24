from database import tambah_produk
from database import data_produk
from database import delete_produk
from database import change_data
from database import temukan_produk
from database import pembayaran
import sys



def produk():
    data_produk()

def delete_data():
    delete_produk()

def add():
    tambah_produk()

def change():
    change_data()

def produk_information():
    code = input ("masukan nama produk: ")
    
    data = temukan_produk(code)
    


def menu():
    while True:
        print ('=============== WARUNG MADURA =================')
        try:
            pilihan = int(input ('\n\n1. produk\n2. delete produk\n3. tambah produk\n4. ubah data produk\n5. cari produk\n6. transaksi\n7. keluar program \n\npilih menu: '))
        except ValueError:
            print("Input harus angka!")
            continue
        if pilihan == 1:
            produk()
        elif pilihan == 2:
            delete_data() 
        elif pilihan == 3:
            add()
        elif pilihan == 4:
            change()
        elif pilihan == 5:
            produk_information()
        elif pilihan == 6:
            pembayaran()
        elif pilihan == 7:
            sys.exit()
        else :
            return ('pilihan tidak valid!!')
    

