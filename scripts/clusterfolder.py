# Manejo de archivos
import os
from pathlib import Path
from xmlrpc.client import Boolean
import cv2
import shutil

# Interfaz
import argparse
from termcolor import cprint

# Manejo de Datos
import numpy as np
import pandas as pd

# Agrupamiento
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans

# Constantes
shape = (9,9)
preprocess_method = "a"

# Funciones de Extracción de Información image -> Vector Information
def image2VectorA(file):
    image = cv2.imread(file)
    processed = cv2.cvtColor(image,cv2.COLOR_BGR2HLS)
    processed = cv2.resize(processed,shape)
    processed = processed[:,:,0]
    processed = processed.reshape(shape[0]*shape[1])
    return processed

def image2VectorB(file):
    image = cv2.imread(file)
    image = image[:,:,0]
    hist,bins = np.histogram(image.ravel(),360,[0,360])
    return hist

# Carga y Procesamiento de Datos
def load_data(dir):
    names = []
    images = []

    if not os.path.exists(dir):
        return []
    
    os.chdir(dir)

    for file in os.listdir("."):
        try :
            images.append(image2VectorA(file))
            names.append(file)
        except:
            names.pop()
            print(f"{file} is not an Image")
        finally:
            pass

    return names,images

# Get the dataframe with image and cluster tag
def cluster(method,names,data,n_clusters=1):
    if method == "kmeans":
        cprint("Using K-Means","yellow")
        model = KMeans(n_clusters,init="random")
        print("Fiting model ...")
        model.fit(data)
        dic = {"file":names,"cluster":model.labels_}
        df = pd.DataFrame(dic)
        print("Clustering Complete")
        return df

# Agrupa por carpetas según el dataframe dado
def group_dir(df):
    for file,cluster in df.values:
        cluster_dir = f"Cluster_{cluster}"

        if not os.path.exists(cluster_dir):
            os.mkdir(cluster_dir)

        print(f"{file} -> {cluster_dir}/{file}")
        shutil.move(file,cluster_dir)

def cli():
    parser = argparse.ArgumentParser(
        prog="Cluster all the images in a folder",
        usage="no usage"
    )

    parser.add_argument(
        "-d"
        "--directory",
        type=Path,
        required=True
    )

    parser.add_argument(
        "-m"
        "--method",
        type=str,
        required=True
    )

    parser.add_argument(
        "-csv",
        "--csvsave",
        type=Boolean,
        default=False,
        required=False
    )

    parser.add_argument(
        "-f",
        "--file-cluster",
        required=False,
        default=True
    )

    parser.add_argument(
        "-k",
        required=True,
        type=int,
        default=1
    )

    return parser.parse_args()

def main():
    args = cli()

    dir =  args.d__directory
    method = args.m__method
    save_on_csv = args.csvsave
    file_cluster = args.file_cluster
    num_clusters = args.k
    
    names,images = load_data(dir)
    df = cluster(method,names,images,num_clusters)

    if save_on_csv :
        df.to_csv("Data.csv")

    if file_cluster:
        group_dir(df)

if __name__=="__main__":
    main()