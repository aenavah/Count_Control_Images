import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

plt.rcParams['font.family'] = 'Arial'


def plot_data(key, data, type_):
    date = ""
    count = ""
    dates = []
    counts = []
    for row in data:
        path, exp, wound, date, count = row 
        if len(date) == 16:
          date = datetime.strptime(date, "%Y_%m_%d_%H_%M")
          dates.append(date)
          counts.append(count)
        else:
            print("Unable to plot " + date + "...")

    sorted_indices = sorted(range(len(dates)), key=lambda k: dates[k])
    
    # Reorder dates and counts based on sorted indices
    dates = [dates[i] for i in sorted_indices]
    counts = [counts[i] for i in sorted_indices]

    plt.plot(dates, counts)
    title = key.replace(" ", "")
    title = title.replace("Exp", type_ + ": Experiment ")
    title = title.replace("Pig",  ", Pig ")
    title = title.replace("Wound", ", Wound ")
    title = title.replace("_", "")
    title = title.replace("-", "")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Number of Images")
    plt.subplots_adjust(bottom=0.2)

    date_formatter = mdates.DateFormatter("%Y-%m-%d %H:%M")
    plt.gca().xaxis.set_major_formatter(date_formatter)

    plt.xticks(fontsize = 8, rotation = 40, ha='right')
    plt.yticks(range(min(counts), max(counts)+1), fontsize = 8)
    plt.grid(axis='y', linestyle='dotted', alpha=0.5)

    plt.savefig(base + "Plots/" + type_ + "_" + key.strip())
    plt.close() 
    # for x, y in zip(dates,counts):
    #     plt.text(x, y, f'({x}, {y})', ha='right', va='bottom', fontsize = 5, rotation = 20)  # Display coordinates as labels

    #debugging:
    # df = pd.DataFrame({
    #     "Dates": dates,
    #     "Count": counts
    # })
    # df.to_csv(base + "/Plots/Individual Data/" + title + ".csv")

if __name__ == "__main__":
  global base
  type_ = "Device"
  base =  "/Users/alexandranava/Desktop/DARPA/Tasks/Count_Control_Images/Count Data/" 
  file = "/Data_" + type_ + "_V3.csv"
  path = base + file 

  exps_found = {}
  df = pd.read_csv(path, index_col = False)
  df = df[["Dropbox Path", "Experiment", "Wound", "Folder Name", "Count"]]
  data = df.values.tolist()
  for row in data:
      path, exp, wound, folder, count = row
      key = exp.strip() + " - " + wound.strip()
      if key in exps_found:
          exps_found[key].append(row)
      else:
          exps_found[key] = [row]

  for key in exps_found.keys():
      data = exps_found[key]
      print("------------------------------Plotting " + key + "...")          
      plot_data(key, data, type_)
      
