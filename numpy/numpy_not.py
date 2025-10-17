import numpy as np

python_list = [0,1,2,3,4,5,6,7,8,9]
numpy_list = np.array([0,1,2,3,4,5,6,7,8,9])
numpy_list2 = np.array([[0,1,2,3,4,5,6,7,8,9]])
print(f"python listesi: {python_list}")
print(f"numpy_list: {numpy_list}")

print(numpy_list.ndim) #kaç boyutlu olduğunu döner ->1

print(numpy_list.shape) #kaç satır ve sütundan oluştuğunu gösteren tuple döndürür ->(10,)

print(numpy_list2.ndim) 
print(numpy_list2.shape)

print(numpy_list.reshape(1,10))
print(numpy_list.reshape(10,1))
print(numpy_list.reshape(5,2))
print(numpy_list.reshape(2,5))

print(np.arange(0,10,3))
print(np.arange(10))
print(np.arange(0,10,1))

#Diziden elemanları seçmek 
#genel kullanım: ndarray[rows,columns] satır,sütun
#ndarray[:,:] -> buradaki : kullanımı tüm satır ve sütünları seçmemizi sağlar 
numpy_list = np.array([0,1,2,3,4,5,6,7,8,9])
numpy_array = numpy_list.reshape(5,2)
print(f"numpy dizisi: {numpy_array}")
#dizinin herhangi bir satırını seçmek 
first_row = numpy_array[0]
print(first_row)
first_and_second_rows = numpy_array[0:2]
print(first_and_second_rows)
#dizinin herhangi bir kolonunu sütunu çekmek 
first_column = numpy_array[:,0]
print(first_column)
first_and_second_columns = numpy_array[:,0:2]
print(first_and_second_columns)
#dizinin herhangi bir elemanını seçmek 
selecting_item = numpy_array[3,1]
print(selecting_item)

#diziyi ters çevirmek 
print(numpy_array[::-1])

#sıfır matrisi oluşturmak -> np.zeros()
print(np.zeros((5,4)))
#birlerden oluşan matris  -> np.ones()
print(np.ones((3,3,3)))
#birim matris oluşturmak  -> np.eye()
print(np.eye((4)))

#matrisleri birleştirmek
#satır bazlı birleştirme 
print(np.concatenate([numpy_array, numpy_array], axis =0))
#sütun bazlı birleştirme
print(np.concatenate([numpy_array, numpy_array], axis =1))

#satır toplamı 
print(numpy_array.sum(axis = 1))
#sütun toplamı 
print(numpy_array.sum(axis = 0))

#ortalama ->mean
print(numpy_array.mean())
#median ortanca 
print(np.median(numpy_array)) #elemanları kten be sıralar
#eleman sayısı tek ise ortadaki çift ise ortadaki iki değerin ort alınır 
#Varieance - varyans
print(numpy_array.var()) #verileerin ortalamadan ne kadar uzaklatığını ölçer 
#her elemandan ortalamayı çıkarıp karelerini alır toplarız. onu da eleman sayısına böleriz
#Standard Deviation -standart sapma 
print(numpy_array.std()) #varyansın kareköküdür yani ortalama uzaklık gibi 

#numpy toplamaNumpy toplama, çıkarma gibi basit matematiksel işlemlerin yanında 
#trigonometrik, logaritmik,üstel fonksiyonlar… gibi daha kompleks fonksiyonlarla da çalışma imkanı sağlar
# iki matris çarpılırken ilk matrisin sütun sayısının ikinci matrisin satır sayısına eşit olmalıdır
print(numpy_array.T)  #transpozunu alır. satırlar sütun sütunlar satır olur 

#numpyde koşul ifadeleri ile de çalışılır. if else bloğu kullanmadan yapılabilir 
boolean_array = numpy_array >= 5
print(boolean_array)
print(numpy_array[boolean_array]) #hangileri olduğunu verir 
