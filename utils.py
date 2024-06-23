from pathlib import Path
import pickle
from ensure import ensure_annotations
import os 

@ensure_annotations 
def save_file(file,path:Path):
   if os.path.exists(path):
        with open(file, "wb") as f:
        # Pickle the object and write it to the file
         pickle.dump(file, f)
    

@ensure_annotations 
def load_file(path:Path):
  if os.path.exists(path):
        with open(path, "rb") as f:
  # Load the pickled object from the file
            data = pickle.load(f)
            return data
