import pickle

# имя файла, в котором мы созраним объект
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # помещаем объект в файл
f.close()

del shoplist # уничтожаем переменную shoplist

# Считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # загружаем объект из файла
print(storedlist)