from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


class DataProcessingManager:
    def convert_data(self, input_file: str, output_file: str, output_format: str) -> str:
        """Convert data from one format to another."""
        try:
            # Load the data
            data = pd.read_csv(input_file) if input_file.endswith('.csv') else pd.read_json(input_file)

            # Save data in the desired format
            if output_format == 'csv':
                data.to_csv(output_file, index=False)
            elif output_format == 'json':
                data.to_json(output_file, orient='records', lines=True)
            elif output_format == 'excel':
                data.to_excel(output_file, index=False, engine='openpyxl')
            else:
                return f"Error: Unsupported output format '{output_format}'"

            return f"Data converted to {output_format} and saved to {output_file}"
        except Exception as e:
            return f"Error converting data: {str(e)}"

    def filter_data(self, input_file: str, output_file: str, filter_column: str, filter_value: str) -> str:
        """Filter data based on column value."""
        try:
            data = pd.read_csv(input_file) if input_file.endswith('.csv') else pd.read_json(input_file)
            filtered_data = data[data[filter_column] == filter_value]
            filtered_data.to_csv(output_file, index=False)
            return f"Filtered data saved to {output_file}"
        except Exception as e:
            return f"Error filtering data: {str(e)}"

    def summarize_data(self, input_file: str) -> str:
        """Summarize data by calculating basic statistics."""
        try:
            data = pd.read_csv(input_file) if input_file.endswith('.csv') else pd.read_json(input_file)
            summary = data.describe().to_string()
            return summary
        except Exception as e:
            return f"Error summarizing data: {str(e)}"

    def merge_data(self, left_file: str, right_file: str, on: str, output_file: str) -> str:
        """Merge two data files on a common key."""
        try:
            left_data = pd.read_csv(left_file) if left_file.endswith('.csv') else pd.read_json(left_file)
            right_data = pd.read_csv(right_file) if right_file.endswith('.csv') else pd.read_json(right_file)
            merged_data = pd.merge(left_data, right_data, on=on)
            merged_data.to_csv(output_file, index=False)
            return f"Merged data saved to {output_file}"
        except Exception as e:
            return f"Error merging data: {str(e)}"

    def visualize_data(self, input_file: str, x_column: str, y_column: str, chart_type: str, output_file: str) -> str:
        """Generate a simple visualization from data."""
        try:
            data = pd.read_csv(input_file) if input_file.endswith('.csv') else pd.read_json(input_file)

            plt.figure(figsize=(10, 6))
            if chart_type == 'bar':
                data.plot.bar(x=x_column, y=y_column)
            elif chart_type == 'line':
                data.plot.line(x=x_column, y=y_column)
            elif chart_type == 'scatter':
                data.plot.scatter(x=x_column, y=y_column)
            else:
                return f"Error: Unsupported chart type '{chart_type}'"

            plt.savefig(output_file)
            plt.close()
            return f"Chart saved to {output_file}"
        except Exception as e:
            return f"Error generating visualization: {str(e)}"
