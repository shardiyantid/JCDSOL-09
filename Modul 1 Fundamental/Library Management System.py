# Deklarasi dictionary untuk menyimpan data buku
books = {
    "001": {"title": "Data Science for Business", "author": "Foster Provost", "stock": 5, "harga sewa" : 15000},
    "002": {"title": "Mining of Massive Datasets", "author": "Anand Rajaraman", "stock": 3, "harga sewa" : 15000},
    "003": {"title": "Python for Data Analysis", "author": "Wes McKinney", "stock": 1, "harga sewa" : 15000},
}

# Fungsi untuk report menu
def show_report_menu():
    print("Menu Report")
    print("1. Semua data buku")
    print("2. Data buku berdasarkan ISBN")
    print("3. Kembali ke menu utama")

# Fungsi untuk menampilkan menu
def display_menu():
    print("============================================")
    print("SELAMAT DATANG DI PERPUSTAKAAN PURWADHIKA")
    print("============================================")
    print("1. Report Data Buku")
    print("2. Menambah Data Buku")
    print("3. Update Data Buku")
    print("4. Menghapus Data Buku")
    print("5. Menyewa Buku")
    print("6. Exit Program")
    print("============================================")

# Fungsi untuk menampilkan data buku
def display_books():
    print("DAFTAR BUKU")
    print("=======================================================================================")
    print("Kode\tJudul\t\t\t\tPenulis\t\t\tStok\tHarga Sewa")
    print("=======================================================================================")
    for code, book in books.items():
        print(f"{code}\t{book['title']}\t{book['author']}\t\t{book['stock']}\t{book['harga sewa']}")
    print("=======================================================================================")

# Fungsi untuk menampilkan data buku by code
def show_book_by_isbn():
    code = input("Masukkan ISBN buku: ")
    book = books.get(code)
    if book:
        print(f"\nISBN: {code}")
        print(f"Judul: {book['title']}")
        print(f"Penulis: {book['author']}")
        print(f"Stok: {book['stock']}")
        print(f"Harga sewa: {book['harga sewa']}")
        print("\n")
    else:
        print("Buku tidak ditemukan")

# Fungsi untuk menambah list buku
def add_book():
    code = input("Masukkan ISBN Buku: ")
    if code in books:
        print("Buku dengan ISBN tersebut sudah ada.")
    else:
        title = input("Judul Buku: ")
        author = input("Penulis: ")
        stock = int(input("Stok: "))
        harga_sewa = int(input("Harga Sewa: "))
        books[code] = {"title": title, "author": author, "stock": stock, "harga sewa": harga_sewa}
        print("Buku berhasil ditambahkan.")

# Fungsi untuk mengupdate data buku
def update_book():
    code = input("Masukkan kode buku: ")
    if code in books:
        title = input("Masukkan judul buku: ")
        author = input("Masukkan nama penulis: ")
        stock = int(input("Masukkan jumlah stok: "))
        harga_sewa = int(input("Harga Sewa: "))
        books[code] = {"title": title, "author": author, "stock": stock, "harga sewa": harga_sewa}
        print("Data buku berhasil diupdate!")
    else:
        print("Data buku tidak ditemukan!")

# Fungsi untuk menghapus data buku
def delete_book():
    code = input("Masukkan ISBN buku: ")
    if code in books:
        del books[code]
        print("Data buku berhasil dihapus!")
    else:
        print("Data buku tidak ditemukan!")

# Fungsi untuk menyewa buku 
def rent_book():
    code = input("Masukkan ISBN Buku: ")
    if code not in books:
        print("Buku dengan ISBN tersebut tidak ditemukan.")
    else:
        stock = books[code]["stock"]
        if stock <= 0:
            print("Maaf, stok buku habis.")
        else:
            books[code]["stock"] -= 1
            harga_sewa = books[code]["harga sewa"]
            print("Buku '%s' berhasil disewa dengan harga sewa Rp%s." % (books[code]["title"], harga_sewa))

# Program utama
while True: 
    display_menu()
    choice = input("Masukkan pilihan menu: ")
    if choice == "1":
        while True:
            show_report_menu()
            report_choice = input("Pilih menu report: ")
            if report_choice == "1":
                display_books()
            elif report_choice == "2":
                show_book_by_isbn()
            elif report_choice == "3":
                break
            else:
                print("Pilihan tidak valid, silakan pilih menu yang tersedia")
    elif choice == "2":
        add_book()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        rent_book()
    elif choice == "6":
        print("Terima kasih telah menggunakan program ini")
        break
    else :
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia!")
        continue

display_menu()
