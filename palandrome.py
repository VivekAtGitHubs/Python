pal ="ViviV"
# a =a , s=s a

ispal = True

leng =len(pal)
for i in range(leng//2):
    print(i ," ",pal[i] , " " + pal[leng - 1 - i] )
    if pal[i] != pal[leng - 1 - i]:
        ispal = False



if ispal == True:
    print(pal + " is palandrome")

else:
    print(pal + " " + " is not palandrome")
    






