import pandas as pd 
import os 



def correct_naming(path):
  indexes_to_add_underscore = [3, 5, 7, 9]
  df = pd.read_csv(path)
  df = df[["Dropbox Path", "Experiment", "Wound", "Folder Name", "Count"]]
  df["Folder Name"] = df["Folder Name"].astype(str).str.replace("-", "_")
  df["Folder Name"] = df["Folder Name"].astype(str).str.replace("_", "")
  print(df["Folder Name"].astype(str))
  df["Folder Name"] = df["Folder Name"].apply(lambda x: ''.join(c + '_' if len(x) == 12 and i in indexes_to_add_underscore else c for i, c in enumerate(x)))
  return df

if __name__ == "__main__":
  global base
  type_ = "Device"
  base = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Count Data/V2/"
  output_path = base + "Data_V2.csv"
  output_path_V2 = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Count Data/" + "Data_" + type_ + "_V3.csv"


  exp1_pig305_path = "Research and Data/Porcine Experiment at Davis/20220808-20220818 Swine Exp-1/DARPA_Porcine_Exp_1/Pig 305"
  exp1_pig306_path = "Research and Data/Porcine Experiment at Davis/20220808-20220818 Swine Exp-1/DARPA_Porcine_Exp_1/Pig 306"
  exp4_pig1_path = "Research and Data/Porcine Experiment at Davis/20221021-20221104 Swine Expt-4/Wound Picture From Device/Porcine_Exp_4/Pi_1"
  exp4_pig2_path = "Research and Data/Porcine Experiment at Davis/20221021-20221104 Swine Expt-4/Wound Picture From Device/Porcine_Exp_4/Pi_2"
  exp5_pig1_path = "Research and Data/Porcine Experiment at Davis/20221104-20221118 Swine Expt-5/Exp_5_Wound Picture from device camera/Pi_1"
  exp5_pig2_path = "Research and Data/Porcine Experiment at Davis/20221104-20221118 Swine Expt-5/Exp_5_Wound Picture from device camera/Pi_2"
  exp6_pig1_path = "Research and Data/Porcine Experiment at Davis/20221201-20221216 Swine Expt-6/TA2 wound image_original name/Exp_6/Pi_1"
  exp6_pig2_path = "Research and Data/Porcine Experiment at Davis/20221201-20221216 Swine Expt-6/TA2 wound image_original name/Exp_6/Pi_2"
  exp7_pig2_path = "Research and Data/Porcine Experiment at Davis/20230110-20230123 Swine Expt-7/TA2 Wound Image_Original name/Pi_2"
  exp7_pig3_path = "Research and Data/Porcine Experiment at Davis/20230110-20230123 Swine Expt-7/TA2 Wound Image_Original name/Pi_3"
  exp8_path = "Research and Data/Porcine Experiment at Davis/20230131-20230207 Swine Expt-8/TA2 wound picture by device camera_original name/Wound photo_sorted by wound"
  exp10_path = "Research and Data/Porcine Experiment at Davis/20230221-20230306 Swine Expt-10/Wound Photos by Device/Wound photo_sorted by wound"
  exp11_path = "Research and Data/Porcine Experiment at Davis/20230326-20230413 Swine Expt-11/Wound Photos by device camera/Wound photo_sorted by wound"
  exp12_path = "Research and Data/Porcine Experiment at Davis/20230508-20230523 Swine Expt-12/Wound Picture by device camera/Wound photo_sorted by wound"
  exp13_path = "Research and Data/ Porcine Experiment at Davis/20230601-20230616 Swine Expt-13/Wound Photos by Device Camera/Wound Picture_copied_sorted by wound"
  exp14_path = "Research and Data/ Porcine Experiment at Davis/20230814-20230829 Swine Expt-14/Wound Picture by Device Camera/Wound Picture Copied_Sorted by wound"

  exp1_pig305 = "Exp1_Pig305"
  exp1_pig306 = "Exp1_Pig306"
  exp4_pig1 = "Exp4_Pig1"
  exp4_pig2 = "Exp4_Pig2"
  exp5_pig1 = "Exp5_Pig1"
  exp5_pig2 = "Exp5_Pig2"
  exp6_pig1 = "Exp6_Pig1"
  exp6_pig2 = "Exp6_Pig2"
  exp7_pig2 = "Exp7_Pig2"
  exp7_pig3 = "Exp7_Pig3"
  exp8 = "Exp8"
  exp10 = "Exp10"
  exp11 = "Exp11"
  exp12 = "Exp12"
  exp13 = "Exp13"
  exp14 = "Exp14"

  ind_files = [exp1_pig305, exp1_pig306, exp4_pig1, exp4_pig2, exp5_pig1, exp5_pig2, exp6_pig1, exp6_pig2, exp7_pig2, exp7_pig3, exp8, exp10, exp11, exp12, exp13]
  dropbox_paths = [exp1_pig305_path, exp1_pig306_path, exp4_pig1_path, exp4_pig2_path, exp5_pig1_path, exp5_pig2_path, exp6_pig1_path, exp6_pig2_path, exp7_pig2_path, exp7_pig3_path, exp8_path, exp10_path, exp11_path, exp12_path, exp13_path]
  main_df = pd.DataFrame()
  for index in range(0,len(ind_files)-1):
    file = ind_files[index]
    file_path = base + file + ".csv"
    dropbox_path = (dropbox_paths[index])
    df_curr = pd.read_csv(file_path)
    dropbox_column = pd.DataFrame({'Dropbox Path': [dropbox_path] * df_curr.shape[0]})
    exp_column = pd.DataFrame({'Experiment': [file] * df_curr.shape[0]})

    df_curr_updated = pd.concat([dropbox_column[["Dropbox Path"]], exp_column[["Experiment"]], df_curr[["Wound", "Folder Name", "Count"]]], axis=1, ignore_index=True)
    main_df = pd.concat([main_df, df_curr_updated], axis=0, ignore_index=True)

  main_df.to_csv(output_path, header = ["Dropbox Path", "Experiment", "Wound", "Folder Name", "Count"])
  print("Output V2...")
  main_df_updated = correct_naming(output_path)
  print("Updated naming...")
  main_df_updated.to_csv(output_path_V2)
  print("Output V3...")