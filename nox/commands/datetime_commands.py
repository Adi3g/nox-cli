from __future__ import annotations

import click

from nox.domains.datetime_manager import DateTimeManager


@click.group()
def datetime():
    """Date and time management commands."""
    pass


@click.command()
@click.option(
    '--timezone', default='UTC',
    help='Time zone to display the current time (default: UTC)',
)
def now(timezone):
    """Get the current time in the specified time zone."""
    manager = DateTimeManager()
    result = manager.get_current_time(timezone)
    click.echo(result)


@click.command()
@click.option(
    '--time', 'time_str', required=True,
    help='Time to convert (e.g., "2024-09-10 12:00:00")',
)
@click.option('--from-tz', 'from_timezone', required=True, help='Time zone of the input time')
@click.option('--to-tz', 'to_timezone', required=True, help='Time zone to convert the time to')
def convert(time_str, from_timezone, to_timezone):
    """Convert time from one time zone to another."""
    manager = DateTimeManager()
    result = manager.convert_time(time_str, from_timezone, to_timezone)
    click.echo(result)


@click.command()
@click.option('--date', 'date_str', required=True, help='Starting date (e.g., "2024-09-10")')
@click.option('--days', default=0, help='Days to add')
@click.option('--weeks', default=0, help='Weeks to add')
@click.option('--months', default=0, help='Months to add (approximated as 30 days each)')
def add(date_str, days, weeks, months):
    """Add days, weeks, or months to a given date."""
    manager = DateTimeManager()
    result = manager.add_to_date(date_str, days, weeks, months)
    click.echo(result)


@click.command()
@click.option('--start', 'start_date', required=True, help='Start date (e.g., "2024-09-10")')
@click.option('--end', 'end_date', required=True, help='End date (e.g., "2024-09-15")')
def difference(start_date, end_date):
    """Calculate the difference between two dates."""
    manager = DateTimeManager()
    result = manager.date_difference(start_date, end_date)
    click.echo(result)


# Add commands to the datetime group
datetime.add_command(now)
datetime.add_command(convert)
datetime.add_command(add)
datetime.add_command(difference)
