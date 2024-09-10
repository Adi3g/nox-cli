from __future__ import annotations

import click

from nox.domains.data_processing_manager import DataProcessingManager


@click.group()
def data():
    """Data processing commands."""
    pass


@click.command()
@click.option('--input', 'input_file', required=True, help='Path to the input data file')
@click.option('--output', 'output_file', required=True, help='Path to the output data file')
@click.option('--format', 'output_format', required=True, help='Output format (csv, json, excel)')
def convert(input_file, output_file, output_format):
    """Convert data from one format to another."""
    manager = DataProcessingManager()
    result = manager.convert_data(input_file, output_file, output_format)
    click.echo(result)


@click.command()
@click.option('--input', 'input_file', required=True, help='Path to the input data file')
@click.option('--output', 'output_file', required=True, help='Path to the output data file')
@click.option('--column', 'filter_column', required=True, help='Column to filter on')
@click.option('--value', 'filter_value', required=True, help='Value to filter by')
def filter(input_file, output_file, filter_column, filter_value):
    """Filter data based on column value."""
    manager = DataProcessingManager()
    result = manager.filter_data(input_file, output_file, filter_column, filter_value)
    click.echo(result)


@click.command()
@click.option('--input', 'input_file', required=True, help='Path to the input data file')
def summarize(input_file):
    """Summarize data by calculating basic statistics."""
    manager = DataProcessingManager()
    result = manager.summarize_data(input_file)
    click.echo(result)


@click.command()
@click.option('--left', 'left_file', required=True, help='Path to the left data file')
@click.option('--right', 'right_file', required=True, help='Path to the right data file')
@click.option('--on', 'on_column', required=True, help='Column to merge on')
@click.option('--output', 'output_file', required=True, help='Path to the output data file')
def merge(left_file, right_file, on_column, output_file):
    """Merge two data files on a common key."""
    manager = DataProcessingManager()
    result = manager.merge_data(left_file, right_file, on_column, output_file)
    click.echo(result)


@click.command()
@click.option('--input', 'input_file', required=True, help='Path to the input data file')
@click.option('--x', 'x_column', required=True, help='Column for the x-axis')
@click.option('--y', 'y_column', required=True, help='Column for the y-axis')
@click.option('--chart', 'chart_type', required=True, help='Chart type (bar, line, scatter)')
@click.option('--output', 'output_file', required=True, help='Path to the output image file')
def visualize(input_file, x_column, y_column, chart_type, output_file):
    """Generate a simple visualization from data."""
    manager = DataProcessingManager()
    result = manager.visualize_data(input_file, x_column, y_column, chart_type, output_file)
    click.echo(result)


# Add commands to the data group
data.add_command(convert)
data.add_command(filter)
data.add_command(summarize)
data.add_command(merge)
data.add_command(visualize)
