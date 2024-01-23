import os
import pandas as pd 

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
            # Count the number of files in the current subdirectory
            file_count = len(files)
            # Print the count for the current subdirectory
            print(f"Number of files in '{root}': {file_count}")
            path = root
            path_split = path.split("/")
            #print(path_split)
            #print(path_split[-1])
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
  "Experiment": experiment,
  "Wound": wounds,
  "Folder Name": folder_list,
  "Count": count_list})
  df.to_csv("Count Data/V1/" + title)

if __name__ == "__main__":
  #user inputs---------------------: 
  dropbox_path = "path placeholder"
  type_ = "Device"
  #path = "YOURPATH/Wound_X/Date-Time/data.jpg" image path 
  path = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Pi_2"
  wound_subdirectory = -2 #aligns with subdirectory above
  experiment = "Exp4_Pig2" 
  #---------------------------------

  wound_list, folder_list, count_list = count_files_in_subdirectories(path, wound_subdirectory)
  write_to_file(wound_list, folder_list, count_list, type_ + "_" + experiment + ".csv")
