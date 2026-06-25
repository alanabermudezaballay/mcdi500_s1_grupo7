from src.procesamiento import Transformador

class PipelineF3:
    def __init__(self, df):
        self.transformador = Transformador(df)

    def ejecutar(self):
        try:
            # Aquí es donde llamas a tus métodos
            return self.transformador._df
        except Exception as e:
            print(f"Error en el flujo: {e}")