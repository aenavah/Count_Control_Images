import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates

plt.rcParams['font.family'] = 'Arial'


def map_days_to_dates(day_list, start_date):
    date_dict = {}
    for day in day_list:
        if day.startswith("Day"):
            day_number = int(day[3:])  # Extract the number after "Day"
            date_dict[day] = start_date + timedelta(days=day_number)
        else:
            date_dict[day] = start_date
    return date_dict


def plot_data(key, data, type_):
    date = ""
    count = ""
    dates = []
    counts = []
    for row in data:
        if type_ == "iPhone":
            path, exp, wound, day, count = row 
            tmp = path.split("/")[4]
            tmp = tmp.split("-")
            date_init = tmp[0]
            year = int(date_init[0:4])
            month = int(date_init[4:6])
            day_ = int(date_init[6:8])
            date_of_day_0 = datetime(year, month, day_)
            days_list = ["Day 0", "Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8", "Day 9", "Day 10"]
            mapped_dates_dict = map_days_to_dates(days_list, date_of_day_0)
            date = mapped_dates_dict[day]
            if len(str(date).split(" ")[0]) == 10:
                dates.append(str(date))
                counts.append(count)
            else:
                print("Unable to plot " + str(date) + "...")


        if type_ == "Device":
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

    plt.xticks(fontsize = 8, rotation = 40, ha='right')
    plt.yticks(range(min(counts), max(counts)+1), fontsize = 8)
    plt.grid(axis='y', linestyle='dotted', alpha=0.5)

    plt.savefig(base + "Plots/" + type_ + "_" + key.strip())
    plt.close() 

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
      if type_ == "Device":     
        plot_data(key, data, type_)
      if type_ == "iPhone":
        plot_data(key, data, type_)
      
