"""stdOut.py
Descripción.
        muestra los argumentos de la función print
        sep: símbolo para separar objetos
        end: símbolo al final de la instrucción
"""
#define expresiones 
calle=str("Av. Ameyalco s/n, Tlatel Xochitenco")
municipio="Chimalhuacan"
telefono="52+ 55 2632 0808"
telefonoAlt="52+ 55 5817 1618"
cp=56366
estadoFederativo="Estado de México."
url="https://chimalhuacan.conalepmex.edu.mx"

#imprime con argumentos 
print("Conalep Chimalhuacan",calle,municipio,cp,sep=",",end="\n")
print(estadoFederativo,url,end="\n")

#impresion con formato
print("\n","*"*10)
print(f" Calle: {calle}, municipio: {municipio}",sep=",",end="\n")
print(f" telefono: {telefono}",sep=",",end="\n")
print(f" cp: {cp}, Estado: {estadoFederativo}",sep=",",end="")
print(f" Url: {url}",sep=",",end="\n")

#define una estructura indexada tipo arreglo
direccion=[calle,municipio,cp,telefono,estadoFederativo,url]
tamanio=len(direccion)#recupera tamaño del arreglo
print("\n\t",direccion)



#ciclo iterativo
print("\n")
for indx in range(tamanio):
    print(direccion[indx],sep=",")



    

