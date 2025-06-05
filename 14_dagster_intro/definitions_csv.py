# ===================== #
#                       #
#         Set up        #
#                       #
# ===================== #

import pandas as pd
import dagster as dg
import matplotlib.pyplot as plt

# ===================== #
#                       #
#         Asset         #
#                       #
# ===================== #

@dg.asset
def csv_data():
    df = pd.read_csv("sample_data.csv")
    return df

@dg.asset
def age_plot(csv_data: pd.DataFrame):
    plt.figure(figsize=(8, 6))
    plt.hist(csv_data['age'])
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plot_path = "age_distribution.png"
    plt.savefig(plot_path)
    
# ===================== #
#                       #,



#         Job           #
#                       #
# ===================== #

csv_data_job = dg.define_asset_job(name="csv_data_job", selection=["csv_data"])
age_plot_job = dg.define_asset_job(name="age_plot_job", selection=["age_plot"])

# ===================== #
#                       #
#       Schedule        #
#                       #
# ===================== #

csv_data_schedule = dg.ScheduleDefinition(job=csv_data_job, 
                                          cron_schedule="*/5 * * * *", # Runs at minute 0, hour 0 (midnight), every day of the month, every month, all days of the week, CEST
)

# ===================== #
#                       #
#        Sensor         #
#                       #
# ===================== #

@dg.asset_sensor(asset_key=dg.AssetKey("csv_data"), 
                job=age_plot_job)
def age_plot_sensor(context): 
    yield dg.RunRequest()

# ===================== #
#                       #
#      Definitions      #
#                       #
# ===================== #

defs = dg.Definitions(
                        assets=[csv_data, age_plot],
                        jobs=[csv_data_job, age_plot_job],
                        schedules=[csv_data_schedule],
                        sensors=[age_plot_sensor],
)