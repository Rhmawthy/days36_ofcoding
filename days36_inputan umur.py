#program menghitung usia dan menentukan usia
tahun_kelahiran = int(input("masukkan tahun kelahiran anda:"))
tahun_sekarang = int(input("masukkan tahun kelahiran anda:"))

usia = tahun_sekarang - tahun_kelahiran
if usia <= 5:
    print ("usia anda ",usia, "kategori usia anda balita")
elif usia <= 12:
    print ("usia anda ",usia, "kategori usia anda anak-anak")
elif usia <= 19:
    print ("usia anda ",usia, "kategori usia anda remaja")
elif usia <= 30:
    print ("usia anda ",usia, "kategori usia anda dewasa")
elif usia <= 60:
    print ("usia anda ",usia, "kategori usia anda mudah")
else:
    print ("usia anda ",usia, "kategori usia anda lansia")
    









          
    
          
        
