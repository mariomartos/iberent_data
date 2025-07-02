# iberent_data

Este repositorio contiene la arquitectura de datos de *Iberent*, consta de una parte de Ingesta, Transformación y Carga de datos. Se tratarán
múltiples origenes. La metodología de trabajo va a ser mediante dbt Core.

## Estructura inicial del repositorio

.
├── .gitignore               # Ignora artefactos de Python, dbt y configuraciones locales
├── README.md                # Documentación de inicio y resumen de la arquitectura
├── requirements.txt         # Dependencias Python para los pipelines de ingestión
├── config/                  # Configuración y credenciales (no versionado)
│   └── profiles.yml         # Conexión de dbt al data warehouse (incluido en .gitignore)
│
├── pipelines/               # Código de ingestión y carga de datos
│   ├── extract/             # Scripts de extracción desde APIs, ficheros, etc.
│   ├── load/                # Scripts para cargar datos al data warehouse
│   └── dag/                 # Definición de DAGs (ej. Airflow) para orquestación
│
└── dbt/                     # Proyecto dbt Core para transformación de datos
    ├── dbt_project.yml      # Configuración del proyecto dbt
    ├── profiles.yml         # Enlazado a config/profiles.yml
    ├── models/
    │   ├── raw/             # Tablas/vistas con datos sin procesar
    │   ├── staging/         # Formateo inicial: nomenclatura y tipos
    │   ├── silver/          # Limpieza y enriquecimiento de datos
    │   └── marts/           # Tablas de hechos y dimensiones finales
    ├── snapshots/           # Versionado temporal de datos
    ├── macros/              # Macros reutilizables de dbt
    ├── seeds/               # Datos estáticos (CSV) cargados por dbt
    ├── tests/               # Tests de calidad específicos
    └── analyses/            # Consultas ad-hoc y análisis exploratorios

## Flujo de trabajo básico

1. Configura variables de entorno (`DB_USER`, `DB_PASS`, etc.).
2. Instala dependencias: `pip install -r requirements.txt`.
3. Ejecuta los pipelines de ingestión:

   ```bash
   python pipelines/extract/fetch_data.py
   python pipelines/load/to_warehouse.py
   ```
4. Modela con dbt Core:

   ```bash
   cd dbt
   dbt run --models raw
   dbt run --models staging
   dbt run --models silver
   dbt run --models marts
   dbt test
   ```
5. Genera y sirve la documentación de dbt:

   ```bash
   dbt docs generate
   dbt docs serve
   ```
