from sys import argv
import pandas as pd
import shutil
import os

def clusterFilesWithDir(dir,datasetpath):
    df = pd.read_csv(datasetpath)
    df = df.values

    os.chdir(dir)
    for index,file,label in df:
        labeldir = f"Cluster_{label}"

        if not os.path.exists(labeldir):
            os.mkdir(labeldir)

        try:
            print(f"Moving {file} -> {labeldir}/{file}")
            shutil.move(file,labeldir)
        except:
            print("Error")

if __name__ == "__main__":
    # clusterFilesWithDir dataset.csv .
    clusterFilesWithDir(argv[1],argv[2])