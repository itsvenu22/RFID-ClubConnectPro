# RFID-ClubConnectPro 🚀

RFID-ClubConnectPro is an exciting and versatile solution designed to supercharge attendance tracking for clubs and organizations. This system harnesses the power of RFID (Radio-Frequency Identification) technology to elegantly record attendance, empowering clubs to concentrate on their core activities while effortlessly managing attendance records. Additionally, the system goes the extra mile by tapping into email and SMS services to foster seamless communication with participants, making it a comprehensive attendance management powerhouse!

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/venukanthan_bs)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/venukanthan)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/itsvenu22)

## Features and Installation🌟
| Feature                       | Description                                                                                         |
|-------------------------------|-----------------------------------------------------------------------------------------------------|
| RFID-based Attendance         | Simplify attendance recording by letting participants tap their RFID cards—say goodbye to tedious manual check-ins! |
| Email and SMS Notifications   | Automatically dispatch messages to participants or club members upon RFID card tap. Keep everyone in the loop about upcoming events, announcements, or anything important. |
| Local and Cloud Storage       | Store attendance records locally and in the cloud, creating a robust safety net for your data. Even in the face of local system hiccups, your records remain safe and sound. |
| Automated Backup              | After each attendance session, a local backup of the attendance records is sent straight to the admin's email. Double data protection, just like that! |

## Getting Started 🚀

## Requirements
To recreate this project you need the following hardware components:
- RaspberryPi
- RC522 RFID Card Reader Module 13.56MHz
- 0.96 inch display or any I²C display
- Breadboard
- Push button
- Jumper wires

To embark on your RFID-ClubConnect journey, follow these simple steps:
<details>
  <summary><strong>Configure Raspberry Pi for RFID</strong></summary>
  
---
    
  **Important:** Check SPI interface:
  
  1. Run `sudo raspi-config`.
  2. Choose `Interfacing Options` > `SPI` (P4).
  3. Confirm enabling SPI.
  4. Wait for enabling.
  5. Restart: `sudo reboot`.
  
  Check SPI: `lsmod | grep spi`.
  - If `spi_bcm2835` is present, move on.
  - If not, follow:
  
  Edit config: `sudo nano /boot/config.txt`.
  - Remove "#" from `dtparam=spi=on` or add it.
  - If absent, add `dtparam=spi=on`.
  
  Save (Ctrl + O), exit (Ctrl + X).
  Reboot: `sudo reboot`.
  
  This ensures the SPI interface is properly enabled on your Raspberry Pi.

---
  
</details>

1. **Installation**: Clone this repository to your local machine. 🖥️
<br>Here, I'm using
<br>[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.linux.org/)

```bash
# Update the system
sudo apt update
sudo apt upgrade

# Install Python
sudo apt install python3

# Install Pip (Python Package Manager)
sudo apt install python3-pip

# Install Required Libraries
pip3 install RPi.GPIO twilio mfrc522

# Hardware Setup
# If the code interfaces with hardware, ensure proper connections

# Custom Modules
# If the code relies on custom modules, ensure they're available and configured

# Run the Script with all pins connected
# Clone the repo with
git clone https://github.com/itsvenu22/RFID-ClubConnectPro

# Use a text editor or the terminal to create the file
nano rfid-data.py

# Paste the code into the file, save, and then run the script
python3 rfid-data.py

```
    

3. **Configuration**: Customize the configuration files to set up email and SMS services. Don't forget to provide those essential API keys, email addresses, and other settings.

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your_email@example.com)
[![Twilio](https://img.shields.io/badge/Twilio-F22F46?style=for-the-badge&logo=Twilio&logoColor=white)](https://www.twilio.com/)

4. **Database Setup**: Configure the local and cloud database connections to ensure your attendance records stay snug and secure.

[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Airtable](https://img.shields.io/badge/Airtable-18BFFF?style=for-the-badge&logo=Airtable&logoColor=white)](https://www.airtable.com/)
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Microsoft Azure](https://img.shields.io/badge/microsoft%20azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)



5. **RFID Integration**: Get that RFID hardware connected! Make sure the RFID reader is speaking the same language as your software. 📡

6. **Usage**: Fire up the system and test it with a few sample RFID cards. Ensure attendance records are being captured with pinpoint accuracy and that those email/SMS notifications are rocking as expected! 💥
   


<h3 align="left">If you have any questions or want to connect with me, feel free to reach out:</h3>

[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/venukanthan_bs)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/venukanthan)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/itsvenu22)

  
[![Thank You](https://img.shields.io/badge/Thank_You-For_Visiting_My_Repository!-brightgreen?style=for-the-badge&logo=heart)](https://github.com/itsvenu22)
## License 📜

This project proudly embraces the [MIT License](LICENSE). Feel free to use, modify, and spread the RFID-ClubConnect magic following the terms of the license.

Let's revolutionize attendance tracking, one tap at a time!


