import os
import re
from pyicloud import PyiCloudService

APPLE_ID = 'email@domain.com'
PASSWORD = 'password'

print("Attempting to connect to iCloud...")
api = PyiCloudService(APPLE_ID, PASSWORD)

if api.requires_2fa:
    print("Two-factor authentication required.")
    code = input("Enter the verification code received on your Apple devices: ")
    result = api.validate_2fa_code(code)
    
    if not result:
        print("Incorrect code. Exiting.")
        exit(1)
        
    if not api.is_trusted_session:
        print("Trusting session for future logins...")
        api.trust_session()

elif api.requires_2sa:
    print("Two-step authentication required.")
    print("Devices available to receive SMS:")
    devices = api.trusted_devices
    for i, device in enumerate(devices):
        print(f"  {i}: {device.get('deviceName', 'SMS Device')}")
        
    device_index = int(input("Choose device (number): "))
    device = devices[device_index]
    if not api.send_verification_code(device):
        print("Failed to send verification code.")
        exit(1)
        
    code = input("Enter the received code: ")
    if not api.validate_verification_code(device, code):
        print("Failed to verify code.")
        exit(1)

base_download_dir = 'iCloudPhotos'
if not os.path.exists(base_download_dir):
    os.makedirs(base_download_dir)

try:
    photos = api.photos.all
    total_photos = len(photos)
    print(f"\nSuccess! {total_photos} photos/videos found on your iCloud.\n")
    
    for index, photo in enumerate(photos, start=1):
        progress_prefix = f"[{index}/{total_photos}]"
        
        if hasattr(photo, 'created') and photo.created:
            year = str(photo.created.year)
        else:
            year = "Unknown"
            
        year_dir = os.path.join(base_download_dir, year)
        if not os.path.exists(year_dir):
            os.makedirs(year_dir)
        
        raw_unique_filename = f"{photo.id}_{photo.filename}"
        unique_filename = re.sub(r'[<>:"/\\|?*]', '_', raw_unique_filename)
        file_path = os.path.join(year_dir, unique_filename)
        
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            print(f"{progress_prefix} Downloading to [{year}]: {unique_filename}...")
            download = photo.download()
            
            with open(file_path, 'wb') as opened_file:
                if isinstance(download, bytes):
                    opened_file.write(download)
                else:
                    opened_file.write(download.content)
        else:
            print(f"{progress_prefix} Skipped: {unique_filename} already exists in folder {year}.")
            
    print("\n🎉 Download and sorting completed successfully!")

except Exception as e:
    print(f"\n❌ An error occurred during retrieval: {e}")