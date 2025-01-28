# quiz-locator
A python program that creates calendar events for all quizzes and exams for the week at the University of Waterloo.

UWaterloo has a website, Odyssey, that they use to keep track of the different quizzes and exams seated by students.
This website only shows the location and seat number for your quiz a week before the quiz.
The purpose of this program is to automate retrieving the seat and location of the quiz and put them onto your personal calendar.

This program gets all the information for a quiz and exam (room number, location, time, etc)
and produces a set of calendars that you can open.

A few notes:
- This program can only read html files at the moment
- You have to manually open every event to add them to the calendar
- There is not auto updating system which can be used to update the quiz location.

I plan to fix these limitations, but for now it can still generate event files from the html table given
