from __future__ import annotations

from unittest.mock import patch

import pytest

from nox.domains.datetime_manager import DateTimeManager


@pytest.fixture
def datetime_manager():
    """Fixture to create a DateTimeManager instance."""
    return DateTimeManager()


def test_get_current_time_default(datetime_manager):
    """Test getting the current time in the default timezone (UTC)."""
    with patch('nox.domains.datetime_manager.datetime') as mock_datetime:
        mock_datetime.now.return_value = mock_datetime
        mock_datetime.strftime.return_value = '2024-09-10 12:00:00 UTC+0000'
        result = datetime_manager.get_current_time()
        assert result == '2024-09-10 12:00:00 UTC+0000', 'Unexpected current time format.'


def test_get_current_time_invalid_timezone(datetime_manager):
    """Test getting the current time with an invalid timezone."""
    result = datetime_manager.get_current_time(timezone='Invalid/Timezone')
    assert 'Error: Unknown time zone' in result, 'Expected error message for invalid timezone.'


def test_convert_time(datetime_manager):
    """Test converting time from one timezone to another."""
    time_str = '2024-09-10 12:00:00'
    with patch('nox.domains.datetime_manager.datetime') as mock_datetime:
        mock_datetime.now.return_value = mock_datetime
        mock_datetime.astimezone.return_value = mock_datetime
        mock_datetime.strftime.return_value = '2024-09-10 05:00:00 PDT-0700'
        result = datetime_manager.convert_time(time_str, 'UTC', 'America/Los_Angeles')
        assert result == '2024-09-10 05:00:00 PDT-0700', 'Unexpected converted time format.'


def test_convert_time_invalid_input(datetime_manager):
    """Test converting time with invalid time input."""
    result = datetime_manager.convert_time('Invalid time', 'UTC', 'America/Los_Angeles')
    assert 'Error' in result, 'Expected error message for invalid time input.'


def test_add_to_date_days(datetime_manager):
    """Test adding days to a date."""
    result = datetime_manager.add_to_date('2024-09-10', days=5)
    assert result == '2024-09-15 00:00:00', 'Unexpected date after adding days.'


def test_add_to_date_weeks(datetime_manager):
    """Test adding weeks to a date."""
    result = datetime_manager.add_to_date('2024-09-10', weeks=1)
    assert result == '2024-09-17 00:00:00', 'Unexpected date after adding weeks.'


def test_add_to_date_months(datetime_manager):
    """Test adding months to a date."""
    result = datetime_manager.add_to_date('2024-09-10', months=1)
    assert result == '2024-10-10 00:00:00', 'Unexpected date after adding months.'


def test_date_difference(datetime_manager):
    """Test calculating the difference between two dates."""
    result = datetime_manager.date_difference('2024-09-10', '2024-09-15')
    assert result == 'Difference: 5 days, 0 hours, 0 minutes', 'Unexpected date difference.'


def test_date_difference_invalid_input(datetime_manager):
    """Test calculating the difference with invalid date input."""
    result = datetime_manager.date_difference('Invalid date', '2024-09-15')
    assert 'Error' in result, 'Expected error message for invalid date input.'
