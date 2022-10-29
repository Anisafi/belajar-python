#MEMBUAT STRUK BELANJA
import datetime

waktu = datetime.datetime.now().strftime("%X")
tanggal = datetime.datetime.now().strftime("%X")

#nama kasir
namakasir = input("masukkan nama kasir: ")

#tampilan awal 
print(f"""
    PAPUA SPM & DPSTORE
    02.316.442.9-951.000
    JL. SUNGAI MARUNI KM10
        081-2567-5758
     {tanggal} {waktu}
 ===========================
             Ksr: {namakasir}
 ===========================              
""")

tambahBarang = 'y'
totalBelanja = 0
jumlahBelanja = 0
while ('y' in tambahBarang) :

    #nama barang
    namaBarang = input("masukkan nama barang: ")

    #harga barang
    hargaBarang = int(input("masukkan harga barang: "))

    #jumlah barang
    jumlahBarang = int(input("masukkan jumlah barang: "))

    #tampilkan barang
    print(f"""
    {namaBarang}
    PCS   {jumlahBarang} {hargaBarang:,} {hargaBarang * jumlahBarang:,}
    """)

    #kalkulasi total belanja dan jumlah belanja
    totalBelanja += (hargaBarang * jumlahBarang)
    jumlahBelanja += jumlahBarang

    #tambah barang atau tidak
    tambahBarang = input("tambah barang lagi?(y/n: ")

    #tampilan total dan quality
    print(f"""
    {jumlahBelanja} item
    totBelanja   : Rp.   {totalBelanja:,}
    =====================================
    """)

    #pembayaran
    pembayaran = int(input("masukkan pembayaran: "))
    print(f"pembayaran   :  Rp.   {pembayaran:,}")
    kembalian = pembayaran - totalBelanja
    print("------------------------------")
    print(f"kembalian   :  Rp.    {kembalian:,}")

    #tampilan akhir
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               THANK YOU 
            FOR SHOPPING AT 
            OUR SUPERMARKET
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             """)