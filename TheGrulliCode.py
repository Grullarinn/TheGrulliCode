print('Skrifaðu "1" fyrir aftan örina að neðan ef þú vilt breyta venjulegum texta í GrúllíKóða')
print('Skrifaðu "2" fyrir aftan örina að neðan ef þú vilt breyta GrúllíKóða yfir í venjulegan texta')
innslag = input('---> ')
nowGrulli = ''
nowTexti = ''
if int(innslag) == 1:
    print('Skrifaðu textann sem þú vilt breyta í GrúllíKóða hér að neðan')
    TxtToGrulli = input('---> ')
    lengd = len(TxtToGrulli)
    for x in range(0, lengd, 1):
        gildiTolu = ord(TxtToGrulli[x])
        if gildiTolu == 32:
            nowGrulli += chr(32)
        elif gildiTolu >= 61:
            if gildiTolu % 2 == 0:
                nowGrulli += chr(gildiTolu + 3)
            elif gildiTolu % 2 != 0:
                nowGrulli += chr(gildiTolu + 5)
        elif 32 < gildiTolu < 60:
            if gildiTolu % 2 == 0:
                nowGrulli += chr(gildiTolu + 1)
            else:
                nowGrulli += chr(gildiTolu - 1)

    print(TxtToGrulli, ' = ', nowGrulli, end='')
elif int(innslag) == 2:
    print('Skrifaðu GrúllíKóðann sem þú vilt breyta í venjulegan texta hér að neðan')
    GrulliToTxt = input('---> ')
    staerd = len(GrulliToTxt)
    for y in range(0, staerd, 1):
        gildiStafs = ord(GrulliToTxt[y])
        if gildiStafs == 32:
            nowTexti += chr(32)
        elif gildiStafs > 60:
            if gildiStafs % 2 != 0:
                nowTexti += chr(gildiStafs - 3)
            elif gildiStafs % 2 == 0:
                nowTexti += chr(gildiStafs - 5)
        elif gildiStafs < 61:
            if gildiStafs % 2 != 0:
                nowTexti += chr(gildiStafs - 1)
            elif gildiStafs % 2 == 0:
                nowTexti += chr(gildiStafs + 1)
    print(GrulliToTxt, '=', nowTexti, end='')

