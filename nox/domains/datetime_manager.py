from __future__ import annotations

from datetime import datetime
from datetime import timedelta

import pytz as pytz
from dateutil import parser


class DateTimeManager:
    def get_current_time(self, timezone: str = 'UTC') -> str:
        """Get the current time in the specified time zone."""
        try:
            tz = pytz.timezone(timezone)
            current_time = datetime.now(tz)
            return current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        except pytz.UnknownTimeZoneError:
            return f"Error: Unknown time zone '{timezone}'"

    def convert_time(self, time_str: str, from_timezone: str, to_timezone: str) -> str:
        """Convert time from one time zone to another."""
        try:
            from_tz = pytz.timezone(from_timezone)
            to_tz = pytz.timezone(to_timezone)
            time = parser.parse(time_str)
            from_time = from_tz.localize(time)
            converted_time = from_time.astimezone(to_tz)
            return converted_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        except (pytz.UnknownTimeZoneError, ValueError) as e:
            return f"Error: {str(e)}"

    def add_to_date(self, date_str: str, days: int = 0, weeks: int = 0, months: int = 0) -> str:
        """Add days, weeks, or months to a given date."""
        try:
            date = parser.parse(date_str)
            # Adding days and weeks
            date += timedelta(days=days, weeks=weeks)
            # For simplicity, add months as 30 days each
            date += timedelta(days=months * 30)
            return date.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError as e:
            return f"Error: {str(e)}"

    def date_difference(self, start_date: str, end_date: str) -> str:
        """Calculate the difference between two dates."""
        try:
            start = parser.parse(start_date)
            end = parser.parse(end_date)
            difference = end - start
            return f"Difference: {difference.days} days, \
                {difference.seconds // 3600} hours, {(difference.seconds // 60) % 60} minutes"
        except ValueError as e:
            return f"Error: {str(e)}"
