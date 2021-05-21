import pandas as pd
import wget
import ssl
import urllib3
import os.path
from pathlib import Path
import requests
from datetime import datetime
import time

urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

# sets a general class for information
class DataTable:

    def __init__(self, grain_type=''):
        self.grain_type = grain_type
        self.current_marketing_year_sheet = None
        self.previous_marketing_year_sheet = None
        self.sheet_2019 = None
        self.current_week_date = None
        self.previous_week_date = None

# removes files from directory
    def remove_files(self):
        print('deleting')
        os.remove('./CY2021.csv')
        os.remove('./CY2020.csv')
        os.remove('./CY2019.csv')
        os.remove('./Wheat.xlsx')
        os.remove('./Corn.xlsx')
        os.remove('./Soybeans.xlsx')

# downloads files
    def _download_files(self):
        print("_download")
        url = 'https://fgisonline.ams.usda.gov/ExportGrainReport/CY2021.csv'
        self.current_marketing_year_sheet = wget.download(url, out="/home/ec2-user/inspections_final")
        url = 'https://fgisonline.ams.usda.gov/ExportGrainReport/CY2020.csv'
        self.previous_marketing_year_sheet = wget.download(url, out="/home/ec2-user/inspections_final")
        url = 'https://fgisonline.ams.usda.gov/ExportGrainReport/CY2019.csv'
        self.sheet_2019 = wget.download(url, out="/home/ec2-user/inspections_final")

# check if files exist in the directory before making calculation to avoid FILE NOT FOUND ERROR
    def files(self):
        print("files")
        if not os.path.isfile('./CY2021.csv') and not os.path.isfile('./CY2020.csv') and self.updates_checker():
            self._download_files()
        elif os.path.isfile('./CY2021.csv') and os.path.isfile('./CY2020.csv') and not self.updates_checker():
            os.remove('./CY2021.csv')
            os.remove('./CY2020.csv')
            os.remove('./CY2019.csv')
            time.sleep(60)
            print("sleeping1")
            self.files()
        elif os.path.isfile('./CY2021.csv') and os.path.isfile('./CY2020.csv') and self.updates_checker():
            self.current_marketing_year_sheet = Path('CY2021.csv')
            self.previous_marketing_year_sheet = Path('CY2020.csv')
            self.sheet_2019 = Path('CY2019.csv')
        elif not os.path.isfile('./CY2021.csv') and not os.path.isfile('./CY2020.csv') and not self.updates_checker():
            print("sleeping2")
            time.sleep(60)
            self.files()

# checks if there were updates on the website - doublecheck from sender.py

    def updates_checker(self):
        url = "https://fgisonline.ams.usda.gov/ExportGrainReport/CY2021.csv"
        r = requests.head(url, verify=False)
        r2 = r.headers['Last-Modified']
        date_of_update = datetime.strptime(r2[5:-4], '%d %b %Y %H:%M:%S').date()
        today = datetime.today().date()
        # if you need to test output, change date to the last updated on the website in last_up varibale and
        # put it instead of today variable in if statement
        # last_up = datetime.strptime("2021-01-11", "%Y-%m-%d").date()

        if today == date_of_update:
            return True
        else:
            return False

# checks if dates for current and previous week were set. Otherwise, calls function to set them
    def week_dates(self):
        if self.current_week_date == None and self.previous_week_date == None:
            self._find_dates()
        else:
            print('no dates there')

# finds dates building the table with Pandas

    def _find_dates(self):
        with open(self.current_marketing_year_sheet, "rt") as file:
            table = (pd.read_csv(file, usecols=["Thursday"], parse_dates=["Thursday"]))
            self.current_week_date = table.iloc[-1].at["Thursday"]
            self.previous_week_date = self.current_week_date - pd.Timedelta(days=7)

# generates table for calculation, sending text and tables
    def weekly_table(self, grain="", data_file=None, date=None,
                       columns=["Thursday", "Grade", "Class",
                                "Grain", "Destination", "AMS Reg", "Metric Ton"],
                       index="Destination", margins=None, name=None):

        with open(data_file, "rt") as file:
            table = (pd.read_csv(file,
                                 usecols=columns,
                                 parse_dates=["Thursday"])
                     .query('Thursday == @date and Grain == @grain')
                     .pivot_table(values="Metric Ton",
                                  index=index,
                                  columns="Class",
                                  aggfunc="sum",
                                  fill_value=0,
                                  margins=margins,
                                  margins_name=name

                                  )
                     )

        current_week_volumes = table.sum().sum()
        weekly_by_class = table.sum(0).sort_values(ascending=False)
        weekly_by_destination = table.sum(1).sort_values(ascending=False)
        weekly_by_port = table.sum(1).sort_values(ascending=False)

        if margins:
            pivot_table = table.sort_values("Total", ascending=False)
        else:
            pivot_table = None

        return current_week_volumes, weekly_by_class,\
                          weekly_by_destination, weekly_by_port, pivot_table

# populates variables with all the needed data. Names of the function do exactly the same what they mean

class Grains(DataTable):

    def __init__(self, grain_type=''):
        super().__init__(grain_type)
        self.current_week_volume = None
        self.previous_week_volume = None
        self.weekly_volumes_change = None
        self.current_marketing_year_volume = None
        self.previous_marketing_year_volume = None
        self.marketing_yoy_change = None
        self.types_volumes = None
        self.ports_volumes = None
        self.destinations_volumes = None
        self.pivot_table = None

    def find_current_week_volume(self):
        self.current_week_volume = self.weekly_table(self.grain_type,
                                                     self.current_marketing_year_sheet,
                                                     self.current_week_date)[0]

    def find_previous_week_volume(self):
        self.previous_week_volume = self.weekly_table(self.grain_type,
                                                      self.current_marketing_year_sheet,
                                                      self.previous_week_date)[0]

    def find_weekly_change(self):
        current = self.current_week_volume
        previous = self.previous_week_volume
        self.weekly_volumes_change = ((current - previous) / previous) * 100

    def find_current_marketing_year_volume(self):
        current_volumes = 0
        with open(self.current_marketing_year_sheet, "rt") as file:
            table = (pd.read_csv(file, usecols=["Thursday", "Grain", "Metric Ton", "MKT YR"],
                                 parse_dates=['Thursday', 'MKT YR']))
            current_marketing_year = table.iloc[-1].at["MKT YR"]
            mask1 = table["MKT YR"] == current_marketing_year
            mask2 = table["Grain"] == self.grain_type
            table = table[mask1 & mask2]
            volumes = table["Metric Ton"].sum()
            current_volumes += volumes

        with open(self.previous_marketing_year_sheet, "rt") as file:
            table = (pd.read_csv(file, usecols=["Thursday", "Grain", "Metric Ton", "MKT YR"],
                                 parse_dates=['Thursday', 'MKT YR']))
            current_marketing_year = table.iloc[-1].at["MKT YR"]
            mask1 = table["MKT YR"] == current_marketing_year
            mask2 = table["Grain"] == self.grain_type
            table = table[mask1 & mask2]
            volumes = table["Metric Ton"].sum()
            current_volumes += volumes
            self.current_marketing_year_volume = current_volumes

    def find_previous_marketing_year_volume(self):
        prev_volumes = 0
        with open(self.previous_marketing_year_sheet, "rt") as file:
            table = pd.read_csv(file, usecols=['Thursday', 'Grain', 'Metric Ton', 'MKT YR'],
                                parse_dates=['Thursday', "MKT YR"])
            previous_marketing_year = table.iloc[0].at['MKT YR']
            to_date = (self.current_week_date + pd.Timedelta(days=2)) - pd.Timedelta(days=365)
            mask1 = table['Thursday'] <= to_date
            mask2 = table['MKT YR'] == previous_marketing_year
            mask3 = table['Grain'] == self.grain_type
            table = table[mask1 & mask2 & mask3]
            volumes = table["Metric Ton"].sum()
            prev_volumes += volumes

        with open(self.sheet_2019, "rt") as file:
            table = pd.read_csv(file, usecols=['Thursday', 'Grain', 'Metric Ton', 'MKT YR'],
                                    parse_dates=['Thursday', "MKT YR"])
            previous_marketing_year = table.iloc[-1].at['MKT YR']
            to_date = (self.current_week_date + pd.Timedelta(days=2)) - pd.Timedelta(days=365)
            mask1 = table['Thursday'] <= to_date
            mask2 = table['MKT YR'] == previous_marketing_year
            mask3 = table['Grain'] == self.grain_type
            table = table[mask1 & mask2 & mask3]
            volumes = table["Metric Ton"].sum()
            prev_volumes += volumes
            self.previous_marketing_year_volume = prev_volumes

    def find_marketing_year_change(self):
        current = self.current_marketing_year_volume
        previous = self.previous_marketing_year_volume
        self.marketing_yoy_change = ((current - previous) / previous) * 100

    def find_types_volumes(self):
        self.types_volumes = self.weekly_table(self.grain_type,
                                               self.current_marketing_year_sheet,
                                               self.current_week_date)[1]

    def find_ports_volumes(self):
        self.ports_volumes = self.weekly_table(self.grain_type,
                                              self.current_marketing_year_sheet,
                                              self.current_week_date,
                                              index="AMS Reg")[3]

    def find_destinations_volumes(self):
        self.destinations_volumes = self.weekly_table(self.grain_type,
                                                      self.current_marketing_year_sheet,
                                                      self.current_week_date)[2]

    def find_pivot_table(self):
        self.pivot_table = self.weekly_table(self.grain_type,
                                             self.current_marketing_year_sheet,
                                             self.current_week_date,
                                             margins=True,
                                             name="Total")[4]



