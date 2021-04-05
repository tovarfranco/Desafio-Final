## Set Up de archivos:

- Tener el archivo properati.csv en el mismo directorio donde se encuentra la notebook.
- Tener instalados los requerimientos para poder correr las instrucciones (los usados en el curso).
- En la Notebook se generan varios 'warnings', pero de todas formas realiza la operación de la celda.

## Set Up de display en la Notebook:

Las siguientes líneas afectan la visualización de los dataframes (modifica la cantidad de columnas y filas visibles):

### Configuraciones de display():
pd.set_option("display.max_columns", 50)   # Limita la visualización a max 50 columnas. Si se excede genera "...". NO existe display.min_columns.

pd.set_option("display.max_rows", 200)     # Limita la visualización a max 20 columnas. Si se excede genera "..."

pd.set_option("display.min_rows", 10)      # Una vez que display.max_rows se excede, la display.min_rows determina cuántas filas se muestran.

#pd.reset_option("^display")               # Este comando resetea todas las opciones por defecto.
