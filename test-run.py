# In order to use our Google Sheets API, we're going to need to import
# two additional dependencies into our project:
import gspread   # imports the entire gspread library, to access any function,  class or method
# imports the Credentials class, which is part of the service_account  function
from google.oauth2.service_account import Credentials

# Every Google account has an IAM configuration.
# This configuration specifies what the user has access to.
# The SCOPE is constant and lists the APIs that the  program should access in order to run.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# sheet variable defined with constants [we need these settings to access our spreadsheet data]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# access our  love_sandwiches sheet, using the open() method on our client object
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# using the worksheet method of the sheet, we can call our “sales” worksheet to test setup of code
sales = SHEET.worksheet('sales')
data = sales.get_all_values()
print(data)