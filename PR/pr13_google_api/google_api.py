"""See mida tester tahab."""
from __future__ import print_function

import os.path
import pickle

import googleapiclient
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SAMPLE_RANGE_NAME = 'A1:E10'


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """See mida tester tahab."""
    creds = None
    res_list = []

    if os.path.exists(token):
        with open(token, 'rb') as tkn:
            creds = pickle.load(tkn)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token, 'wb') as tkn:
            pickle.dump(creds, tkn)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            res_list.append(row[0])

    return res_list


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """See mida tester tahab."""
    res_list = []
    res_link = link.split("playlist?list=")[1]

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key)

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=res_link,
        maxResults=50
    )
    response = request.execute()

    for i in response["items"]:
        video_id = i["snippet"]["resourceId"]["videoId"]
        formatted_vid = "https://www.youtube.com/watch?v=" + video_id
        res_list.append(formatted_vid)

    return res_list
