# Belajar-
input_pertanyaan = input('Selamat datang, ada yang bisa aku bantu sebagai robot kamu? (ketik "iya" ketika ada yang ingin dibantu) :')
pertanyaan = ('iya')

if input_pertanyaan == pertanyaan:
    print ('Baiklah, saya akan membantu kamu')
    nama = input('Sebelumnya siapakah nama kamu? :')

    input_bantuan = input('Baik ' + nama + ', kamu ingin dibantu apa? (pilihan: kalkulator, menghitung belanjaan, biodata) : ')
    kalkulator = ('kalkulator')
    belanjaan = ('menghitung belanjaan')
    biodata = ('biodata')

    if input_bantuan == kalkulator:
        print ('=====MODE KALKULATOR AKTIF=====')
        x = int(input())
        eksekusi = input('pilih + (tambah) - (kurang) * (kali) / (bagi)')
        y = int(input())

        kali = ('*')
        bagi = ('/')
        tambah = ('+')
        kurang = ('-')

        x_kali_y = x * y
        X_bagi_y = x / y
        x_tambah_y = x + y
        x_kurang_y = x - y

        if eksekusi == kali:
            print (x_kali_y)

        elif eksekusi == bagi:
            print (X_bagi_y)

        elif eksekusi == tambah:
            print (x_tambah_y)

        elif eksekusi == kurang:
            print (x_kurang_y)

    elif input_bantuan == belanjaan:
        print ('=====MODE BELANJA AKTIF=====')
        barang = input('Mau beli apa ' + nama + ' ? :')
        harga = int(input('Baiklah kamu ingin membeli ' + barang + ' seharga berapa satuannya? :'))
        berapa = int(input('Kamu ingin membeli ' + barang + ' sebanyak? :'))
        total = harga * berapa

        print('===MODE MENGHITUNG===')
        print('Kamu ingin membeli ' + barang + ' dengan harga sebesar Rp.' + str(total))

        input_kembalian = input('Apakah kamu ingin menghitung kembalian dari saldo yang kamu miliki? (ketik iya jika ingin menghitung) :')
        true_kembalian = ('iya')

        if input_kembalian == true_kembalian:
            print ('===MODE KEMBALIAN===')
            saldo = int(input('Ada berapa banyak saldo kamu? '))
            kembalian = saldo - total
            print ('Jadi sisa dari saldo kamu sebesar Rp.' + str(kembalian))
        
        else:
            print ('---- MODE SELESAI ----')

    elif input_bantuan == biodata:
        print('=====MODE BIODATA AKTIF=====')
        input_nama = input('Sebelumnya kita sudah berkenalan, apakah benar nama kamu ' + nama + ' ?: (jawab "iya" ketika benar) (jawab "tidak" ketika salah)')
        true_nama = ('iya')
        
        if input_nama == true_nama:
            print ('Oke ' + nama)
            print ('Perkenalkan aku adalah robot yang diciptakan aby')
            print ('Untuk membantu kebutuhan sehari hari kamu')
            tanggal = input ('Tanggal berapa kamu lahir? :')
            bulan = input('Bulan? :')
            tahun = input('Tahun? :')

            input_pendidikan = input('Apakah kamu masih seorang pelajar/ sudah bekerja? (jawab "pelajar" ketika kamu masih pelajar) (jawab "kerja" apabila kamu sudah bekerja) :')
            true_pelajar = ('pelajar')
            true_kerja = ('kerja')
            if input_pendidikan == true_pelajar:
                pendidikan = input('Kamu sekolah di mana? :')
            
            else:
                kerja = input('Kamu bekerja di perusahaan apa? :')
                jabatan = input('Jabatan apa yang kamu duduki di ' + kerja)


            print ('---- MODE MENGENAL AKTIF ----')
            print ('Halo ' + nama)
            print ('Kamu lahir pada tanggal ' + str(tanggal) + ' Bulan ' + str(bulan) + ' Tahun ' + str(tahun))
            print ('Kamu adalah seorang ' + input_pendidikan)
            if input_pendidikan == true_pelajar:
                print ('Kamu bersekolah di ' + pendidikan)
            
            elif input_pendidikan == true_kerja:
                print ('Kamu bekerja di ' + kerja)
                print ('Kamu menjabat di jabatan ' + jabatan)

else:
    print('Okey, Terima Kasih')
