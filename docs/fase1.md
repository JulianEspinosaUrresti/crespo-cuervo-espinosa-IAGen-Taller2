# Fase 1. Selección y justificación de componentes
**Caso:** EcoMarket busca mejorar la atención de consultas repetitivas, sin inventar respuestas cuando falten datos.

## Modelo de embeddings
**Seleccionado:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, abierto y multilingüe, utilizable en español. Genera vectores densos para comparar semánticamente consultas y fragmentos. Ventajas: ejecución local, sin tarifa por solicitud de embeddings y despliegue académico sencillo. Limitaciones: descarga y consumo de memoria, posibles errores con números de pedido y terminología específica; no se asume precisión medida sin evaluación. Para números de pedido se usa búsqueda exacta, no únicamente similitud semántica.
**Alternativa propietaria:** embeddings de API gestionada; simplifican operaciones pero implican costo variable, dependencia del proveedor y consideraciones de transferencia de datos.

## Base de datos vectorial
| Alternativa | Ventajas | Limitaciones | Decisión |
|---|---|---|---|
| ChromaDB | Gratuita para prototipo local, persistencia simple, integración LangChain | Operación distribuida y alta disponibilidad requieren diseño adicional | **Elegida** |
| Pinecone | Servicio administrado y opciones de escalado | Costo, dependencia de servicio externo y transferencia de información | Alternativa producción |
| Weaviate | Búsqueda vectorial y funcionalidades de escalamiento | Mayor complejidad de operación en autohospedaje | Alternativa si crece el sistema |

## Generación e integración
LangChain orquesta la recuperación; Ollama sirve `llama3.2:3b` localmente. No se necesita fine-tuning para incorporar cambios frecuentes de políticas: RAG actualiza documentos sin reentrenar el modelo. Un fine-tuning posterior podría ajustar estilo, pero no reemplazar una fuente de verdad actualizada.

**Costo:** software local sin tarifa por consulta de API, pero con costos reales de equipo, energía, mantenimiento y tiempo de inferencia. **Escalabilidad:** prototipo monousuario; producción exigiría autenticación, monitoreo, actualización incremental, pruebas de carga y posiblemente infraestructura administrada.

**Trade-off:** se prioriza claridad y privacidad local sobre la máxima capacidad generativa. El desempeño en español debe verificarse con pruebas y no se presenta como resultado medido.
