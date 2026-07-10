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

## Fase 4 — Proyecto Final Integrador

La Fase 4 consolida el proyecto transversal desarrollado en MCDI500, integrando los avances de F1, F2 y F3 en un notebook final reproducible.

### Notebook principal

`F4/F4_Proyecto_Final_Integrador.ipynb`

### Propósito

El objetivo de esta fase es integrar la definición del problema, el dataset procesado, el núcleo algorítmico, la programación orientada a objetos y las visualizaciones analíticas en una entrega final coherente y reproducible.

### Estructura por fases

- `F1/`: carpeta documental de la Fase 1. El notebook oficial se mantiene en `notebooks/F1_Definicion.ipynb`.
- `F2/`: carpeta documental de la Fase 2. El notebook oficial se mantiene en `notebooks/F2_Preprocesamiento.ipynb`.
- `F3/`: contiene el notebook de algoritmos, recursividad, complejidad y eficiencia.
- `F4/`: contiene el notebook integrador final del proyecto.
- `data/processed/`: contiene el dataset procesado utilizado como insumo para las fases posteriores.
- `changelog.md`: resume las mejoras y ajustes incorporados durante la fase final.

### Reproducibilidad

Para ejecutar el proyecto:

1. Clonar el repositorio.
2. Crear o activar el entorno virtual.
3. Instalar dependencias desde `requirements.txt`.
4. Ejecutar los notebooks en orden lógico:
   - `notebooks/F1_Definicion.ipynb`
   - `notebooks/F2_Preprocesamiento.ipynb`
   - `F3/F3_Algoritmos_Complejidad.ipynb`
   - `F4/F4_Proyecto_Final_Integrador.ipynb`

### Relación con el problema

El proyecto aborda la optimización del OEE mediante mantenimiento predictivo inteligente aplicado a activos críticos industriales. La Fase 4 permite comunicar los principales resultados técnicos mediante visualizaciones, conclusiones y una estructura final trazable.
## Actualización F4 - Proyecto Final Integrador

La Fase 4 consolida el trabajo desarrollado en F1, F2 y F3 mediante un notebook integrador que articula definición del problema, preparación del dataset, diseño algorítmico, programación orientada a objetos, visualizaciones analíticas, trazabilidad y reflexión final.

### Componentes incorporados en F4

- Integración de las fases previas del proyecto.
- Reestructuración del notebook según formato de entrega final.
- Índice académico alineado con la pauta de evaluación.
- Introducción, problemática, objetivos, metodología, resultados, discusión, conclusiones y bibliografía APA 7.
- Visualizaciones analíticas avanzadas:
  - Distribución de la variable objetivo `failure`.
  - Histograma con curva KDE.
  - Scatter plot con codificación de color.
  - Gráfico de violín.
  - Matriz de correlación o heatmap.
- Uso de paletas de Seaborn para mejorar la presentación visual.
- Declaración explícita del alcance del análisis respecto al OEE.

### Alcance técnico

El proyecto no calcula formalmente el OEE completo, ya que el dataset no contiene todas las variables necesarias para estimar disponibilidad, rendimiento y calidad. Sin embargo, el análisis se vincula con la dimensión de disponibilidad operacional, dado que estudia eventos de falla en activos industriales.

### Resultados base

- Total de registros procesados: 124.493.
- Total de eventos de falla: 106.
- Total de dispositivos únicos: 1.169.
- Total de registros sin falla: 124.387.

### Archivos principales

- `F4/F4_Proyecto_Final_Integrador.ipynb`
- `F4/F4_Proyecto_Final_Integrador_ejecutado.html`
- `data/processed/dataset_procesado.csv`
- `changelog.md`
