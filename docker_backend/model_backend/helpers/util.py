import os
import sys
import requests
import numpy as np

curpath = os.path.abspath(os.curdir)
tf_path = os.path.join(curpath, 'helpers/tensorflow')
sys.path.append(tf_path)
