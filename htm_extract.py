import os
from bs4 import BeautifulSoup

# Specify the directory containing the HTML files
directory_path = '/path/to/your/html/files'

# Create an empty list to store extracted data
setup_data_list = []

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".html"):
        # Read the HTML content
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r') as file:
            html_content = file.read()

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract specific information based on HTML structure
        track_info = soup.find('h2').text
        left_front_pressure = soup.find('h2', text='LEFT FRONT:').find_next('u').text
        # Add more extraction logic for other parameters...

        # Store extracted data in a dictionary
        setup_data = {
            'filename': filename,
            'track_info': track_info,
            'left_front_pressure': left_front_pressure,
            # Add more parameters...
        }

        # Append the dictionary to the list
        setup_data_list.append(setup_data)

# Now you have a list of dictionaries containing setup data for each file
# You can save this data to a CSV, JSON, or any other structured format

# For example, saving to a CSV file
import csv

csv_filename = 'setup_data.csv'
csv_fieldnames = ['filename', 'track_info', 'left_front_pressure']  # Add more fieldnames...
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_fieldnames)
    
    # Write header
    writer.writeheader()
    
    # Write data
    writer.writerows(setup_data_list)

