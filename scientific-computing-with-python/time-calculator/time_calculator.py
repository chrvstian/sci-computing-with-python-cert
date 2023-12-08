"""
@name: time_calculator.py
@date: 06/11/2023 (dd/mm/yy)
@author: github.com/chrvstian
"""

# List of days of the week, used for calculating the resulting day if starting_day is provided
DAYS_OF_WEEK: list[str] = [
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
  "Sunday"
]

# Constants for the number of hours in a day and minutes in an hour
HOURS_IN_DAY: int = 24
MINUTES_IN_HOUR: int = 60

def add_time(start_time: str, 
             duration: str, 
             starting_day: str=None
    ) -> str:
    """
    Adds the given duration to the start time and returns the result.

    Args:
    - start_time (str): The starting time in the 12-hour clock format.
    - duration (str): The duration to be added in hours and minutes.
    - starting_day (str): Optional starting day of the week (case insensitive).

    Returns:
    - str: The resulting time, optionally followed by the day of the week and
           days later information.
    """

    # Extracting the start hour, start minute, and period (AM/PM) from the start_time
    start_time, period = start_time.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Adjusting the start hour based on the period (PM adds 12 hours)
    start_hour += 12 if period == "PM" else 0

    # Extracting the duration hour and duration minute from the duration
    duration_hour, duration_minute = map(str, duration.split(':'))

    # Calculating the total minutes from the start time and duration
    total_minutes = (start_hour
        * MINUTES_IN_HOUR 
        + start_minute
        + int(duration_hour)
        * MINUTES_IN_HOUR 
        + int(duration_minute)
    )

    # Calculating the new hour and minute from the total minutes
    new_hour = total_minutes // MINUTES_IN_HOUR % HOURS_IN_DAY
    new_minute = total_minutes % MINUTES_IN_HOUR

    # Determining the new period (AM/PM) and adjusting the new hour format
    new_period = "PM" if new_hour >= 12 else "AM"
    new_hour = new_hour % 12 if new_hour % 12 != 0 else 12

    # Calculating the number of days later
    days_later = total_minutes // (HOURS_IN_DAY * MINUTES_IN_HOUR)

    # If starting_day is provided, calculating the resulting day of the week
    if starting_day:
      starting_day = starting_day.capitalize()
      starting_day_index = DAYS_OF_WEEK.index(starting_day)
      new_day_index = (starting_day_index + days_later) % len(DAYS_OF_WEEK)
      new_day = DAYS_OF_WEEK[new_day_index]
      day_output = f", {new_day}"
    else:
        day_output = ""

    # Constructing the result string with the new time, period, and optional day information
    result = f"{new_hour}:{new_minute:02d} {new_period}{day_output}"

    # Appending days later information to the result if applicable
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result
