import os
import pandas as pd 

def count_files_in_subdirectories_V2(directory, dropbox_path, exp):
  lists = []
  for root, dirs, files in os.walk(directory):
    print(root)
    if "Day" in root.split("/")[-1]:
      Day = root.split("/")[-1]
      #file count per folder, experiment,   
      dictionary= {}
      for file in files:
        file = file.split("-")
        for cell in file:
            if "Day" in cell:
               Day = cell.replace(".jpeg", "")
            if "Wound" in cell:
              Wound = cell
              if Wound + Day in dictionary:
                dictionary[Wound + Day] += 1
              if Wound + Day not in dictionary:
                dictionary[Wound] = 1
      print(dictionary)
      for key in dictionary.keys():
        value = dictionary[key]
        lists.append([dropbox_path, exp, key, Day.replace(".",""), value])
      print(lists)
  return lists
        
       


def count_files_in_subdirectories(directory, neg_wound_index):
    try:
        wound_list = []
        folder_list = []
        count_list = []
        # Walk through the directory and its subdirectories
        for root, dirs, files in os.walk(directory):
            wound = " "
            folder_name = " "
            file_count = " "
            file_count = len(files)
            print(f"Number of files in '{root}': {file_count}")
            path = root
            path_split = path.split("/")
            if ("Wound" in path_split[neg_wound_index]):
              wound = path_split[neg_wound_index]
            if ("2022" in path_split[-1]) or ("2023" in path_split[-1]) or ("2024" in path_split[-1]):
              folder_name = path_split[-1]
            if (wound!=" " and file_count!=" " and folder_name != " "):
              wound_list.append(wound)
              count_list.append(file_count)
              folder_list.append(folder_name)

        print(len(wound_list), len(folder_list), len(count_list))
        return wound_list, folder_list, count_list
    except FileNotFoundError:
        print(f"Error: The specified directory '{directory}' does not exist.")

def write_to_file(wounds, folder_list, count_list, title):
  df = pd.DataFrame({
  "Dropbox Path": dropbox_path,
  "Experiment": exp,
  "Wound": wounds,
  "Folder Name": folder_list,
  "Count": count_list})
  df.to_csv("Count Data/V1/" + title)

if __name__ == "__main__":
  #user inputs---------------------: 
  type_ = "iPhone"
  base = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/"

  exp = "Exp18"
  dropbox_path = "/BETR DARPA Project/Research and Data/Porcine Experiment at Davis/20231212-20231222 Swine Expt-18/Wound Photos by iPhone"
  
  img_folder = "Experiment Images/" + exp 
  image_folder_path = base + img_folder
  csv_path = base + "Count Data/V1/" + type_ + "_" + exp + ".csv"

  #---------------------------------
  if type_ == "Device":
    #path = "YOURPATH/Wound_X/Date-Time/data.jpg" image path 
    wound_subdirectory = -2 #aligns with subdirectory above
    wound_list, folder_list, count_list = count_files_in_subdirectories(image_folder_path, wound_subdirectory)
    write_to_file(wound_list, folder_list, count_list, type_ + "_" + exp + ".csv")

if type_ == "iPhone":
    list = count_files_in_subdirectories_V2(image_folder_path, dropbox_path, exp)
    pd = pd.DataFrame(list)
    pd.to_csv(csv_path)