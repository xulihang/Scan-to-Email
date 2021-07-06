import datetime
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError


class dropbox_helper:

    def __init__(self):
        self.dbx = dropbox.Dropbox("sl.A0Emzcsz404L6iMHaj2oLKyLCIjptl9tV1zjdVYZ6Nw4Kp83ALbEHbaRRpR4J1yDj_8JatXcvGhO30MLqovS-6010z_pDv7GiB_q7sF2192mjCRE7Mh3i8LgCGeIsM0FrxOBMvHl")

    def upload(self,filebytes,filepath):
        try:
            self.dbx.files_upload(filebytes, filepath, mode=WriteMode('overwrite'))
            return True
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            return False
            
    def create_sharing_link(self,filepath):
        try:
            #expires = datetime.datetime.now() + datetime.timedelta(days=30)
            #settings = dropbox.sharing.SharedLinkSettings(require_password=True,link_password="123456",expires=expires)
            #shared_link_metadata = dbx.sharing_create_shared_link_with_settings(filepath, settings=desired_shared_link_settings)
            shared_link_metadata = self.dbx.sharing_create_shared_link(filepath)
            return shared_link_metadata.url
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            return None
        

if __name__ == '__main__':
    helper=dropbox_helper()
    if helper.upload(open('email_utils.py', 'rb').read(),'/email_utils.py'):
        print(helper.create_sharing_link('/email_utils.py'))
        
        
        