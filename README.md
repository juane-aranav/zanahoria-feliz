`Parcial 2: Programación`
El programa *main.py* funciona de la siguiente manera:

    -Solicita un texto que contenga números romanos.

    -Separa el string ingresado en los espacios que tenga y los elementos separados los convierte en una lista *separador*.

    -Usa una función *traductor* para convertir los números romanos de la lista en números arábigos que trabaja de la siguiente manera:

        -Identifica en los elementos de la lista si hay signos de puntuación tales como __,.;__ y los elimina
         asignándolos a un valor específico de una variable *signos*.

        -Invierte horizontalmente el texto de cada string en la lista.

        -En un ciclo para *i* en la lista de textos invertidos horizontalmente, evalúa si en el ciclo actual el caracter
         pertenece a un diccionario con números romanos expresados como strings. De pertenecer, evalúa si el valor numérico de la posición anterior es mayor que el de la actual y asigna (con signo negativo) en una variable *arabn* el valor numérico del caracter en el diccionario. Caso contrario para los pertenecientes, se asigna (con signo positivo) en *arabn* el valor numérico del caracter en el diccionario. En el mismo ciclo, se evalúa si el caracter actual corresponde a uno de los valores específicos de *signos* y de ser así, añade el caracter correspondiente en *arabn* expresado como string. De no corresponder, se arroja el string de *arab*.

    -En un ciclo, para la posición de *i* en la lista intenta aplicar *traductor* y agrega en una lista *salida*  el
     valor evaluado en *traductor*. Si falla la función se agrega a la lista el valor original de *separador*.

    -Finalmente, añade a un string *textra* cada valor de *salida* y lo imprime. *textra* sería la traducción del texto
     ingresado.
