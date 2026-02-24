import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_warung'
)

def data (nama_barang, code_barang, harga_barang, stok_barang):
    cursor = db.cursor()
    cursor.execute('INSERT INTO inventori (produk, code_produk, harga_produk, stok_produk)VALUE(%s, %s, %s, %s)', (nama_barang, code_barang, harga_barang, stok_barang))
    db.commit()

    if cursor.rowcount > 0:
        return ('success')
    else:
        return ('gagal!!')
    
    
def tambah_produk():
    nama_barang = input('poduk: ')
    code_barang = input('code produk: ')
    harga_barang = int(input('harga produk: '))
    stok_barang = int(input('stok produk: '))
    print ('input produk success!!!\n\n')

    save = data(nama_barang, code_barang, harga_barang, stok_barang)
    return(save)

def data_produk():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM inventori")
    hasil = cursor.fetchall()
    for row in hasil:
        print (f"{row[1]}")
        if row[2] <= 20000:
            print (f"{row[0]} | {row[2]} (murah)")
        elif row[2] <= 50000 and row[2] >= 20000:
            print (f"{row[0]} | {row[2]} (sedang)")
        elif row[2] >= 50000:
            print (f"{row[0]} | {row[2]} (mahal)")
        print (f"stok : {row[3]}\n")
        
    validasi = input("\ntekan enter untuk ke menu utama!")



def delete_produk():
    cursor = db.cursor()

    kode = input("Masukan kode produk yang ingin dihapus: ")

    cursor.execute("SELECT * FROM inventori WHERE code_produk = %s", (kode,))
    data = cursor.fetchone()

    if data is None:
        print("Produk tidak ditemukan!")
        return

    konfirmasi = input("Yakin ingin menghapus produk? (y/n): ")

    if konfirmasi.lower() == 'y':
        cursor.execute("DELETE FROM inventori WHERE code_produk = %s", (kode,))
        db.commit()
        print("Produk berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")
    validasi = input("\ntekan enter untuk ke menu utama!")



def change_data():
    cursor = db.cursor()
    kode = input("masukan kode produk: ")

    cursor.execute("SELECT * FROM inventori WHERE code_produk = %s ", (kode,))
    data = cursor.fetchone()

    if data is None:
        print ("produk tidak ditemukan, silahkan tinjau kembali")
        return
    
    update_nama = input ("update nama produk: ")

    try:
        update_harga = int(input("update harga: "))
        update_stok = int (input("update stok produk: "))
    except ValueError:
        print("mohon masukan data dalam bentuk angka!")
        return
    
    query = '''
UPDATE inventori
SET produk = %s, harga_produk = %s, stok_produk = %s
WHERE code_produk = %s
'''

    value = (update_nama, update_harga, update_stok, kode)

    cursor.execute(query, value)
    db.commit()

    if cursor.rowcount > 0:
        print ("data berhasil dirubah!")
    else:
        print("update invalid")
    validasi = input("\ntekan enter untuk ke menu utama!")


def temukan_produk(produk):
    cursor = db.cursor()

    cursor.execute("SELECT * FROM inventori WHERE produk = %s", (produk,))
    data = cursor.fetchone()

    if data is None:
        print ("Produk tidak ditemukan!!")
        return

    print (f'''
code: {data[1]}
produk: {data[0]}
harga: {data [2]}   
stok: {data[3]}''')
    
    validasi = input("\ntekan enter untuk ke menu utama!")



def pembayaran():
    cursor = db.cursor()

    code = input("Masukan code produk: ")
    jumlah = int(input("Masukan jumlah beli: "))

    cursor.execute("""
        SELECT harga_produk, stok_produk 
        FROM inventori 
        WHERE code_produk = %s
    """, (code,))

    data = cursor.fetchone()

    if data is None:
        print("Produk tidak ditemukan!")
        return

    harga, stok = data   # <- sudah benar

    if stok < jumlah:
        print("Stok tidak mencukupi!")
        return

    total = harga * jumlah

    try:
        cursor.execute("""
            UPDATE inventori 
            SET stok_produk = stok_produk - %s 
            WHERE code_produk = %s
        """, (jumlah, code))

        cursor.execute("""
            INSERT INTO penjualan (code_produk, jumlah, harga_satuan, total_harga)
            VALUES (%s, %s, %s, %s)
        """, (code, jumlah, harga, total))

        db.commit()

        print(f"""
Pembayaran berhasil!
Total bayar: {total}
Stok berhasil diupdate!
""")

    except Exception as e:
        db.rollback()
        print("Terjadi kesalahan saat transaksi!", e)





        