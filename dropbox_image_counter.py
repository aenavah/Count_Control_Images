import pandas as pd
import dropbox
from dropbox.exceptions import AuthError


def count_images(path, dbx):
  data_dict = {}
  paths = []
  result = dbx.files_list_folder(path, recursive = True) #recursive = True
  for item in result.entries: #for each item in the root folder 
    item_path_string = item.path_display
    print(item_path_string)
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
      if data not in data_dict:
        data_dict[data] = 0
        paths.append(item_path_string)
      if data in data_dict:
        data_dict[data] += 1
  return data_dict, paths

def write_data(dictionary, paths_list, csv_name):
  wounds = []
  experiments = []
  foldernames = []
  folder_info = list(dictionary.keys())
  for folder in folder_info:
    wound = folder[0]
    wounds.append(wound)
    experiment = folder[1]
    experiments.append(experiment)
    folder_name = folder[2]
    foldernames.append(folder_name)
  file_counts = list(dictionary.values())
  header_list = ["Wound", "Experiment", "Folder Name", "Path", "Count"]
  df = pd.DataFrame({
    "Wound": wounds,
    "Experiment": experiments,
    "Folder Name": foldernames,
    "Path": paths,
    "Count": file_counts
  })
  df.to_csv("Count Data/" + csv_name)

if __name__ == "__main__":
  token = "sl.BtfGxxSQ2ePT8JOCMtij9cq7PPovFVlkbV50dwPHnumaRP5CX9tg8-LU4zfUQU4cR6MtXaz0TyKTBGBYXU0yy-X2DWQaMh1nzds4pgaDp6xQLTzlNFVNwwa54pJBYh3WKkx6F76q8pGv"
  dbx = dropbox.Dropbox(token)

  exp1_path = "/20220808-20220818 Swine Exp-1/DARPA_Porcine_Exp_1"
  exp2_path = "/20220906-20220916 Swine Expt-2" #cant find? 
  exp3_path = "/20220930-20221010 Swine Expt-3" #cant find
  exp4_path = "/20221021-20221104 Swine Expt-4/Wound Picture From Device/Porcine_Exp_4"
  exp5_path = "/20221104-20221118 Swine Expt-5/Exp_5_Wound Picture from device camera"
  exp6_path = "/20221201-20221216 Swine Expt-6/TA2 wound image_original name/Exp_6"
  exp7_path = "/20230110-20230123 Swine Expt-7/TA2 Wound Image_Original name"
  exp8_path = "/20230131-20230207 Swine Expt-8/TA2 wound picture by device camera_original name/Wound photo_sorted by wound"
  exp9_path = "/20230206-20230221 Swine Expt-9" #cant find
  exp10_path = "/20230221-20230306 Swine Expt-10/Wound Photos by Device/Wound photo_sorted by wound/"
  exp11_path = "/20230326-20230413 Swine Expt-11"
  exp12_path = "/20230508-20230523 Swine Expt-12"
  exp13_path = "/20230601-20230616 Swine Expt-13"
  exp14_path = "/20230814-20230829 Swine Expt-14"


  #data_dict, paths = count_images(exp1_path, dbx)
  #write_data(data_dict, paths, "Exp1_Count.csv")

  #data_dict, paths = count_images(exp4_path, dbx)
  #write_data(data_dict, paths, "Exp4_Count.csv")

  #data_dict, paths = count_images(exp5_path, dbx)
  #write_data(data_dict, paths, "Exp5_Count.csv")

  #data_dict, paths = count_images(exp6_path, dbx)
  #write_data(data_dict, paths, "Exp6_Count.csv")

  #data_dict, paths = count_images(exp7_path, dbx)
  #write_data(data_dict, paths, "Exp7_Count.csv")

  #data_dict, paths = count_images(exp8_path, dbx)
  #write_data(data_dict, paths, "Exp8_Count.csv")

  data_dict, paths = count_images(exp10_path, dbx)
  write_data(data_dict, paths, "Exp10_Count.csv")