import pandas as pd
import dropbox
from dropbox.exceptions import AuthError


def count_images(path, dbx, rec):
  data_dict = {}
  paths = []
  result = dbx.files_list_folder(path, recursive = rec) #recursive = True
  for item in result.entries: #for each item in the root folder 
    item_path_string = item.path_display
    print("-------------------")
    #print(path)
    print(item_path_string)
    #print(item)
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
    "Path": paths_list,
    "Count": file_counts
  })
  df.to_csv("Count Data/" + csv_name)

def count_images_V2(basepath, dbx, rec, wound_numbers):
  #for loop that goes through wound numbers and apprends to base path to make dbx of each wound folder. write each one separately 
  for num in wound_numbers:
    path = basepath + "/Wound_" + str(num)
    data_dict = {}
    paths = []
    result = dbx.files_list_folder(path, recursive = rec) #recursive = True
    for item in result.entries: #for each item in the root folder 
      item_path_string = item.path_display
      print(item_path_string)


def count_images_V3(basepath, dbx, wound_numbers):
    data_dict = {}

    # Function to count images in a folder
    def count_images_in_folder(folder_path):
        try:
            result = dbx.files_list_folder(folder_path, recursive=True)
        except dropbox.exceptions.DropboxException as e:
            print(f"Error listing folder {folder_path}: {e}")
            return 0

        image_count = sum(1 for entry in result.entries if isinstance(entry, dropbox.files.FileMetadata) and entry.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')))
        return image_count

    # Loop through wound numbers
    for num in wound_numbers:
        path = basepath + "/Wound_" + str(num)
        total_image_count = count_images_in_folder(path)

        # Store the total image count for the current wound folder in the data_dict
        data_dict[path] = total_image_count
        print(f"Total images in {path}: {total_image_count}")

        # Update counts for subfolders
        subfolder_paths = [subfolder for subfolder in data_dict.keys() if path in subfolder and subfolder != path]
        for subfolder_path in subfolder_paths:
            subfolder_count = count_images_in_folder(subfolder_path)
            data_dict[subfolder_path] = subfolder_count
            print(f"Total images in {subfolder_path}: {subfolder_count}")

    return data_dict

if __name__ == "__main__":
  token = "sl.BtdC-hFWimPcgo5OMAipT6lPPk7TCtXlk8QOik0yl6Y_D3amopFYBcj1193Wf9o5DpjvII9TowQ_Kqq8D9JImD1qHCwk18f-8VA0SuBe6xY0i4jcGHEskwFJqAWsq1NKRUZY4lNPPKup"
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
  exp10_path = "/20230221-20230306 Swine Expt-10/Wound Photos by Device/Wound photo_sorted by wound" #not working
  exp11_path = "/20230326-20230413 Swine Expt-11/Wound Photos by device camera/Wound photo_sorted by wound/Wound_7"
  exp12_path = "/20230508-20230523 Swine Expt-12"
  exp13_path = "/20230601-20230616 Swine Expt-13"
  exp14_path = "/20230814-20230829 Swine Expt-14"


  #data_dict, paths = count_images(exp1_path, dbx, True)
  #write_data(data_dict, paths, "Exp1_Count.csv")

  #data_dict, paths = count_images(exp4_path, dbx, True)
  #write_data(data_dict, paths, "Exp4_Count.csv")

  data_dict, paths = count_images(exp5_path, dbx, True)
  write_data(data_dict, paths, "Exp5_Count.csv")

  #data_dict, paths = count_images(exp6_path, dbx, True)
  #write_data(data_dict, paths, "Exp6_Count.csv")

  #data_dict, paths = count_images(exp7_path, dbx, True)
  #write_data(data_dict, paths, "Exp7_Count.csv")

  #data_dict, paths = count_images(exp8_path, dbx, True)
  #write_data(data_dict, paths, "Exp8_Count.csv")

  #count_images_V3(exp10_path, dbx, [1,2,3,5,6,7])

  #data_dict, paths = count_images(exp10_path, dbx, True)
  #write_data(data_dict, paths, "Exp10_Count.csv")