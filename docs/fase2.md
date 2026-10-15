# Fase 2. Base de conocimiento
**Fuentes ficticias:**
1. `data/politica_devoluciones.md`: política comercial estructurada por secciones.
2. `data/inventario.json`: catálogo, existencias y descripción.
3. `data/faq.json`: preguntas frecuentes con respuestas.
4. `data/pedidos.json`: 12 pedidos de prueba (datos transaccionales simulados).

## Segmentación (chunking)
- **Tamaño fijo:** sencillo, pero puede cortar condiciones de una devolución o separar una respuesta de su pregunta.
- **Por párrafos / estructura:** conserva reglas y FAQs completas; preferido para textos cortos y estructurados.
- **Recursiva:** útil para documentos largos cuando se excede el tamaño de fragmento; se usa como respaldo para la política (separadores jerárquicos, 600 caracteres, 80 de solapamiento).

**Elección:** una FAQ por fragmento, un producto por fragmento y secciones coherentes para la política. Los pedidos NO se recuperan solo por similitud: se consultan exactamente por identificador en JSON, evitando confundir códigos parecidos.

## Indexación
1. Leer y validar archivos UTF-8 / JSON.
2. Transformar FAQs y productos en documentos con metadatos `fuente`, `tipo`, `id`.
3. Dividir política en fragmentos coherentes con el separador recursivo.
4. Obtener embeddings con el modelo multilingüe.
5. Guardar vectores y metadatos en ChromaDB persistente.
6. Para cada consulta, recuperar hasta cuatro fragmentos; adjuntar datos de pedido únicamente cuando se proporcione un identificador exacto.

## Calidad
Se requieren documentos vigentes, consistentes y autorizados. Un chunk mal segmentado puede omitir una excepción; una política obsoleta puede producir una respuesta incorrecta aun si la búsqueda es perfecta. En producción: versionado, fecha de vigencia, permisos por documento y validación editorial.
