import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

# Set the name of your Google Sheets spreadsheet
spreadsheet_name = "Jobs"

# Set the name of the worksheet and the column where you want to add the date
worksheet_name = "2024"
column1= "A"  # Change this to your desired column
column2= "B"
json_filename = "in.json"

def authenticate_gspread():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("/mnt/c/Users/jacob/Downloads/tensile-axon-405704-53761fe143ca.json", scope)
    gc = gspread.authorize(credentials)
    return gc

def scrape_linkedin_saved_jobs(values_list):
    with open(json_filename,'r') as json_file:
        job_data = json.load(json_file)
    json_file.close()
    
    for job in job_data:
        now = datetime.now()
        relative_time=job["date"]
        #print(relative_time)
        timestamp=""
        if 'h ago' in relative_time and relative_time[0:11]!='Application':
            print("gere")
            hours_ago = int(relative_time.split('h')[0].split()[-1])
            timestamp = now - timedelta(hours=hours_ago)
            #print(timestamp)
            # tss=datetime.strptime(str(timestamp),"%Y-%m-%d %H:%M:%S.%f")
        
            if timestamp.date() == now.date():
                # ts=tss.strftime("%H:%M:%S")    
                #print(ts)
                date_str = timestamp.strftime("%m/%d/%Y")
                values=[date_str,job["company"],job["title"],job["location"],job["link"]]
                values_list.append((values))
        if 'm ago' in relative_time and relative_time[0:11]!='Application': 
            
            minutes_ago = int(relative_time.split('m')[0].split()[-1])
            timestamp = now - timedelta(minutes=minutes_ago)
            date_str = timestamp.strftime("%m/%d/%Y")
            values=[date_str,job["company"],job["title"],job["location"],job["link"]]
            values_list.append((values))
        else:
            continue


        
            
        
        

    
    
    return values_list

def add_date_to_sheet(gc,values_list):
    spreadsheet = gc.open(spreadsheet_name)
    worksheet = spreadsheet.worksheet(worksheet_name)
   
    # Get today's date in the format YYYY-MM-DD
    

    # Find the last row in the specified column
    last_row = len(worksheet.col_values(ord(column1) - ord('A') + 1)) + 1
     
    #  start = "A" + str(last_row)
    #  end = "A" + str(last_row+12)
    

    start_col=1
    start_row=last_row
    num_rows = len(values_list)
 
    num_cols = len(values_list[0]) if values_list else 0
    print(num_cols)
    print(chr(65 + start_col + num_cols - 2))
    cell_range = f"{chr(65 + start_col - 1)}{start_row}:{chr(65 + start_col + num_cols - 2)}{start_row + num_rows - 1}"
   
    cell_list=worksheet.range(cell_range)

    for cell, value in zip(cell_list, [item for sublist in values_list for item in sublist]):
        cell.value = value

    # for cell in cell_list:
    #     cell.value = [f'{today_date}',1,1]
    # values=[[today_date,"comp_name","link"]]
    # Update the cell with today's date
    worksheet.update_cells(cell_list)


def main():
    gc = authenticate_gspread()
    today_date = datetime.now().strftime("%m/%d/%Y")
    #populate values_list with scrape f(x)
   
   
    values_list=[]
    scrape_linkedin_saved_jobs(values_list)
    #print(len(values_list[0]))
    print((values_list))
    add_date_to_sheet(gc,values_list)

    

if __name__ == "__main__":
    main()
