# This is auto-generated python wrapper.
import rpy2.robjects as robjects
import os
import json
from rpy2.robjects import r, pandas2ri
pandas2ri.activate()

def init():
    global r_run
    os.environ["AZUREML_MODEL_DIR"] = os.path.dirname(os.path.realpath(__file__))
    print(os.path.dirname(os.path.realpath(__file__)))
    
    score_r_path = os.path.join(os.path.dirname(
      os.path.realpath(__file__)),
      "score.R")

    # handle path for windows os
    score_r_path = score_r_path.replace('\\', '/')
    robjects.r.source("{}".format(score_r_path))
    r_run = robjects.r['init']()

def run(input_data):
    dataR = r_run(input_data)
    return list(dataR)
