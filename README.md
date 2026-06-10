# Optimización del OEE mediante Mantenimiento Predictivo Inteligente en Activos Críticos Industriales

## Descripción del proyecto
Este proyecto corresponde al curso MCDI500 y aborda una problemática de mantenimiento predictivo aplicada a activos industriales críticos. El propósito general es construir una base técnica reproducible para analizar eventos de falla y su relación con métricas operacionales, con foco en la disponibilidad operacional y la optimización del indicador OEE.

## Problemática
Las fallas no programadas afectan directamente la disponibilidad operacional de los activos y deterioran el indicador OEE. En este contexto, el proyecto busca estructurar un flujo de trabajo reproducible que permita obtener, limpiar, transformar y dejar preparados los datos para fases posteriores de análisis y modelamiento.

## Dataset utilizado
Se utiliza el dataset `predictive_maintenance_dataset.csv`, almacenado en:

- `data/raw/predictive_maintenance_dataset.csv`

El conjunto original contiene 124494 registros y 12 columnas, incluyendo:
- una dimensión temporal (`date`),
- un identificador de activo (`device`),
- una variable objetivo binaria (`failure`),
- y nueve métricas operacionales (`metric1` a `metric9`).

## Estado actual del proyecto
Actualmente el repositorio contiene el trabajo desarrollado en:
- **Fase 1**: definición del problema, entorno reproducible y revisión inicial del dataset.
- **Fase 2**: pipeline de obtención, limpieza, transformación, validación y exportación del dataset procesado.

## Objetivo de la Fase 2
Implementar un pipeline reproducible de preprocesamiento de datos que permita:
- cargar el dataset original desde `data/raw/`,
- diagnosticar su calidad,
- eliminar duplicados,
- transformar la variable temporal,
- crear variables derivadas,
- validar técnicamente el resultado,
- y exportar el dataset final a `data/processed/`.

## Transformaciones aplicadas en la Fase 2
En el notebook de Fase 2 se realizaron las siguientes acciones:

- carga del dataset desde `data/raw/predictive_maintenance_dataset.csv`,
- revisión de valores nulos, duplicados y tipos de datos,
- identificación y eliminación de 1 registro duplicado,
- conversión de la columna `date` a formato `datetime`,
- creación de variables temporales derivadas: `year`, `month` y `day`,
- validación final mediante revisión estructural y comprobaciones automáticas (`assert`),
- exportación del resultado final a `data/processed/dataset_procesado.csv`.

## Resultado final del preprocesamiento
El dataset procesado final quedó almacenado en:

- `data/processed/dataset_procesado.csv`

Resultados principales:
- filas iniciales: **124494**
- filas finales: **124493**
- duplicados restantes: **0**
- valores nulos finales: **0**
- columna `date` convertida correctamente a tipo datetime
- variables derivadas `year`, `month` y `day` incorporadas al dataset final

## Estructura del proyecto
```text
mcdi500_s1_grupo7/
├── data/
│   ├── raw/
│   │   └── predictive_maintenance_dataset.csv
│   └── processed/
│       └── dataset_procesado.csv
├── notebooks/
│   ├── F1_Definicion.ipynb
│   └── F2_Preprocesamiento.ipynb
├── src/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
# Actualizacion Final F2 
