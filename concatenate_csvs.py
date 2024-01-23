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
  type_ = "iPhone"
  base = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Count Data/V1/"

  output_path = base + type_ + "_Data_V2.csv"
  output_path_V2 = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Count Data/" + "Data_" + type_ + "_V3.csv"

  exp1_pig305 = "Exp1_Pig305"
  exp1_pig306 = "Exp1_Pig306"
  exp2 = "Exp2"
  exp3 = "Exp3"
  exp4 = "Exp4"
  exp5 = "Exp5"
  exp6 = "Exp6"
  exp7 = "Exp7"
  exp8 = "Exp8"
  exp9 = "Exp9"
  exp10 = "Exp10"
  exp11 = "Exp11"
  exp12 = "Exp12"
  exp13 = "Exp13"
  exp14 = "Exp14"
  exp15 = "Exp15"
  exp16 = "Exp16"
  exp17 = "Exp17"
  exp18 = "Exp18"
  exp19 = "Exp19"

  ind_files = [exp1_pig305, exp1_pig306, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9, exp10, exp11, exp12, exp13, exp14, exp15, exp16, exp17, exp18, exp19]
  main_df = pd.DataFrame()
  for index in range(0,len(ind_files)-1):
    file = ind_files[index]
    file_path = base + type_ + "_" + file + ".csv"
    df_curr = pd.read_csv(file_path)
    main_df = pd.concat([main_df, df_curr], axis=0, ignore_index=True)

  main_df.to_csv(output_path, header = ["Index", "Dropbox Path", "Experiment", "Wound", "Folder Name", "Count"])
  print("Output V2...")
  main_df_updated = correct_naming(output_path)
  print("Updated naming...")
  main_df_updated.to_csv(output_path_V2)
  print("Output V3...")