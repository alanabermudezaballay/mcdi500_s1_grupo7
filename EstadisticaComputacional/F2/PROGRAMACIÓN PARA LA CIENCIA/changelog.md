# Changelog del Proyecto ABP — Grupo 7

## [F4] - 2026-06-19

### Added
- Integración final del proyecto F1-F4 en el notebook `F4/F4_Proyecto_Final_Integrador.ipynb`.
- Incorporación de visualizaciones analíticas para comunicar resultados del proyecto.
- Inclusión de estructura referencial para las fases F1 y F2 mediante carpetas documentales.
- Preparación de cierre técnico con resultados, discusión, conclusiones y proyección.
- Consolidación del repositorio con carpetas F1, F2, F3 y F4.

### Changed
- Se fortalece la coherencia entre definición del problema, procesamiento de datos, núcleo algorítmico y comunicación de resultados.
- Se organiza el cierre técnico del proyecto final integrador, alineado con la rúbrica de Sumativa 4.
- Se mantiene la trazabilidad de los notebooks F1 y F2 dentro de la carpeta `notebooks/`, documentando su ubicación desde las carpetas F1 y F2.

### Fixed
- Se mejora la consistencia entre la estructura del repositorio y los criterios solicitados para la entrega final.
- Se refuerza la documentación del proceso para facilitar la reproducibilidad y revisión del proyecto.

### Technical rationale
- La Fase 4 integra, mejora y comunica los avances previos del proyecto, sin reemplazar el trabajo técnico desarrollado en F1, F2 y F3.
- La estructura final permite evidenciar continuidad metodológica, trazabilidad y organización por fases.
## [F4] Reestructuración final y visualizaciones analíticas avanzadas

### Added
- Índice académico alineado con el formato de entrega final.
- Sección de introducción y contextualización ajustada al enfoque de mantenimiento predictivo.
- Definición reforzada de problemática y objetivos.
- Sección de herramientas científicas y reproducibilidad.
- Sección de diseño de soluciones algorítmicas eficientes.
- Subsecciones de codificación funcional, preprocesamiento, validación técnica, eficiencia con `timeit` y recursividad.
- Sección formal de programación orientada a objetos.
- Set de visualizaciones analíticas avanzadas:
  - Barras de distribución de la variable objetivo `failure`.
  - Histograma con KDE.
  - Scatter plot con codificación por color.
  - Gráfico de violín.
  - Heatmap de correlación.
- Interpretación ejecutiva de visualizaciones.
- Sección de metodología, trazabilidad de mejoras y `changelog`.
- Resultados y discusión alineados con los nuevos gráficos.
- Conclusiones, reflexión crítica y bibliografía APA 7.

### Changed
- Se reestructuró el notebook F4 para seguir una narrativa académica completa.
- Se fortaleció la interpretación de resultados desde un enfoque de storytelling con datos.
- Se incorporó el análisis del desbalance extremo de la variable objetivo.
- Se ajustó la discusión para justificar futuras métricas como Recall, Precision y F1-Score.
- Se declaró explícitamente que el proyecto no calcula el OEE completo, sino que analiza señales asociadas a disponibilidad operacional.

### Fixed
- Se corrigió la interpretación de fallas por dispositivo, evitando presentarlas como ranking de criticidad cuando no existe reincidencia por activo.
- Se evitó sobreprometer resultados predictivos, aclarando que la Fase 4 corresponde a una base exploratoria, metodológica y reproducible.
- Se alinearon notebook, visualizaciones, discusión y conclusiones con los datos procesados: 124.493 registros, 106 fallas y 1.169 dispositivos únicos.

### Validated
- Notebook F4 ejecutado con `Restart & Run All`.
- HTML ejecutado exportado como evidencia reproducible.
- Visualizaciones generadas correctamente desde el dataset procesado.
