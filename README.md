# Optimización del OEE mediante Mantenimiento Predictivo Inteligente en Activos Críticos Industriales

## Descripción del proyecto
Este proyecto corresponde a la Fase 1 del curso MCDI500 y aborda una problemática de mantenimiento predictivo aplicada a activos industriales críticos. El propósito general es establecer una base técnica reproducible para analizar eventos de falla y su relación con métricas operacionales, con foco en la disponibilidad operacional y la optimización del indicador OEE.

## Problemática
Las fallas no programadas afectan directamente la disponibilidad operacional de los activos y deterioran el indicador OEE. En este contexto, se busca estructurar un flujo de trabajo reproducible que permita, en fases posteriores, analizar variables operacionales asociadas a eventos de falla.

## Dataset utilizado
El proyecto utiliza un dataset histórico de mantenimiento predictivo compuesto por 124494 registros y 12 columnas. El conjunto incluye una dimensión temporal (date), un identificador de activo (device), una variable objetivo binaria (failure) y nueve métricas operacionales (metric1 a metric9).

## Hallazgos iniciales del dataset
- Se identifica una variable objetivo asociada a la ocurrencia de fallas en los equipos.
- No se identifican valores nulos en la revisión inicial.
- Se detecta 1 fila duplicada.
- El conjunto presenta un fuerte desbalance de clases.

## Objetivo de la Fase 1
Implementar la base técnica reproducible del proyecto mediante:
- estructura ordenada del repositorio,
- entorno virtual,
- registro de dependencias,
- notebook inicial de definición y análisis exploratorio,
- documentación técnica del proceso.

## Estructura del proyecto
```text
mcdi500_s1_grupo7/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
</> Markdown
## Reproducibilidad
Para reproducir el entorno del proyecto:

1. Crear y activar el entorno virtual:
```bash
py -m venv .venv
.venv\Scripts\activate
2. Instalar dependencias:

```bash
pip install -r requirements.txt
3. Ejecutar el entorno de trabajo:

```bash
jupyter notebook
## Ejecución del análisis

Una vez iniciado Jupyter Notebook, navegar a la carpeta `notebooks/` y abrir el archivo principal del proyecto. Ejecutar todas las celdas para reproducir completamente el análisis exploratorio de datos.
