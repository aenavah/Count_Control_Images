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
  main_df = pd.DataFrame()
  for index in range(0,len(ind_files)-1):
    file = ind_files[index]
    file_path = base + file + ".csv"
    df_curr = pd.read_csv(file_path)
    main_df = pd.concat([main_df, df_curr], axis=0, ignore_index=True)

  main_df.to_csv(output_path, header = ["Dropbox Path", "Experiment", "Wound", "Folder Name", "Count"])
  print("Output V2...")
  main_df_updated = correct_naming(output_path)
  print("Updated naming...")
  main_df_updated.to_csv(output_path_V2)
  print("Output V3...")