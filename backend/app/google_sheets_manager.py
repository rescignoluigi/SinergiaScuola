from googleapiclient.discovery import build
from google.auth import default

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_sheets_service():
    creds, _ = default(scopes=SCOPES)
    return build("sheets", "v4", credentials=creds)

def create_sheet(title: str):
    service = get_sheets_service()

    spreadsheet = {
        "properties": {"title": title}
    }

    sheet = service.spreadsheets().create(
        body=spreadsheet,
        fields="spreadsheetId"
    ).execute()

    return sheet["spreadsheetId"]

def write_data(spreadsheet_id: str, range_name: str, values: list):
    service = get_sheets_service()

    body = {"values": values}

    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body
    ).execute()

    return result
