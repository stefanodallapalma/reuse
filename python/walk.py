"""
Python snippet to collect all files in a directory and its subdirectories.
"""

import os

PATH_TO_DIR = '.'  # Path to the directory to walk through
all_files = set()

for root, _, filenames in os.walk(PATH_TO_DIR):
  for file in filenames:
    filepath = os.path.join(root, file)
    all_files.add(filepath)
