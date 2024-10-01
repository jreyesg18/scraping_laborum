# Scraper de Ofertas Laborales Laborum

Este proyecto es un script de scraping que utiliza Selenium para extraer ofertas laborales desde el sitio web Laborum.cl. Permite al usuario buscar trabajos según palabras clave específicas y guarda los resultados en un archivo JSON.

## Requisitos

- Python 3.x
- Selenium
- Chrome WebDriver (debe ser compatible con tu versión de Chrome)

## Instalación

1. Clona este repositorio o descarga los archivos.

2. Instala las dependencias requeridas:

       pip install selenium
3. Asegúrate de tener Chrome WebDriver instalado y que esté en tu PATH. 

## Uso

1. Abre una terminal y navega hasta el directorio del proyecto.

2. Ejecuta el script:

         python main.py
3. Cuando se te solicite, ingresa la palabra clave que deseas buscar en los títulos de trabajo.
        

         analista, desarrollador, ingeniero
4. El script comenzará a buscar ofertas laborales que contengan las palabras clave ingresadas. Los resultados se mostrarán en la consola y se guardarán en job_offers.json al finalizar.

## Ejemplo

Si deseas buscar trabajos que contengan las palabras "Ventas, Marketing, Programación", simplemente ingresa esas palabras separadas por comas cuando se te solicite.
## Estructura de los Datos

Los datos extraídos se guardarán en un archivo JSON con la siguiente estructura:


        [
            {
                "title": "Analista TI",
                "matching_keyword": "analista"
                "link": "https://cl.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-ejecutivo-de-ventas-part-time-de-10-a-1630-hrs-de-lunes-a-viernes-en-santiago-centro-2DC9E14A19608C9661373E686DCF3405#lc=ListOffers-Score-0"
                
            },
            ...
        ]

## Notas

- Asegúrate de que tu conexión a internet esté activa durante la ejecución del script.
- El script puede tardar un tiempo en completarse, dependiendo de la cantidad de páginas de resultados.
- Las palabras clave son insensibles a mayúsculas/minúsculas, por lo que "ventas" y "Ventas" se tratarán como iguales.
