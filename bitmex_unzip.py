import gzip
import os
import shutil
import csv

def g_unzip_csv(file_path):
    try:
        with gzip.open(file_path,'rt') as f:
            with open(file_path[:-3],'x') as f_out: # 'x' is for the creation of a new file. change to 'wb' to wite to an existing file
                shutil.copyfileobj(f, f_out)
    except Exception as e:
        print(e.__class__, " occurred.")


if __name__ == "__main__":
    g_unzip_csv() # Add your file path

