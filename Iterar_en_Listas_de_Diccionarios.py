def iterarDiccionarios(lista):
    for x in range (len(lista)):
        clave=[]
        value=[]
        ouput=''
        for y in lista[x]:
            clave.append(y)
            value.append(lista[x][y])
        for i in range(0,len(clave),1):
            if i==len(clave)-1:
                ouput=ouput+clave[i] + ' - ' + value[i]
            else:
                ouput=ouput+clave[i] + ' - ' + value[i]+',  '
        print(ouput)

# Press the green button in the gutter to run the script.

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
iterarDiccionarios(students)


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
