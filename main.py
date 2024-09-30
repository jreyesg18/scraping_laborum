import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Solicitar al usuario que ingrese varias palabras clave separadas por comas
keywords = input("Ingrese las palabras clave para buscar en los títulos de trabajo, separadas por comas: ").split(',')

# Limpiar las palabras clave (eliminar espacios en blanco alrededor de cada palabra)
keywords = [keyword.strip().lower() for keyword in keywords]

# Lista para almacenar los resultados
job_results = []

# Abrir la página
url = "https://www.laborum.cl/en-region-metropolitana/empleos-publicacion-hoy.html?recientes=true"
driver = webdriver.Chrome()
driver.get(url)

try:
    while True:
        # Esperar a que los trabajos estén cargados
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "sc-kJdAmE.etbjmW"))
        )

        # Encontrar todos los elementos que contienen el título y el enlace
        job_elements = driver.find_elements(By.CLASS_NAME, "sc-kJdAmE.etbjmW")

        # Extraer el título y el enlace de cada trabajo
        for job_element in job_elements:
            try:
                title_element = job_element.find_element(By.CLASS_NAME, "sc-dCVVYJ.gknyoN")
                title = title_element.text  # Texto del título del trabajo
                #link_element = job_element.find_element(By.TAG_NAME, "href")  # Encontrar el elemento 'a' dentro del trabajo
                link = job_element.get_attribute("href")  # Obtener el enlace de la oferta

                # Inicializar una variable para guardar la palabra que coincide
                matching_keyword = None

                # Filtrar por las palabras clave en el título (insensible a mayúsculas/minúsculas)
                for keyword in keywords:
                    if keyword in title.lower():
                        matching_keyword = keyword  # Guardar la palabra que coincide
                        break  # Si encuentra una coincidencia, no es necesario seguir buscando

                # Si se encontró una coincidencia
                if matching_keyword:
                    # Imprimir los datos del trabajo en la consola
                    print(f"Título: {title}\nPalabra coincidente: {matching_keyword}\nEnlace: {link}\n")
                    # Crear un diccionario con los datos del trabajo
                    job_data = {
                        "title": title,
                        "matching_keyword": matching_keyword,  # Almacenar la palabra clave que coincidió
                        "link": link
                    }

                    # Agregar el diccionario a la lista
                    job_results.append(job_data)

            except Exception as e:
                print(f"Error al procesar un trabajo: {e}")

        # Intentar ir a la siguiente página
        try:
            next_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "i.icon-icon-light-caret-right.sc-iwsKbI.hiZjGo"))
            )
            next_button.click()  # Hacer clic en el botón "Siguiente"
            time.sleep(3)  # Esperar a que se carguen los nuevos trabajos
        except Exception as e:
            print("No se pudo encontrar el botón 'Siguiente':", e)
            break  # Romper el ciclo si no se encuentra el botón

except Exception as e:
    print(f"Error: {e}")

finally:
    # Cerrar el navegador
    driver.quit()

# Guardar los resultados en un archivo JSON
with open("job_offers.json", "w", encoding="utf-8") as f:
    json.dump(job_results, f, ensure_ascii=False, indent=4)

print("Datos guardados en job_offers.json")