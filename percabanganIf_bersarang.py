gaji = 100000000
berkeluarga = True
punyaRumah =  True

if gaji > 3000000:
    print("Gaji sudah diatas UMR")
    if berkeluarga:
        print("Wajib ikut asuransi dan menabung untuk pensiun")
    else:
        print("Tidak perlu ikut asuransi")
    
    if punyaRumah:
        print("Wajib Bayar pajak rumah")
    else:
        print("Tidak wajib bayar pajak rumah")
else:
    print("Gaji belum UMR")