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

            if ("2022" in path_split[-1]) or ("2023" in path_split[-1]):
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
  "Wound": wounds,
  "Folder Name": folder_list,
  "Count": count_list
  })
  df.to_csv("Count Data/" + title)

if __name__ == "__main__":
#-------------------------
  ##using sorted by wound 
  # exp10_path = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Exp10"
  # Experiment, wound_list, folder_list, count_list = count_files_in_subdirectories(exp10_path, -2)
  # write_to_file(wound_list, folder_list, count_list, Experiment)
#-------------------------
  ##using sorted by wound 
  # exp11_path = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Exp11"
  # Experiment, wound_list, folder_list, count_list = count_files_in_subdirectories(exp11_path, -2)
  # write_to_file(wound_list, folder_list, count_list, Experiment)
#------------------------- 
  # https://www.dropbox.com/home/BETR%20DARPA%20Project/Research%20and%20Data/Porcine%20Experiment%20at%20Davis/20220808-20220818%20Swine%20Exp-1/DARPA_Porcine_Exp_1
  # exp1_path_305 = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Exp1/Pig 305"
  # wound_list, folder_list, count_list = count_files_in_subdirectories(exp1_path_305, -3)
  # print(len(wound_list), len(folder_list), len(count_list))
  # write_to_file(wound_list, folder_list, count_list, "Exp1" + "_Pig305")
  #---
  # exp1_path_306 = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Exp1/Pig 306"
  # Experiment = "Exp1"
  # wound_list, folder_list, count_list = count_files_in_subdirectories(exp1_path_306, -3)
  # write_to_file(wound_list, folder_list, count_list, "Exp1" + "_Pig306")
#-------------------------
   #https://www.dropbox.com/home/BETR%20DARPA%20Project/Research%20and%20Data/Porcine%20Experiment%20at%20Davis/20221021-20221104%20Swine%20Expt-4/Wound%20Picture%20From%20Device/Porcine_Exp_4
  # exp4_path_pig1 = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Exp4/Pi_1"
  # wound_list, folder_list, count_list = count_files_in_subdirectories(exp4_path_pig1, -2)
  # write_to_file(wound_list, folder_list, count_list, "Exp4" + "_Pig1")  
  #---
  # exp4_path_pig2 = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Exp4/Pi_2"
  # wound_list, folder_list, count_list = count_files_in_subdirectories(exp4_path_pig2, -2)
  # write_to_file(wound_list, folder_list, count_list, "Exp4" + "_Pig2")  
#-------------------------
  #https://www.dropbox.com/scl/fo/9bvsnkq5uin89gydiy2ts/h?rlkey=b89qq4qlnhja1vi0jpxf1s2q8&dl=0
  # exp5_path_pig2 = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Exp5/Pi_2"
  # wound_list, folder_list, count_list = count_files_in_subdirectories(exp5_path_pig2, -2)
  # write_to_file(wound_list, folder_list, count_list, "Exp5" + "_Pig2")  

#-------------------------
  #https://www.dropbox.com/home/BETR%20DARPA%20Project/Research%20and%20Data/Porcine%20Experiment%20at%20Davis/20221201-20221216%20Swine%20Expt-6/TA2%20wound%20image_original%20name/Exp_6
  # exp6_path_pig1 = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Exp6/Pi_1"
  # wound_list, folder_list, count_list = count_files_in_subdirectories(exp6_path_pig1, -2)
  # write_to_file(wound_list, folder_list, count_list, "Exp6" + "_Pig1")  


#https://www.dropbox.com/home/BETR%20DARPA%20Project/Research%20and%20Data/Porcine%20Experiment%20at%20Davis/20230110-20230123%20Swine%20Expt-7/TA2%20Wound%20Image_Original%20name
  #  exp7_path_pig3 = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Exp7/Pi_3"
  #  wound_list, folder_list, count_list = count_files_in_subdirectories(exp7_path_pig3, -2)
  #  write_to_file(wound_list, folder_list, count_list, "Exp7" + "_Pig3")  
   
  #https://www.dropbox.com/home/BETR%20DARPA%20Project/Research%20and%20Data/Porcine%20Experiment%20at%20Davis/20230131-20230207%20Swine%20Expt-8/TA2%20wound%20picture%20by%20device%20camera_original%20name 
  # exp8_path = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Exp8"
  # wound_list, folder_list, count_list = count_files_in_subdirectories(exp8_path, -2)
  # write_to_file(wound_list, folder_list, count_list, "Exp8")  
   
  #cant find exp9 
  #https://www.dropbox.com/home/BETR%20DARPA%20Project/Research%20and%20Data/Porcine%20Experiment%20at%20Davis/20230508-20230523%20Swine%20Expt-12/Wound%20Picture%20by%20device%20camera/Wound%20photo_sorted%20by%20wound
  # exp12_path = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Experiment Images/Exp12"
  # wound_list, folder_list, count_list = count_files_in_subdirectories(exp12_path, -2)
  # write_to_file(wound_list, folder_list, count_list, "Exp12")  
   
