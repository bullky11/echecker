abc="AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"
eltolt_abc="XYZAÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVW"
kod=[]
def betukeres(betu):
    i=0

    while i<len(abc) and abc[i]!=betu:
        i+=1
    if i< len(abc):
        return i
    else:
        return -1

keresendo=input("kérek egy betűt").upper()
betukeres("E")
print(betukeres(keresendo))


