try:
    import os
    for i in range(1,10):
        os.mkdir("C:/Users/egitim.sinif2/Desktop/elma"+str(i))
except:FileExistsError
print("Aynı isimle dosyan var")

