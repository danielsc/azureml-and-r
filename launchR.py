from __future__ import print_function

import argparse
import os
import sys

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  FLAGS, unparsed = parser.parse_known_args()
  # [sys.argv[0]]
  # ['--python_path', sys.executable] 
  command_line = ' '.join(['Rscript', '--vanilla']+unparsed)
  print('Launching:', command_line)
  os.system(command_line)