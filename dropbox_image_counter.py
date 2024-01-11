import pathlib
import pandas as pd
import dropbox
from dropbox.exceptions import AuthError


def count_images(path, dbx):
  data_dict = {}
  paths = []
  result = dbx.files_list_folder(path, recursive = True) #recursive = True
  for item in result.entries: #for each item in the root folder 
    item_path_string = item.path_display
    #contains wound id, exp id, and ".img" extension
    if (("Wound" in item_path_string) and ("Exp" in item_path_string) and (".jpg" in item_path_string)):
      item_path_list = item_path_string.split("/")
      for cell in item_path_list:
        if "Wound" in cell:
          wound_number = cell
        if "Exp" in cell:
          if "t" not in cell:
            cell = cell.replace("Exp", "Expt")
          exp_number = cell
      if ".jpg" in item_path_list[-1]:
        img_folder = item_path_list[-2]
      data = wound_number, exp_number, img_folder
      #print("data" , data)
      #print("count " + str(count))
      print(item_path_string)
      print("----------------------------------------------")
      if data not in data_dict:
        data_dict[data] = 0
        paths.append(item_path_string)
      if data in data_dict:
        data_dict[data] += 1

  for key, value in data_dict.items():
    print(f"Key: {key}, Value: {value}")
  print(paths)


if __name__ == "__main__":
  token = "sl.BtcTfi-4w-E095SBqHKB5UVHM88xRc3MTHOdemgFdyOk8CA8CYinMFhHkoUaT7itdlo7xbMjICoUwtLBYEWPV6itusB8n85MpqsN_-A9M195DlguyXTdGK-kZXhDJowFFMSoGLetBPoL"
  dbx = dropbox.Dropbox(token)

  exp1_path = "/20220808-20220818 Swine Exp-1/DARPA_Porcine_Exp_1"
  exp2_path = "/20220906-20220916 Swine Expt-2"
  exp3_path = "/20220930-20221010 Swine Expt-3"
  exp4_path = "/20221021-20221104 Swine Expt-4"
  exp5_path = "/20221104-20221118 Swine Expt-5"
  exp6_path = "/20221201-20221216 Swine Expt-6"
  exp7_path = "/20230110-20230123 Swine Expt-7"
  exp8_path = "/20230131-20230207 Swine Expt-8"
  exp9_path = "/20230206-20230221 Swine Expt-9"
  exp10_path = "/20230221-20230306 Swine Expt-10"
  exp11_path = "/20230326-20230413 Swine Expt-11"
  exp12_path = "/20230508-20230523 Swine Expt-12"
  exp13_path = "/20230601-20230616 Swine Expt-13"
  exp14_path = "/20230814-20230829 Swine Expt-14"

  count_images(exp1_path, dbx)
