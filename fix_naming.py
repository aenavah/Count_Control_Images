import pandas as pd 

def correct_naming(base_folder, folder):
  indexes_to_add_underscore = [3, 5, 7, 9]
  path = base_folder + folder
  df = pd.read_csv(path)

  df = df[["Wound", "Folder Name", "Count"]]

  df["Folder Name"] = df["Folder Name"].astype(str).str.replace("_", "")
  df["Folder Name"] = df["Folder Name"].apply(lambda x: ''.join(c if i not in indexes_to_add_underscore else c + '_' for i, c in enumerate(x)))

  print(df)

if __name__ == "__main__":
  base_folder = "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Count Data/V2/"

  folder = "Exp1_Pig305.csv"
  correct_naming(base_folder, folder)