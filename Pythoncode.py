import csv
import os


# Define a function to process each athlete's CSV file and generate HTML
def generate_athlete_html(csv_filename):
    output_file = csv_filename.replace('.csv', '.html')  # Output HTML file name based on the CSV file name

    # Initialize athlete details and rows for the table
    athlete_name = ""
    athlete_rows = ""

    # Open and read the CSV file
    with open(csv_filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

        # Loop through the athlete's data, skipping the header row
        for row in data[5:]:
            # Ensure the row has at least 8 columns (based on the number of expected fields)
            if len(row) < 8:
                continue  # Skip rows that don't have enough data

            name = row[0]
            overall_place = row[1]
            grade = row[2]
            time = row[3]
            date = row[4]
            meet = row[5]
            comments = row[6]
            photo = row[7]

            if not photo:
                photo = "default_image.jpg"

            # Path to the image
            image_path = f"images/AthleteImages/{photo}"

            # Check if the image file exists, otherwise use a default placeholder
            if not os.path.exists(image_path):
                image_path = "images/AthleteImages/default_image.jpg"

            # Capture the athlete's name from the first row
            if athlete_name == "":
                athlete_name = data[5][0]

            # Create a row for the athlete's performance
            athlete_row = f"""
            <tr>
                <td>{overall_place}</td>
                <td>{grade}</td>
                <td>{time}</td>
                <td>{date}</td>
                <td>{meet}</td>
                <td>{comments}</td>
                <td><img src="{image_path}" alt="{name}'s photo" width="100"></td>
            </tr>
            """
            athlete_rows += athlete_row

    # HTML template for the athlete's performance
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{athlete_name}'s Performance History</title>
    </head>
    <body>
        <header>
            <h1>{athlete_name}'s Performance History</h1>
        </header>

        <div class="athlete-results">
            <h2>Performances of {athlete_name}</h2>
            <table border="1" cellpadding="5" cellspacing="0">
                <thead>
                    <tr>
                        <th>Overall Place</th>
                        <th>Grade</th>
                        <th>Time</th>
                        <th>Date</th>
                        <th>Meet</th>
                        <th>Comments</th>
                        <th>Photo</th>
                    </tr>
                </thead>
                <tbody>
                    {athlete_rows}
                </tbody>
            </table>
        </div>

        <footer>
            <p>&copy; 2024 {athlete_name}'s Performance History. All Rights Reserved.</p>
        </footer>
    </body>
    </html>
    '''

    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        file.write(html_content)

    print(f"Generated {output_file} for athlete: {athlete_name}")


# Example of processing multiple CSV files (one for each athlete)
csv_files = [
    "Alex Nemecek18820260.csv",  # Example CSV file for athlete Alex Nemecek
    "Amir Abston25395576.csv"    # Add more CSV file names as needed
]

# Generate HTML for each CSV file
for csv_file in csv_files:
    generate_athlete_html(csv_file)
