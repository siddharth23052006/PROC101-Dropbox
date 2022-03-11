from dropbox.files import WriteMode
from os import access
import dropbox
import os

class TransferData:
  def __init__(self, access_token):
    self.access_token = access_token

  def upload_file(self, file_from, file_to):
    dbx = dropbox.Dropbox(self.access_token)

    for root, dirs, files in os.walk(file_from):
      for filename in files:
        #construct the full local path
        local_path = os.path.join(root, filename)

        #construct the full Dropbox path
        relative_path = os.path.relpath(local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)

        #upload the file
        with open(file_from,'rb') as f:
          dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
  access_token = 'sl.BDky2KKDcWz8NrF8b7uNa3a2KIdWYFq8JKUptoKlQFLt0eZBl6Y29zBNKR3vrSbJLVBIV0Od9wVFiI9GtStAnrfh2YVVqHk7Y5za4Pz_9Fbu1Lu5NNVmgb74qiHt6d2ZBRGKRXw'
  transferData = TransferData(access_token)

  file_from = input("Enter the path of the file you want to transfer: ")
  file_to = input("Enter the full path to send to dropbox: ") #This is the full path to upload the file to

  transferData.upload_file(file_from, file_to)
  print("File has been moved.")

main()