# preprocesar_datos.py
import pandas as pd
import glob
import os

def ejecutar_preprocesamiento(train_folder, supp_folder, salida="df_final.parquet"):
    # 1. Cargar inputs
    input_files = sorted(glob.glob(os.path.join(train_folder, "input_2023_w*.csv")))
    df_input = pd.concat([pd.read_csv(f) for f in input_files], ignore_index=True)

    # 2. Cargar outputs
    output_files = sorted(glob.glob(os.path.join(train_folder, "output_2023_w*.csv")))
    df_output = pd.concat([pd.read_csv(f) for f in output_files], ignore_index=True)

    # 3. Cargar supplementary
    supp_file = os.path.join(supp_folder, "supplementary_data.csv")
    df_sup = pd.read_csv(supp_file)

    # 4. MERGES pesados
    df_merged = df_input.merge(df_sup, on=['game_id','play_id'], how='left')
    df_merged = df_merged.merge(df_output, on=['game_id','play_id','nfl_id','frame_id'], how='left')

    # 5. Guardar
    df_merged.to_parquet(salida)
    print(f">>> {salida} creado correctamente")

    return df_merged
