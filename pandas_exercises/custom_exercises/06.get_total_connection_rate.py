import pandas as pd

file = 'C://users//ertan//Downloads//data_calls.xlsx'

try:
    # Read the Excel file
    df = pd.read_excel(file)

    # Summarize offered and handled calls by country
    total_offered_calls_by_country = df.groupby('Country')['Offered'].sum()
    total_handled_calls_by_country = df.groupby('Country')['Handled'].sum()

    # Calculate total connection rate
    calculate_total_connection_rate = (total_handled_calls_by_country / total_offered_calls_by_country) * 100

    # Create a summary DataFrame
    summary_df = pd.DataFrame({
        'Total Offered': total_offered_calls_by_country,
        'Total Handled': total_handled_calls_by_country,
        'Total Connection Rate (%)': round(calculate_total_connection_rate, 2)
    }).reset_index()

    # Sort the summary DF by Total Connection Rate
    sorted_summary_df = summary_df.sort_values(by='Total Connection Rate (%)', ascending=False)

    # Write the sorted data to a new Excel file
    output_file = 'C://users//ertan//Downloads//sorted_total_connection_rate.xlsx'
    sorted_summary_df.to_excel(output_file, index=False)  # Save to Excel without the index

    print("File has been created successfully at:", output_file)

except FileNotFoundError as e:
    print(f"Error: The file was not found. Please check the path: {file}")
except Exception as e:
    print(f"An error occurred: {e}")

