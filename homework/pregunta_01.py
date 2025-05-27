# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    # Se guardan las rutas en variables
    input_base = 'files/input'
    output_dir = 'files/output'
    
    # Se crea un directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    # Se inicia con el procesamiento de train y test
    for dataset in ['train', 'test']:
        data = []
        dataset_path = os.path.join(input_base, dataset)
        
        if not os.path.exists(dataset_path):
            continue
        
        for sentiment in ['positive', 'negative', 'neutral']:
            sentiment_path = os.path.join(dataset_path, sentiment)
            
            if not os.path.exists(sentiment_path):
                continue

            print(sentiment_path)
            
            for filename in sorted(os.listdir(sentiment_path)):
                if filename.endswith('.txt'):
                    filepath = os.path.join(sentiment_path, filename)
                    
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            phrase = f.read().strip()
                            data.append({
                                'phrase': phrase,
                                'target': sentiment
                            })
                    except Exception as e:
        
        # Guardar CSV
        if data:
            df = pd.DataFrame(data)
            output_path = os.path.join(output_dir, f'{dataset}_dataset.csv')
            df.to_csv(output_path, index=False)
            print(f" {output_path} creado con {len(df)} registros")
            print("Muestra de datos:")
            print(df.head(2))
        else:
            print(f" No se procesaron datos para {dataset}")
    
    return

print(pregunta_01())