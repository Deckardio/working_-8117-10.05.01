import sys
import os

LIBRARY_PATH = os.path.dirname(os.path.abspath(__file__))
if not LIBRARY_PATH in sys.path:
    sys.path.append(LIBRARY_PATH)


from src import collect_data, create_columns
from run_column_names_collecting import parseColumns
import click
import os
import pandas as pd
    




def parseEvtx(logs_file: str):
    temp_filename = os.path.basename(logs_file);
    
    if (temp_filename.endswith(".evtx")):
        temp_filename = temp_filename[:-5]
        
    temp_cols_name = f"temp/cols_{temp_filename}.txt"
    temp_table_name = f"temp/evtx_{temp_filename}.txt"
    
    parseColumns(logs_file, temp_cols_name)
    column_names = create_columns.get_short_name(temp_cols_name)
    
    collect_data.run(logs_file, temp_table_name, column_names)
    return pd.read_csv(temp_table_name)
    

@click.command()
@click.option("--fieldnames", '-f', help="Путь с именем  до файла с именами колонок", required=True)
@click.option("--logs_file", '-l', help="Путь с именем  до файла логов", required=True)
@click.option("--result_file", '-r', help="Путь с именем для сохранения файла csv", required=True)
def run(fieldnames: str, logs_file: str, result_file: str):
    column_names = create_columns.get_short_name(fieldnames)
    collect_data.run(logs_file, result_file, column_names)


if __name__ == '__main__':
    run()
