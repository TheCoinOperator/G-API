rom __future__ import print_function


from datetime import date
from googleapiclient.http import MediaIoBaseDownload
import io
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import glob
import os
import shutil
from scipy.io.wavfile import read
import paramiko


def google()
    today = (date.today())
    todays = str(today)
    



    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/drive']




    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        
            service = build('drive', 'v3', credentials=creds)
            results = service.files().list(
            pageSize=1000, fields="nextPageToken, files(name,id)",
                                q = "'emailaddress' in writers and modifiedTime > '"+todays+"' and (mimeType contains 'audio/') ").execute()
            items = results.get('files', [])
            for item in items:
                
                
                
                test = [item['id']]
            
                
                test2 = [item ['name']]

                #print(test)

                test3 = str(test)
                #print (test3)

                test4 = (test3[2:-2])
                print (test4)

                test5 = (str(test2))

                test6 = (test5[2:-2])
                print (test5)

                file_id = test4
                filename=test6
                request = service.files().get_media(fileId=file_id)
                fh = io.FileIO(filename, 'wb')
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print ("Download %d%%." % int(status.progress() * 100))
                    
    except HttpError as error:
            # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


def move():

    today = (date.today())
    todays = str(today)
    
    if not os.path.exists(todays):
        os.makedirs(todays)
    source_dir = 'insert/file/path/here'
    target_dir = '/insert/filepath/here/'+todays+'/'
    
    
        # move file whose name starts with string 'emp'
    pattern = source_dir + "*WAV"
    for file in glob.iglob(pattern, recursive=True):
    # extract file name form file path
        file_name = os.path.basename(file)
        shutil.move(file_name, target_dir + file_name)
        print('Moved:', file)

def sftp():
    today = (date.today())
    todays = str(today)
    
    # 1 - Open a transport
    host="insert server here"
    port = insert port here
    transport = paramiko.Transport((host, port))

    
    # 2 - Auth
    password="insert password"
    username="insert username"
    transport.connect(username = username, password = password)
    
    # 3 - Go!
    
    sftp = paramiko.SFTPClient.from_transport(transport)
    

    try:
        sftp.chdir ('insert/file/path/'+todays)  # Test if remote_path exists
        
    except IOError:
        sftp.mkdir("/insert/file/path/"+todays)  # Create remote_path
        sftp.chdir("/insert/file/path/"+todays)
        
       
    # 4 - Specify your source and target folders.
    source_folder="/home/sophie/python/gapi2/"+todays
    outbound_files=os.listdir(source_folder)
    
    # 5 - Download all files from that path
    for file in outbound_files :
        filepath = "/insert/file/path/here/"+todays+"/"+file
        
        remotepath = "/insert/file/path/here/"+todays+"/"+file
        
        
        sftp.put(filepath, remotepath)
        



def rem():
    today = (date.today())
    todays = str(today)
    shutil.rmtree('/insert/file/path/here/'+todays)

google()
move()
sftp()
rem()




