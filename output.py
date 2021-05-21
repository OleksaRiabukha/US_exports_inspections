from data import Grains
from text_generator import text_generator
import pandas as pd

# sets grains types, which will be used to generate output
grains_type = ["WHEAT", "CORN", "SOYBEANS"]

# aggregates the text and files, which will be sent to email
def generate_output(list_of_grains):
    wheat_text = ""
    corn_text = ""
    soybeans_text = ""
    for grain in list_of_grains:
        g = Grains(grain)
        g.files()
        g.week_dates()
        g.find_current_week_volume()
        g.find_previous_week_volume()
        g.find_weekly_change()
        g.find_current_marketing_year_volume()
        g.find_previous_marketing_year_volume()
        g.find_marketing_year_change()
        g.find_types_volumes()
        g.find_ports_volumes()
        g.find_destinations_volumes()
        g.find_pivot_table()
        if grain == "WHEAT":
            wheat_text += text_generator(g.grain_type, g.current_week_volume,
                       g.current_week_date, g.weekly_volumes_change,
                       g.ports_volumes, g.destinations_volumes,
                       g.types_volumes, g.current_marketing_year_volume,
                       g.marketing_yoy_change)
        elif grain == "CORN":
            corn_text += text_generator(g.grain_type, g.current_week_volume,
                       g.current_week_date, g.weekly_volumes_change,
                       g.ports_volumes, g.destinations_volumes,
                       g.types_volumes, g.current_marketing_year_volume,
                       g.marketing_yoy_change)
        elif grain == "SOYBEANS":
            soybeans_text += text_generator(g.grain_type, g.current_week_volume,
                       g.current_week_date, g.weekly_volumes_change,
                       g.ports_volumes, g.destinations_volumes,
                       g.types_volumes, g.current_marketing_year_volume,
                       g.marketing_yoy_change)
        if grain == "WHEAT":
            writer = pd.ExcelWriter("Wheat.xlsx", engine="xlsxwriter")
            g.destinations_volumes.to_excel(writer, sheet_name="Sheet1")
            g.ports_volumes.to_excel(writer, sheet_name="Sheet1", startrow=20)
            g.pivot_table.to_excel(writer, sheet_name="Sheet1", startrow=30)
            workbook = writer.book
            format1 = workbook.add_format({'num_format': '#,##0'})
            worksheet = writer.sheets["Sheet1"]
            worksheet.set_column('B:F', None, format1)
            writer.save()
        elif grain == "CORN":
            writer = pd.ExcelWriter("Corn.xlsx", engine="xlsxwriter")
            g.destinations_volumes.to_excel(writer, sheet_name="Sheet1")
            g.ports_volumes.to_excel(writer, sheet_name="Sheet1", startrow=20)
            g.pivot_table.to_excel(writer, sheet_name="Sheet1", startrow=30)
            workbook = writer.book
            format = workbook.add_format({'num_format': '#,##0'})
            worksheet = writer.sheets["Sheet1"]
            worksheet.set_column('B:F', None, format)
            writer.save()
        else:
            writer = pd.ExcelWriter("Soybeans.xlsx", engine="xlsxwriter")
            g.destinations_volumes.to_excel(writer, sheet_name="Sheet1")
            g.ports_volumes.to_excel(writer, sheet_name="Sheet1", startrow=25)
            g.pivot_table.to_excel(writer, sheet_name="Sheet1", startrow=35)
            workbook = writer.book
            format1 = workbook.add_format({'num_format': '#,##0'})
            worksheet = writer.sheets["Sheet1"]
            worksheet.set_column('B:F', None, format1)
            writer.save()
    return f"{wheat_text}\n{corn_text}\n{soybeans_text}"



