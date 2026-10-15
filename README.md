# EcoMarket — Taller Práctico #2: Sistema RAG
Prototipo académico. **Todos los datos empresariales son ficticios** y no representan políticas reales.

## Arquitectura
Python + LangChain + Sentence Transformers (`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`) + ChromaDB + Ollama (`llama3.2:3b`).

Flujo: documentos → chunks → embeddings → Chroma → búsqueda semántica → prompt con contexto → LLM → respuesta con referencias o abstención.

## Requisitos
- Python 3.10 o 3.11
- Ollama instalado y en ejecución; ejecutar `ollama pull llama3.2:3b`
- Recursos para descargar y ejecutar el modelo de embeddings y el LLM. La primera indexación requiere conexión para descargar embeddings.

## Instalación
```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m src.rag_ejemplo --indexar
python -m src.rag_ejemplo --pregunta "¿Cuál es el estado del pedido ECO-1003?"
python -m src.rag_ejemplo --pregunta "¿Puedo devolver un jabón abierto?"
python -m unittest discover -s tests -v
```
Iniciar Ollama previamente (`ollama serve`, si el servicio no está iniciado).
La base vectorial local se genera en `.chroma/` y no se sube a GitHub.
Para reindexar después de editar documentos: `python -m src.rag_ejemplo --indexar`.

## Documentación
- [Fase 1: componentes](docs/fase1.md)
- [Fase 2: documentos, chunking e indexación](docs/fase2.md)
- [Fase 3: integración, pruebas y limitaciones](docs/fase3.md)
- [Autoevaluación de rúbrica](docs/rubrica.md)

## Seguridad y alcance
No es una plataforma de producción. No hay autenticación, integración con ERP, actualización automática, observabilidad ni control de acceso por cliente. **No cargar datos personales reales.** La búsqueda vectorial no sustituye verificaciones transaccionales; los pedidos se consultan por ID exacto sobre un JSON ficticio. Las respuestas no ejecutan reembolsos.

## Versión 2: comparación de prompts
El prompt mejorado es el predeterminado. Para comparar:
```bat
python -m src.rag_ejemplo --pregunta "Cual es el estado del pedido ECO-1004?" --variante base
python -m src.rag_ejemplo --pregunta "Cual es el estado del pedido ECO-1004?" --variante mejorado
python -m src.evaluar --limite 12
```
Los resultados se guardan en `resultados/comparacion_prompts.csv`. Se requieren 24 inferencias, por lo que pueden tardar en CPU. Revisar manualmente y documentar los hallazgos en `docs/evaluacion.md`.

## Actualización V3
Consulta [mejoras y evaluación](docs/mejoras_v3.md). El prompt predeterminado ahora es `corregido`. Los resultados V2 se conservan sin alteración.
