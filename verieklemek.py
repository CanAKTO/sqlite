import sqlite3
veritabani = sqlite3.connect("veritaban.db") #database oluşturduk
imlec  = veritabani.cursor() #imlec oluşturduk
tablo="CREATE TABLE IF NOT EXISTS personel(isim TEXT,soyisim TEXT ,departman TEXT,maas INT)"
imlec.execute(tablo)
veritabani.commit()#güncelledik
imlec.execute("INSERT INTO personel VALUES('can','akto','arge',4000)")
imlec.execute("INSERT INTO personel VALUES('ceyda','akto','karım',10000)")
veritabani.commit()#güncelledik

isim=input("isim : " )
soyisim=input("soyisim : " )
departman=input("departman : " )
maas=input("maas : " )
imlec.execute("INSERT INTO personel VALUES(?,?,?,?)",(isim,soyisim,departman,maas))
veritabani.commit()#güncelledik

def verileri_al():
    imlec.execute("SELECT * FROM personel")
    liste=imlec.fetchall()
    for i in liste:
        print(i)

verileri_al()

def verileri_al2():
    imlec.execute("SELECT isim,soyisim FROM personel")
    liste=imlec.fetchall()
    for i in liste:
        print(i)
    # isim soy isimleri aldık
verileri_al2()

def verileri_al3():
    imlec.execute("SELECT * FROM personel WHERE departman = 'arge'")
    liste=imlec.fetchall()
    for i in liste:
        print(i)
    # departmanı arge olanları aldık
verileri_al3()

def güncelle(eski_dep,yeni_dep):
    imlec.execute("UPDATE personel SET deparman = ? WHERE deparman = ?",(yeni_dep,eski_dep))
    liste=imlec.fetchall()

    # güncelleme yaptık
güncelle("arge","satınalma")

verileri_al()

def sil(departman):
    imlec.execute("DELETE FROM personel WHERE departman = ?",(departman,))
    veritabani.commit()

sil("arge")

veritabani.close()

