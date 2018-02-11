import dappy as dp

# Define the output excel filename
outfile_name = 'My_Report.xlsx'

# Define the desired excel sheet names and the excel queries
file_tab = {'Phone Call Segment CV Recent': 'Call_Volume.sql',
            'Phone Call Segment CV NR': 'Call_Volume2.sql'
            }

# Run the sql queries and export to an excel sheet (fully qualified path stored in outfilepath
outfilepath = dp.multi_excel_from_sql(file_tab, outfile_name,append_date = True)

# Define all of the strings to be used for the email
mailto = 'Zachary.Brown2@capitalone.com'
subject = "My Report"
body = "Hi all, \n \
Here is the latest report. \n \
Let me know if there are any questions. \n\
Thanks! \n\
Zak \
"
mailfrom = "Zachary.Brown2@capitalone.com"

# Email the report
dp.email(mailto,subject,outfilepath,body,mailfrom)


