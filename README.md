# iberent_data

Este repositorio contiene la arquitectura de datos de *Iberent*, consta de una parte de Ingesta, Transformación y Carga de datos. Se tratarán
múltiples origenes. La metodología de trabajo va a ser mediante dbt Core.

## Estructura inicial del repositorio


iberent_data/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
├── config/                       # profiles.yml para dbt
│   └── profiles.yml
│
├── ingestion/                    # Parte de ingestión de datos (“fuentes”)
│   ├── oracle/                   # Carpeta para Oracle
│   │   ├── fetch_data.py
│   │   └── __init__.py
│   │
│   ├── sqlserver/                # Carpeta para SQL Server
│   │   ├── fetch_data.py
│   │   └── __init__.py
│   │
│   ├── files/                    # Ejemplo: ficheros planos, FTP, etc.
│   │   ├── fetch_csv.py
│   │   └── __init__.py
│   │
│   └── load/                     # Carga genérica al warehouse
│       ├── to_warehouse.py
│       └── __init__.py
│
└── transform/                    # Parte de transformación (dbt Core)
    ├── dbt_project.yml
    ├── profiles.yml             # symlink o copia de ../config/profiles.yml
    ├── models/
    │   ├── strategy/            # Modelos para área “strategy”
    │   │   ├── raw/             # (opcional) si quieres raw por área
    │   │   ├── staging/
    │   │   ├── silver/
    │   │   └── marts/
    │   │
    │   ├── admin/               # Modelos para área “admin”
    │   │   ├── staging/
    │   │   ├── silver/
    │   │   └── marts/
    │   │
    │   └── renove/              # Modelos para área “renove”
    │       ├── staging/
    │       ├── silver/
    │       └── marts/
    │
    ├── snapshots/
    ├── macros/
    ├── seeds/
    ├── tests/
    └── analyses/

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
