import unittest
from types import SimpleNamespace
from src.rag_ejemplo import preparar_contexto, buscar_pedido

class PruebasV3(unittest.TestCase):
    def test_politica_completa_en_devolucion(self):
        docs = [SimpleNamespace(metadata={"fuente":"faq.json","id":"FAQ-01"},page_content="FAQ")]
        texto = preparar_contexto("¿Puedo devolver un jabón abierto?", docs, None)
        self.assertIn("defectuoso", texto)
        self.assertIn("agente humano", texto)
    def test_politica_completa_en_dano(self):
        self.assertIn("agente humano", preparar_contexto("Llegó dañado", [], None))
    def test_pregunta_general_no_inyecta_politica(self):
        self.assertEqual(preparar_contexto("¿Cuánto cuesta el envío?", [], None), "")
    def test_pedido_retrasado(self):
        pedido, encontrado = buscar_pedido("ECO-1004")
        self.assertTrue(encontrado)
        self.assertEqual(pedido["estado"], "Retrasado")
        self.assertIsNone(pedido["entrega_estimada"])

if __name__ == "__main__":
    unittest.main()
