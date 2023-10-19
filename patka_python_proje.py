# SORU 1:Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir
liste =  [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def list_eleman(liste_1):
    eleman = []
    for item in liste_1:
        if type(item) == list:
            eleman += list_eleman(item)
        else:
            eleman.append(item)
    return eleman

print(list_eleman(liste))

#Soru 2:  Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
liste = [[1, 2], [3, 4], [5, 6, 7]]

def tersini_alma(ters):
    ters = ters[::-1]
    ters = [i[::-1] for i in ters]
    return ters
print(tersini_alma(liste))




