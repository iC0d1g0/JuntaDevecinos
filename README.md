# JuntaDevecinos

Este proyecto fue desarrollado como un aporte a la junta de vecinos "La Unión Hace la Fuerza" en la comunidad de Villa Liberación, Santo Domingo Este, República Dominicana. **JuntaDevecinos** es un programa diseñado para organizar la información de los vecinos y facilitar el registro de aportes económicos. 

## Descripción

El programa permite:
- Registrar datos de los vecinos, incluyendo nombre, dirección, teléfono, entre otros.
- Registrar y llevar un control detallado de los aportes económicos de cada vecino.
- Calcular y mostrar la totalidad de los aportes acumulados, facilitando la transparencia y la administración de los fondos.

## Tecnologías Utilizadas

- **Lenguaje de programación:** Python
- **Base de datos:** MySQL
- **Sistema operativo de destino:** Windows (compilado para su ejecución en este sistema)

## Características

- **Registro de Vecinos**: Permite almacenar información relevante de cada vecino para mantener una base de datos actualizada.
- **Control de Aportes**: Se pueden registrar los montos aportados por cada vecino, lo que permite llevar un control detallado de las contribuciones.
- **Reporte de Aportes Totales**: Muestra de forma clara la suma de todos los aportes realizados, útil para la junta de vecinos y la comunidad.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tuusuario/JuntaDevecinos.git
   cd JuntaDevecinos
   ```

2. **Instalar las dependencias**:
   Asegúrate de tener Python y MySQL instalados en tu sistema. Luego, instala las dependencias necesarias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuración de la base de datos**:
   - Crea una base de datos en MySQL para el proyecto.
   - Ejecuta el script SQL proporcionado en el repositorio (`database_setup.sql`) para crear las tablas necesarias.
   - Configura las credenciales de acceso a la base de datos en el archivo de configuración del proyecto.

4. **Ejecución**:
   Compila y ejecuta el programa en un entorno Windows. Puedes hacer esto desde la línea de comandos:
   ```bash
   python main.py
   ```

## Contribuciones

Dado que este proyecto fue realizado como un aporte comunitario, no se espera una colaboración activa, pero cualquier mejora o sugerencia será bienvenida. 

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

---

**Nota**: Este proyecto fue una gran oportunidad para aplicar mis conocimientos en Python y MySQL y hacer una contribución significativa a mi comunidad.
