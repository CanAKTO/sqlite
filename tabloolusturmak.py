import sqlite3
veritabani = sqlite3.connect("veritaban.db") #database oluşturduk
imlec  = veritabani.cursor() #imlec oluşturduk
tablo="CREATE TABLE IF NOT EXISTS personel(isim,soyisim,departman,maas)"
imlec.execute(tablo)
veritabani.close()
