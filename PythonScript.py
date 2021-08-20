import pandas as pd
import numpy as np
datos = pd.read_csv('/home/jc/Documents/GitHub/mypythonadventure/NotasIngresos.csv')
datos.head()
hist = datos.hist()
datos.describe()
datos.Notas.describe()
datos.info()
datos['Ingreso Familiar'].describe()
datos['Ingreso Familiar'].hist()
datos['Fuente'] = 'Colombia'
datos.head()
del datos['Fuente']
datos.head()
datos['Altos Ingresos'] = np.where(datos['Ingreso Familiar']>36000, True, False)
datos.head()
datos[10:25]['Ingreso Familiar']
datos[10:25]['Altos Ingresos']
datos[8:16]