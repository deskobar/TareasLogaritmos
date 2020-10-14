Esta tarea solo funciona en linux, se esperaba funcionara en todos los SO, pero fracasamos miserablemente.

Si bien el SO en el que fue desarrollada no es el mismo de Anakena, se puede correr y probar ahí.

Hay un Makefile, pero se pide encarecidamente no traten de usarlo, puesto que no fue más que probado en un solo computador.

Adicionalmente, el archivo generator.py que fue requerido, arroja los archivos a la carpeta input_files, sin embargo, se puede colocar algún P o T en la carpeta raíz del proyecto, valga decir, aquí o también se puede llamar de la siguiente forma:

# python indexedSearch.py input_files/P.txt input_files/T.txt