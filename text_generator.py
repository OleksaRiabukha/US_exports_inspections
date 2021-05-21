#if you need to change text, do it right here

# generate text for different grains and soybeans and clauses
def text_generator(grain_type, weekly_volume, current_week,
                   weekly_change, ports, destinations,
                   types_volumes, year_to_date, yoy_change):
    to_print = ""
    if grain_type == "WHEAT":
        if weekly_change > 0:
            to_print += f"Export inspections of US {grain_type.lower()} were up {round(weekly_change, 2)}% " \
                        f"in the week to {current_week:%B %d}, USDA data showed Monday.\n" \
                        f"Weekly inspections came at {weekly_volume:,} mt, while analysts were expecting " \
                        f"them in the range of YOUR INPUT.\n" \
                        f"Among the largest destinations were " \
                        f"{destinations.index[0].capitalize()} ({destinations.values[0]:,} mt), " \
                        f"{destinations.index[1].capitalize()} ({destinations.values[1]:,} mt), " \
                        f"{destinations.index[2].capitalize()} ({destinations.values[2]:,} mt), " \
                        f"{destinations.index[3].capitalize()} ({destinations.values[3]:,} mt), " \
                        f"{destinations.index[4].capitalize()} ({destinations.values[4]:,} mt), " \
                        f"{destinations.index[5].capitalize()} ({destinations.values[5]:,} mt), " \
                        f"{destinations.index[6].capitalize()} ({destinations.values[6]:,} mt).\n"
        if weekly_change < 0:
            to_print += f"Export inspections of US {grain_type.lower()} were down {round(weekly_change, 2)}% " \
                        f"in the week to {current_week:%B %d}, USDA data showed Monday.\n" \
                        f"Weekly inspections came at {weekly_volume:,} mt, while analysts were expecting " \
                        f"them in the range of YOUR INPUT.\n" \
                        f"Among the largest destinations were " \
                        f"{destinations.index[0].capitalize()} ({destinations.values[0]:,} mt), " \
                        f"{destinations.index[1].capitalize()} ({destinations.values[1]:,} mt), " \
                        f"{destinations.index[2].capitalize()} ({destinations.values[2]:,} mt), " \
                        f"{destinations.index[3].capitalize()} ({destinations.values[3]:,} mt), " \
                        f"{destinations.index[4].capitalize()} ({destinations.values[4]:,} mt), " \
                        f"{destinations.index[5].capitalize()} ({destinations.values[5]:,} mt), " \
                        f"{destinations.index[6].capitalize()} ({destinations.values[6]:,} mt).\n"

        if weekly_change == 0:
            to_print += f"Export inspections of US {grain_type.lower()} were unchanged. " \
                        f"in the week to {current_week:%B %d}, USDA data showed Monday.\n" \
                        f"Weekly inspections came at {weekly_volume:,} mt, while analysts were expecting " \
                        f"them in the range of YOUR INPUT.\n" \
                        f"Among the largest destinations were " \
                        f"{destinations.index[0].capitalize()} ({destinations.values[0]:,} mt), " \
                        f"{destinations.index[1].capitalize()} ({destinations.values[1]:,} mt), " \
                        f"{destinations.index[2].capitalize()} ({destinations.values[2]:,} mt), " \
                        f"{destinations.index[3].capitalize()} ({destinations.values[3]:,} mt), " \
                        f"{destinations.index[4].capitalize()} ({destinations.values[4]:,} mt), " \
                        f"{destinations.index[5].capitalize()} ({destinations.values[5]:,} mt), " \
                        f"{destinations.index[6].capitalize()} ({destinations.values[6]:,} mt).\n"

        if len(ports) == 6:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt, " \
                        f"{ports.index[3].capitalize()} inspected {ports.values[3]:,} mt, " \
                        f"{ports.index[4].capitalize()} loaded {ports.values[4]:,} mt," \
                        f"{ports.index[5].capitalize()} processed {ports.values[5]:,} mt.\n"
        elif len(ports) == 5:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt, " \
                        f"{ports.index[3].capitalize()} inspected {ports.values[3]:,} mt, " \
                        f"{ports.index[4].capitalize()} loaded {ports.values[4]:,} mt.\n"
        elif len(ports) == 4:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt, " \
                        f"{ports.index[3].capitalize()} inspected {ports.values[3]:,} mt.\n"
        elif len(ports) == 3:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt.\n"
        elif len(ports) == 2:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt.\n" \

        elif len(ports) == 1:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt.\n" \

        if len(types_volumes) == 6:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                        f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt), " \
                        f"{types_volumes.index[3].upper()} ({types_volumes.values[3]:,} mt), " \
                        f"{types_volumes.index[4].upper()} ({types_volumes.values[4]:,} mt), " \
                        f"{types_volumes.index[5].upper()} ({types_volumes.values[5]:,} mt).\n"
        elif len(types_volumes) == 5:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                        f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt), " \
                        f"{types_volumes.index[3].upper()} ({types_volumes.values[3]:,} mt), " \
                        f"{types_volumes.index[4].upper()} ({types_volumes.values[4]:,} mt).\n"
        elif len(types_volumes) == 4:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                        f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt), " \
                        f"{types_volumes.index[3].upper()} ({types_volumes.values[3]:,} mt).\n"
        elif len(types_volumes) == 3:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                        f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt).\n"
        elif len(types_volumes) == 2:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()}, with " \
                        f"{types_volumes.values[1]:,} mt weighted.\n "

        if yoy_change > 0:
            to_print += f"Weekly volumes pushed the total inspections since the start " \
                        f"of the 2020/21 marketing year to {round(year_to_date, 2):,} mt, "  \
                        f"up {round(yoy_change, 2)}% year-on-year.\n"
        elif yoy_change < 0:
            to_print += f"Weekly volumes pushed the total inspections since the start " \
                        f"of the 2020/21 marketing year to {round(year_to_date, 2):,} mt, " \
                        f"down {round(yoy_change, 2)}% year-on-year.\n"
        elif yoy_change == 0:
            to_print += f"Weekly volumes pushed the total inspections since the start " \
                        f"of the 2020/21 marketing year to {round(year_to_date, 2):,} mt, " \
                        f"unchanged year-on-year.\n"
        return to_print

    if grain_type == "CORN":
        if weekly_change > 0:
            to_print += f"Export inspections of US {grain_type.lower()} were up {round(weekly_change, 2)}% " \
                        f"in the week to {current_week:%B %d}, USDA data showed Monday.\n" \
                        f"Weekly inspections came at {weekly_volume:,} mt, while analysts were expecting " \
                        f"them in the range of YOUR INPUT.\n" \
                        f"Among the largest destinations were " \
                        f"{destinations.index[0].capitalize()} ({destinations.values[0]:,} mt), " \
                        f"{destinations.index[1].capitalize()} ({destinations.values[1]:,} mt), " \
                        f"{destinations.index[2].capitalize()} ({destinations.values[2]:,} mt), " \
                        f"{destinations.index[3].capitalize()} ({destinations.values[3]:,} mt), " \
                        f"{destinations.index[4].capitalize()} ({destinations.values[4]:,} mt), " \
                        f"{destinations.index[5].capitalize()} ({destinations.values[5]:,} mt), " \
                        f"{destinations.index[6].capitalize()} ({destinations.values[6]:,} mt).\n"
        if weekly_change < 0:
            to_print += f"Export inspections of US {grain_type.lower()} were down {round(weekly_change, 2)}% " \
                        f"in the week to {current_week:%B %d}, USDA data showed Monday.\n" \
                        f"Weekly inspections came at {weekly_volume:,} mt, while analysts were expecting " \
                        f"them in the range of YOUR INPUT.\n" \
                        f"Among the largest destinations were " \
                        f"{destinations.index[0].capitalize()} ({destinations.values[0]:,} mt), " \
                        f"{destinations.index[1].capitalize()} ({destinations.values[1]:,} mt), " \
                        f"{destinations.index[2].capitalize()} ({destinations.values[2]:,} mt), " \
                        f"{destinations.index[3].capitalize()} ({destinations.values[3]:,} mt), " \
                        f"{destinations.index[4].capitalize()} ({destinations.values[4]:,} mt), " \
                        f"{destinations.index[5].capitalize()} ({destinations.values[5]:,} mt), " \
                        f"{destinations.index[6].capitalize()} ({destinations.values[6]:,} mt).\n"

        if weekly_change == 0:
            to_print += f"Export inspections of US {grain_type.lower()} were unchanged. " \
                        f"in the week to {current_week:%B %d}, USDA data showed Monday.\n" \
                        f"Weekly inspections came at {weekly_volume:,} mt, while analysts were expecting " \
                        f"them in the range of YOUR INPUT.\n" \
                        f"Among the largest destinations were " \
                        f"{destinations.index[0].capitalize()} ({destinations.values[0]:,} mt), " \
                        f"{destinations.index[1].capitalize()} ({destinations.values[1]:,} mt), " \
                        f"{destinations.index[2].capitalize()} ({destinations.values[2]:,} mt), " \
                        f"{destinations.index[3].capitalize()} ({destinations.values[3]:,} mt), " \
                        f"{destinations.index[4].capitalize()} ({destinations.values[4]:,} mt), " \
                        f"{destinations.index[5].capitalize()} ({destinations.values[5]:,} mt), " \
                        f"{destinations.index[6].capitalize()} ({destinations.values[6]:,} mt).\n"

        if len(ports) == 6:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt, " \
                        f"{ports.index[3].capitalize()} inspected {ports.values[3]:,} mt, " \
                        f"{ports.index[4].capitalize()} loaded {ports.values[4]:,} mt," \
                        f"{ports.index[5].capitalize()} processed {ports.values[5]:,} mt.\n"
        elif len(ports) == 5:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt, " \
                        f"{ports.index[3].capitalize()} inspected {ports.values[3]:,} mt, " \
                        f"{ports.index[4].capitalize()} loaded {ports.values[4]:,} mt.\n"
        elif len(ports) == 4:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt, " \
                        f"{ports.index[3].capitalize()} inspected {ports.values[3]:,} mt.\n"
        elif len(ports) == 3:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt.\n"
        elif len(ports) == 2:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt.\n" \

        elif len(ports) == 1:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt.\n" \

        if len(types_volumes) == 6:
                to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                            f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                            f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                            f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt), " \
                            f"{types_volumes.index[3].upper()} ({types_volumes.values[3]:,} mt), " \
                            f"{types_volumes.index[4].upper()} ({types_volumes.values[4]:,} mt), " \
                            f"{types_volumes.index[5].upper()} ({types_volumes.values[5]:,} mt).\n"
        elif len(types_volumes) == 5:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                        f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt), " \
                        f"{types_volumes.index[3].upper()} ({types_volumes.values[3]:,} mt), " \
                        f"{types_volumes.index[4].upper()} ({types_volumes.values[4]:,} mt).\n"
        elif len(types_volumes) == 4:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                        f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt), " \
                        f"{types_volumes.index[3].upper()} ({types_volumes.values[3]:,} mt).\n"
        elif len(types_volumes) == 3:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                        f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt).\n"
        elif len(types_volumes) == 2:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()}, with " \
                        f"{types_volumes.values[1]:,} mt weighted.\n "

        if yoy_change > 0:
            to_print += f"Weekly volumes pushed the total inspections since the start " \
                        f"of the 2020/21 marketing year to {round(year_to_date, 2):,} mt, " \
                        f"up {round(yoy_change, 2)}% year-on-year.\n"
        elif yoy_change < 0:
            to_print += f"Weekly inspections pushed the total inspections since the start " \
                        f"of the 2020/21 marketing year to {round(year_to_date, 2):,} mt, " \
                        f"down {round(yoy_change, 2)}% year-on-year.\n"
        elif yoy_change == 0:
            to_print += f"Weekly volumes pushed the total inspections since the start " \
                        f"of the 2020/21 marketing year to {round(year_to_date, 2):,} mt, " \
                        f"unchanged year-on-year.\n"
        return to_print
    if grain_type == "SOYBEANS":
        if weekly_change > 0:
            to_print += f"Export inspections of US {grain_type.lower()} were up {round(weekly_change, 2)}% " \
                        f"in the week to {current_week:%B %d}, USDA data showed Monday.\n" \
                        f"Weekly inspections came at {weekly_volume:,} mt, while analysts were expecting " \
                        f"them in the range of YOUR INPUT.\n" \
                        f"Among the largest destinations were " \
                        f"{destinations.index[0].capitalize()} ({destinations.values[0]:,} mt), " \
                        f"{destinations.index[1].capitalize()} ({destinations.values[1]:,} mt), " \
                        f"{destinations.index[2].capitalize()} ({destinations.values[2]:,} mt), " \
                        f"{destinations.index[3].capitalize()} ({destinations.values[3]:,} mt), " \
                        f"{destinations.index[4].capitalize()} ({destinations.values[4]:,} mt), " \
                        f"{destinations.index[5].capitalize()} ({destinations.values[5]:,} mt), " \
                        f"{destinations.index[6].capitalize()} ({destinations.values[6]:,} mt).\n"
        if weekly_change < 0:
            to_print += f"Export inspections of US {grain_type.lower()} were down {round(weekly_change, 2)}% " \
                        f"in the week to {current_week:%B %d}, USDA data showed Monday.\n" \
                        f"Weekly inspections came at {weekly_volume:,} mt, while analysts were expecting " \
                        f"them in the range of YOUR INPUT.\n" \
                        f"Among the largest destinations were " \
                        f"{destinations.index[0].capitalize()} ({destinations.values[0]:,} mt), " \
                        f"{destinations.index[1].capitalize()} ({destinations.values[1]:,} mt), " \
                        f"{destinations.index[2].capitalize()} ({destinations.values[2]:,} mt), " \
                        f"{destinations.index[3].capitalize()} ({destinations.values[3]:,} mt), " \
                        f"{destinations.index[4].capitalize()} ({destinations.values[4]:,} mt), " \
                        f"{destinations.index[5].capitalize()} ({destinations.values[5]:,} mt), " \
                        f"{destinations.index[6].capitalize()} ({destinations.values[6]:,} mt).\n"

        if weekly_change == 0:
            to_print += f"Export inspections of US {grain_type.lower()} were unchanged. " \
                        f"in the week to {current_week:%B %d}, USDA data showed Monday.\n" \
                        f"Weekly inspections came at {weekly_volume:,} mt, while analysts were expecting " \
                        f"them in the range of YOUR INPUT.\n" \
                        f"Among the largest destinations were " \
                        f"{destinations.index[0].capitalize()} ({destinations.values[0]:,} mt), " \
                        f"{destinations.index[1].capitalize()} ({destinations.values[1]:,} mt), " \
                        f"{destinations.index[2].capitalize()} ({destinations.values[2]:,} mt), " \
                        f"{destinations.index[3].capitalize()} ({destinations.values[3]:,} mt), " \
                        f"{destinations.index[4].capitalize()} ({destinations.values[4]:,} mt), " \
                        f"{destinations.index[5].capitalize()} ({destinations.values[5]:,} mt), " \
                        f"{destinations.index[6].capitalize()} ({destinations.values[6]:,} mt).\n"

        if len(ports) == 6:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt, " \
                        f"{ports.index[3].capitalize()} inspected {ports.values[3]:,} mt, " \
                        f"{ports.index[4].capitalize()} loaded {ports.values[4]:,} mt," \
                        f"{ports.index[5].capitalize()} processed {ports.values[5]:,} mt.\n"
        elif len(ports) == 5:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt, " \
                        f"{ports.index[3].capitalize()} inspected {ports.values[3]:,} mt, " \
                        f"{ports.index[4].capitalize()} loaded {ports.values[4]:,} mt.\n"
        elif len(ports) == 4:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt, " \
                        f"{ports.index[3].capitalize()} inspected {ports.values[3]:,} mt.\n"
        elif len(ports) == 3:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt, " \
                        f"{ports.index[2].capitalize()} weighted {ports.values[2]:,} mt.\n"
        elif len(ports) == 2:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt, " \
                        f"{ports.index[1].capitalize()} handled {ports.values[1]:,} mt.\n" \

        elif len(ports) == 1:
            to_print += f"{ports.index[0].capitalize()} ports inspected {ports.values[0]:,} mt.\n" \

        if len(types_volumes) == 6:
                to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                            f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                            f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                            f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt), " \
                            f"{types_volumes.index[3].upper()} ({types_volumes.values[3]:,} mt), " \
                            f"{types_volumes.index[4].upper()} ({types_volumes.values[4]:,} mt), " \
                            f"{types_volumes.index[5].upper()} ({types_volumes.values[5]:,} mt).\n"
        elif len(types_volumes) == 5:
            to_print += f"{types_volumes.index[0].capitalize()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                        f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt), " \
                        f"{types_volumes.index[3].upper()} ({types_volumes.values[3]:,} mt), " \
                        f"{types_volumes.index[4].upper()} ({types_volumes.values[4]:,} mt).\n"
        elif len(types_volumes) == 4:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                        f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt), " \
                        f"{types_volumes.index[3].upper()} ({types_volumes.values[3]:,} mt).\n"
        elif len(types_volumes) == 3:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()} ({types_volumes.values[1]:,} mt), " \
                        f"{types_volumes.index[2].upper()} ({types_volumes.values[2]:,} mt).\n"
        elif len(types_volumes) == 2:
            to_print += f"{types_volumes.index[0].upper()} was the most popular {grain_type.lower()} " \
                        f"with {types_volumes.values[0]:,} mt passing inspections, followed by " \
                        f"{types_volumes.index[1].upper()}, with " \
                        f"{types_volumes.values[1]:,} mt weighted.\n "

        if yoy_change > 0:
            to_print += f"Weekly volumes pushed the total inspections since the start " \
                        f"of the 2020/21 marketing year to {round(year_to_date, 2):,} mt, " \
                        f"up {round(yoy_change, 2)}% year-on-year.\n"
        elif yoy_change < 0:
            to_print += f"Weekly volumes pushed the total inspections since the start " \
                        f"of the 2020/21 marketing year to {round(year_to_date, 2):,} mt, " \
                        f"down {round(yoy_change, 2)}% year-on-year.\n"
        elif yoy_change == 0:
            to_print += f"Weekly volumes pushed the total inspections since the start " \
                        f"of the 2020/21 marketing year to {round(year_to_date, 2):,} mt, " \
                        f"unchanged year-on-year.\n"
        return to_print


