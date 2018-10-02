import requests as req
import json
import pprint as pretty
import openpyxl as opxl
from datetime import datetime as dt

key = "7af48c8988b13c4580a58cb9ba0158c0"
url = "https://api.monday.com:443"

board_id = "120457797"

all_users = "/v1/users.json"
updates = "/v1/updates.json"
order_setup = "/v1/boards/120457797/pulses.json?per_page=25"



def get(query):
    """Use requests.get to return api call"""
    call = url + query + "&api_key=" + key
    result = req.get(call)
    print("Trying to return {}".format(call))
    return result

response = get(order_setup)

data = json.loads(response.content)

pid = []
name = []
created_date = []

for d in data:
    pid.append(d['pulse']['id'])
    name.append(d['pulse']['name'])
    created_date.append(d['pulse']['created_at'].split("T")[0])


# Write to Excel
wb = opxl.Workbook()
ws = wb.active

pyOut = "Test.xlsx"

colHeaders = ["PID", "PO Name", "Created Date"]

for col in range(0, len(colHeaders)):
    ws.cell(column=col+1, row=1, value=colHeaders[col])

try:
    for row in range(2, len(pid)+2): # add data from lists (start at 2 because excel is unity indexed and a header exists already)
        ws.cell(column=1, row=row, value=pid[row-2])
        ws.cell(column=2, row=row, value=name[row-2])
        ws.cell(column=3, row=row, value=created_date[row-2])

except IndexError:
    pass

wb.save(filename = pyOut)                       

##pulseId = []
##pulseName = []
##
##for d in data:
##    
##    pulseId.append(d["pulse"]["id"])
##    pulseName.append(d["pulse"]["name"])
##
##print(pulseId)
##print(pulseName)
    
