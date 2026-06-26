class Preprocesador:
    def __init__(self, df):
        self._df = df

class Transformador(Preprocesador):
    def imputar_nulos(self, columna):
        self._df[columna] = self._df[columna].fillna(0)
        return self

    def escalar_minmax(self, columnas):
        # Tu lógica aquí
        return self