import gspread
import config
from oauth2client.service_account import ServiceAccountCredentials

def handler(event, context):
  try:
    add_rsvp(event)
    return True

  except Exception as err:
    return "ERROR: " + str(err)

def add_rsvp(rsvp):
  # authorize
  scope = ['https://spreadsheets.google.com/feeds']
  c = ServiceAccountCredentials.from_json_keyfile_name(config.keys, scope)
  gc = gspread.authorize(c)

  # get sheet
  wks = gc.open(rsvp['title']).worksheet(rsvp['sheet'])

  # Get all values from first column, and find first blank row
  col_1 = wks.col_values(1)
  first_blank = min([i for i in range(len(col_1)) if col_1[i] == '']) + 1

  # Get col names
  names = wks.row_values(1)
  # Remove blanks
  names = [x for x in names if x]

  # Add to google sheet
  for i in range(len(names)):
    wks.update_cell(first_blank, i+1, rsvp[names[i]])
