import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_folders(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(fileFrom):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, fileFrom)
                dropbox_path = os.path.join(fileTo,relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'v70aQmSiGoMAAAAAAAAAAXC0HiLnsBtWLvYN5rmklqEhDoZuVxuy-pwfv66uyE_V'
    transferData = TransferData(access_token)

    fileFrom = str(input("Enter the folder path to transfer : -"))
    fileTo = input("enter the full path to upload to dropbox:- ")

    transferData.upload_folders(fileFrom,fileTo)
    print("folder has been moved !!!")

main()