# -*- coding = utf-8 -*-

import shutil, os

def remake_folder(folder_path):
  if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
  os.makedirs(folder_path)
