import dropbox
from datetime import date

dbx = dropbox.Dropbox('api-key')
day = date.today().strftime("%d")

folder = '/Data'

#download files to a zip file
dbx.files_download_zip_to_file('./backup' + day + '.zip', folder)




