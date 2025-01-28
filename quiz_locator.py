import pandas as pd
from ics import Calendar, Event
import re
from datetime import timedelta

# this program creates a calender event for all quizzes/exams that have a location and seat number already

table_MN = pd.read_html("/Users/samshin/Documents/Projects/quiz_locator/quiz-locator/test.html")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = table_MN[0]
quizzes = df[["Exam", "When", "Room"]].head(len(df))

# make_event takes a name, start time, and duration (set to 30 minutes default) and creates a .ics file
def make_event(event_name, event_start, room):
    c = Calendar()
    e = Event()
    e.name = event_name
    e.begin = event_start
    e.duration = timedelta(minutes=30)
    e.location = room
    c.events.add(e)
    with open(f"{event_name}.ics", "w") as my_file:
        my_file.writelines(c.serialize_iter())

def main():
    count = 0
    while count < len(quizzes):
        row = quizzes.loc[count]
        if type(row["When"]) == float or type(row["Room"]) == float:
            break
        time = re.findall("....-..-.. ..:..", str(row["When"]))[0] + ":00-05:00"
        make_event(row["Exam"], time, row["Room"])
        count += 1

main()