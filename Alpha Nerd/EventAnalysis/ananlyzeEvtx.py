from parser.run_data_collecting import parseEvtx

import pandas as pd
import numpy as np
import click
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

pd.options.mode.chained_assignment = None

def preprocess(data: pd.DataFrame, informative_columns: list):
    data = data.drop_duplicates(subset=data.columns.tolist())
    data = data.replace('0', 0) # В обучающих данных много подобных значений
    data = data.dropna()
    
    selected_data = pd.DataFrame()
    for column in informative_columns:
        if ( column not in data.columns ):
            print(f"No column {column} in dataframe! Adding empty column. ")
            selected_data = pd.concat([selected_data, pd.Series([0] * data.shape[0], name = column, dtype=np.int64)], axis = 1)
        else:
            selected_data = pd.concat([selected_data, data[column]], axis = 1)
            
    labelEncoders = {}
    for column_name in selected_data.columns:
        if (selected_data[column_name].dtype.__str__() not in ["int64", "float"]):
            print(f"Label encoding column - {column_name}")  
            selected_data[column_name] = selected_data[column_name].astype(str)
            labelEncoders[column_name] = LabelEncoder()
            labelEncoders[column_name].fit(selected_data[column_name])
            selected_data[column_name] = labelEncoders[column_name].transform(selected_data[column_name])
            
    return selected_data
    

def standardize(data: pd.DataFrame):
    for col in data.columns:
        s_scaler = StandardScaler()
        data[col] = s_scaler.fit_transform(data[col].to_numpy().reshape(-1, 1)).flatten()
    return data


def make_clusters_KMean(data: np.array):
    kmeans_model = KMeans(n_clusters = 2, n_init = 50)
    kmeans_model.fit(data)
    clusters, cluster_counts = np.unique(kmeans_model.labels_, return_counts=True)
    return clusters, cluster_counts


def validate_clusters(clusters: np.array, cluster_counts: np.array, threshold: float):
    """
    Validation checks if clusters have decent size.
    If not returns false
    """
    size = cluster_counts.sum()
    for cluster_ind, cluster_size in enumerate(cluster_counts):
        if cluster_size / size < threshold:
            return False
    return True
    

@click.command()
@click.option('--path_to_file', help = 'Path to evtx file')
@click.option('--threshold', default = 0.01, help = 'Maximum data fraction considered as anomaly')
def run(path_to_file: str, threshold: float):
    
    data = parseEvtx(path_to_file)
    
    informative_columns = ["EventID", "IpAddress", "LogonType", "AuthenticationPackageName", "TargetUserName", "SubjectDomainName"]
    
    data = preprocess(data, informative_columns)
    data = standardize(data)
    clusters, cluster_counts = make_clusters_KMean(data)
    
    is_valid = validate_clusters(clusters, cluster_counts, threshold)
    print("/"*50)
    if is_valid:
        print("No anomalies found in events!")
    else:
        print("An anomaly was found in events!")
    print("/"*50)
    
    
if __name__ == "__main__":
    run()
    
    
    
    