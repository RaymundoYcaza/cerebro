
Esto me dio problemas porque me daba error, indicando que no se podia abrir el archivo. El error se debía a que no puede leerlo desde el disco `P:\` donde tengo el ejecutable y cuando lo cambié a la ruta `C:\data\base.db` sí pudo leerlo correctamente. 

> **Nota**: No debe crearse el archivo en la ruta destino, ni copiarse de otro lado, el sistema la crea automáticamente.

1. Se crea la conexión con el archivo sqlite
2. Se crea la datasource, seleccionando la conexión creada

Estos dos pasos se deben realizar dentro de una de las bases de NocoDB.


