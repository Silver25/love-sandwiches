# In order to use our Google Sheets API, we're going to need to import
# two additional dependencies into our project:
# imports the entire gspread library, to access any function, class or method
import gspread   
# imports the Credentials class, 
# which is part of the service_account function
from google.oauth2.service_account import Credentials

# Every Google account has an IAM configuration.
# This configuration specifies what the user has access to.
# The SCOPE is constant and lists the APIs 
# that the program should access in order to run.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# sheet variable defined with constants 
# [we need these settings to access our spreadsheet data]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# access our  love_sandwiches sheet, 
# using the open() method on our client object
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    # Python function description goes  between triple double quotes
    """
    Get sales figures input from the user.
    """
    # program to repeat its request for data right away
    # without restarting the program in case of error (while loop)
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        
        # split() method on our data  string, to break it up at the commas
        # this will remove the commas from the string
        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        # for each individual value in the values list, 
        # convert that value into an integer
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


data = get_sales_data()