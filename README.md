# Marine Sightings

## Descripción

"Marine Sightings Service" es web services basado en API Restful, formato JSON y XML, construida con FastAPI que permite registrar y gestionar avistamientos de especies marinas. La aplicación permite a los usuarios crear, leer, actualizar y eliminar registros de lugares, especies, categorías taxonómicas y avistamientos.

## Características

- Registro de lugares
- Registro de especies
- Registro de categorías taxonómicas
- Registro de avistamientos
- API RESTful y formato JSON y XML

## Tecnologías Implementadas

- [FastAPI](https://fastapi.tiangolo.com/) - Framework web para construir APIs.
- [SQLModel](https://sqlmodel.tiangolo.com/) - ORM para trabajar con bases de datos.
- [SQLite](https://www.sqlite.org/index.html) - Base de datos ligera para almacenamiento.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Validación de datos y configuración de modelos.
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI para FastAPI.
- [Swagger UI](https://swagger.io/tools/swagger-ui/) - Interfaz de usuario para interactuar con la API.

## Requisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com//marine_sightings_service.git
   cd marine_sightings_service  
   ```

2. Crea un entorno virtual:

   ```bash
   python -m venv venv
   ```

3. Activa el entorno virtual:

   - En macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - En Windows:

     ```bash
     venv\Scripts\activate
     ```

4. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Inicia el servidor de desarrollo:

   ```bash
   uvicorn src.main:app --reload
   ```

2. Accede a la API en tu navegador o mediante herramientas como [Postman](https://www.postman.com/) o [cURL](https://curl.se/):

   - Documentación de la API: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Rutas de la API

### Lugares

- `POST /places/` - Crear un nuevo lugar
- `GET /places/` - Obtener todos los lugares
- `GET /places/{place_id}` - Obtener un lugar por ID
- `PUT /places/{place_id}` - Actualizar un lugar por ID
- `DELETE /places/{place_id}` - Eliminar un lugar por ID

### Especies

- `POST /species/` - Crear una nueva especie
- `GET /species/{specie_id}` - Obtener una especie por ID
- `PUT /species/{specie_id}` - Actualizar una especie por ID
- `DELETE /species/{specie_id}` - Eliminar una especie por ID

### Categorías Taxonómicas

- `POST /taxonomic_categories/` - Crear una nueva categoría taxonómica
- `GET /taxonomic_categories/{category_id}` - Obtener una categoría taxonómica por ID
- `PUT /taxonomic_categories/{category_id}` - Actualizar una categoría taxonómica por ID
- `DELETE /taxonomic_categories/{category_id}` - Eliminar una categoría taxonómica por ID

### Avistamientos

- `POST /sightings/` - Crear un nuevo avistamiento
- `GET /sightings/{sighting_id}` - Obtener un avistamiento por ID
- `PUT /sightings/{sighting_id}` - Actualizar un avistamiento por ID
- `DELETE /sightings/{sighting_id}` - Eliminar un avistamiento por ID

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de [kristianschajris@gmail.com](mailto:kristianschajris@gmail.com).
