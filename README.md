Workout Tracker and Analyzer
Overview:
This Python project is designed to enhance personal fitness tracking by automating the process of analyzing and logging workout details. It utilizes the Nutritionix API for analyzing natural language descriptions of exercises and the Sheety API for storing this data efficiently in a spreadsheet format.

Features:
Natural Language Processing: Analyzes workout descriptions inputted by the user using the Nutritionix API.
Personalized Analysis: Adjusts calculations for calories burned based on user-specific details like gender, weight, height, and age.
Data Storage: Logs each workout session in a spreadsheet via the Sheety API, including date, time, exercise name, duration, and calories burned.
Error Handling: Ensures robustness in API communication and response validation.

How It Works;
User Input: The script prompts the user to enter their workout details.
Data Processing: Sends this data to the Nutritionix API for analysis.
Logging Data: Formats the received data and logs it into a spreadsheet using the Sheety API.
Response Output: Displays the responses from both APIs for user confirmation.

Prerequisites:
Python 3.x
requests library
Nutritionix API credentials (APP_ID, API_KEY)
Sheety API credentials
