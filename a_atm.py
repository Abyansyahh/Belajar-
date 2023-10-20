#ini kode login atm nya
print ('=========== ATM ABY ============')
username = input (' Username: ')
password = input (' Password: ')

#ini username
satu = 'abyansyah'
dua = 'zahira'

#ini pw
p01 = '011005'
p02 = '060513'

#ini respon
cs = '1'
tt = '2'
iss = '3'

#ini saldo
abs = int(1000000000)
zas = int(400000)


if username == satu:
    print('')
    print('====== USERNAME DITEMUKAN ======')
    if password == p01:
        print('')
        print('======== PASSWORD BENAR ========')
        print('')
        print('======= PILIH SALAH SATU =======')
        print('================================')
        print('======== 1. CEK SALDO ==========')
        print('======= 2. TARIK TUNAI =========')
        print('======== 3. ISI SALDO ==========')
        print('================================')
        respon = input (': ')
        if respon == cs :
            print ('SALDO ANDA SEBESAR Rp. ', abs )
        
        elif respon == tt:
            print ('================================')
            print ('===== KAMU MAU TARIK TUNAI =====')
            print ('=========== SEBESAR ============')
            nomtt = input ()
            print ('================================')
            print ('====== PROSES TARIK TUNAI ======')
            print ('================================')
            print ('Duit kamu sudah diambil sebesar ')
            print ('Rp. ' + nomtt)
            print ('================================')

            nomtt_ = int(nomtt)
            hasiltt = abs - nomtt_

            print ('SALDO KAMU TERSISA ', hasiltt)

        elif respon == iss:
            print ('================================')
            print ('======= SALDO MU SEBESAR =======')
            print ('=  Rp.', abs)
            print ('================================')
            print ('== KAMU MAU ISI SALDO SEBESAR ==')
            a = input()
            print ('================================')
            print ('')
            print ('====== ISI SALDO BERHASIL ======')

            isisaldo = int(a)
            ts = abs + isisaldo
            print ('- SALDO KAMU: RP. ', ts)

elif username == dua:
    print('')
    print('====== USERNAME DITEMUKAN ======')
    if password == p02:
        print('')
        print('======== PASSWORD BENAR ========')
        print('')
        print('======= PILIH SALAH SATU =======')
        print('================================')
        print('======== 1. CEK SALDO ==========')
        print('======= 2. TARIK TUNAI =========')
        print('======== 3. ISI SALDO ==========')
        print('================================')
        respon = input (': ')
        if respon == cs :
            print ('SALDO ANDA SEBESAR Rp. ', zas )
        
        elif respon == tt:
            print ('================================')
            print ('===== KAMU MAU TARIK TUNAI =====')
            print ('=========== SEBESAR ============')
            nomtt = input ()
            print ('================================')
            print ('====== PROSES TARIK TUNAI ======')
            print ('================================')
            print ('Duit kamu sudah diambil sebesar ')
            print ('Rp. ' + nomtt)
            print ('================================')

            nomtt_ = int(nomtt)
            hasiltt = zas - nomtt_

            print ('SALDO KAMU TERSISA ', hasiltt)

        elif respon == iss:
            print ('================================')
            print ('======= SALDO MU SEBESAR =======')
            print ('=  Rp.', zas)
            print ('================================')
            print ('== KAMU MAU ISI SALDO SEBESAR ==')
            a = input()
            print ('================================')
            print ('')
            print ('====== ISI SALDO BERHASIL ======')

            isisaldo = int(a)
            ts = zas + isisaldo
            print ('- SALDO KAMU: RP. ', ts)
    
    else:
        print('======== PASSWORD SALAH ========')
    
else:
    print('=== USERNAME TIDAK DITEMUKAN ===')