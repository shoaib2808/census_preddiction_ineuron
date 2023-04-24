import os
import sys
import pickle

def save_obj(Path,obj):
    with open(Path,'wb') as f:
      pickle.dump(obj,f)