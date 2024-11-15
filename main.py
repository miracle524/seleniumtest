from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

# Specify the URL of the PDF
pdf_url = "https://www.idx.co.id/Portals/0/StaticData/NewsAndAnnouncement/ANNOUNCEMENTSTOCK/From_EREP/202405/68857784f8_23e0fe74cb.pdf"

# Set up Chrome options
chrome_options = Options()
# Set the download directory
download_dir = os.path.abspath("downloads")
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True  # This will download PDFs instead of opening them
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the PDF URL
    driver.get(pdf_url)
    # Wait for the download to complete
    time.sleep(5)  # Adjust the sleep time if necessary
finally:
    # Close the browser
    driver.quit()

print(f"PDF has been downloaded to {download_dir}")
