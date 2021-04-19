#Rihar del tito-71200648
#Universitas Kristen Duta Wacana
#https://www.w3resource.com/python-exercises/list/
#list


'''
buatlah sebuah fungsi untuk menghitung banyak kata/huruf pada suatu kalimat.
setelah itu jika jumlah kata/huruf pada suatu kalimat itu lebih banyak dari z maka dimasukkan kedalam list

input: 
kalimat = kalimat yang akan dimasukkan user ; jumlah = jumlah z lebih dari 

proses:
membuat fungsi
membagi kalimat dengan menggunakan split()
melakukan perulangan 
melakukan percabagan dengan menghitung huruf pada kalimat menggunakan len
jika lebih dari z maka akan dimasukkan ke dalam list

output:
kata pada kalimat lebih besar dari akan dimasukkan kedalam list

'''
def menghitung_huruf(z,kalimat):
    list_kalimat = []
    hasil = kalimat.split(" ")
    for x in hasil :
        if len(x) > z :
            list_kalimat.append(x)
    return list_kalimat

jumlah = int(input("Masukkan jumlah huruf : "))
kalimat = str(input("Masukkan kalimat : "))
print(menghitung_huruf(jumlah,kalimat))