warna1=set()
warna2=set()

a=int(input('masukkan jumlah warna 1: '))
b=int(input('masukkan jumlah warna 2: '))

print('masukkan nama warna 1 :')
for i in range (a):
    warnaa=input('')
    warna1.add(warnaa)

print('masukkan nama warna 2:')
for i in range (b):
    warnaa=input('')
    warna2.add(warnaa)

c=warna1-warna2
d=warna2-warna1
c.update(warna2)
print(c)
