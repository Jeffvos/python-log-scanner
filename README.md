# python-log-scanner
Simple log file scanner in python
This script scans all files in the specified folder with the given search string. 
After which, if the scanner finds the string in one or multiple files, it will output the result into a CSV file.

How to use the scanner:
---

Place all log files in a single folder.

Create a folder with the name CSV and create a empty csv file in it (csvfile.csv)
Scan.py dir > csv > csvfile.csv

Run the script.

---
The output to the csv file can be changed by modifying the writeCSV function.
