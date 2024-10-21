#define expresiones 
calle=str("Av. Ameyalco s/n, Tlatel Xochitenco")
municipio="Chimalhuacan"
telefono="52+ 55 2632 0808"
telefonoAlt="52+ 55 5817 1618"
cp=56366
estadoFederativo="Estado de México."
url="https://chimalhuacan.conalepmex.edu.mx"

#define un arreglo de arreglos
arrayDatos=[["id","Campo","Valor"],#define cabecera de tabla
            ["Calle",calle],
            ["Municipio",municipio],
            ["Tel",telefono],
            ["Cp",cp],
            ["Estado",estadoFederativo],
            ["Url",url]
            ]

arrayDatos
#define un diccionario
dictDatos={"Calle":calle,
           "Municipio":municipio,
           "Tel":telefono,
           "Cp":cp,
           "Estado": estadoFederativo,
           "Url":url
           }

direccion={"campo_1":[calle,municipio,telefono]}



