import pandas as pd
import matplotlib.pyplot as plt



def plot_data(key, data):
    for row in data:
        dates = []
        counts = []
        path, exp, wound, folder, count = row 
        if len(folder) == 16:
          dates.append(folder)
          counts.append(count)

    

  




if __name__ == "__main__":
  base =  "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Count Data/V3/" 
  file = "Data_V3.csv"
  path = base + file 

  exps_found = {}
  df = pd.read_csv(path, index_col = False)
  df = df[["Dropbox Path", "Experiment", "Wound", "Folder Name", "Count"]]
  data = df.values.tolist()
  for row in data:
      path, exp, wound, folder, count = row
      key = exp + " - " + wound
      if key in exps_found:
          exps_found[key].append(row)
      else:
          exps_found[key] = [row]


  for key in exps_found.keys():
      data = exps_found[key]
      plot_data(key, data)
      break
