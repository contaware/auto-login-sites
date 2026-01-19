# Auto-login to sites

This project uses the [Splinter](https://splinter.readthedocs.io/) Python package to automate internet sites login. As an example we provide code for [freedns.afraid.org](https://freedns.afraid.org), but you can add any other site. Get inspiration from *freedns.py* to make your own script, when done call it from *auto-login-sites.bat*.

The project setup is primarily meant to be used on Windows because it uses an *auto-login-sites.bat* batch file to execute the Python script(s) and to send emails with the bundled `mailsend-go.exe` from <https://github.com/muquit/mailsend-go>.


## Installation

1. Clone this repository to your local computer:

   ```bash
   git clone https://github.com/contaware/auto-login-sites.git
   ```

2. Install dependencies with py-launcher providing your Python version:

   ```bat
   py -3.XY -m pip install python-dotenv
   py -3.XY -m pip install "splinter[selenium]"
   ```
   - Replace `-3.XY` with your Python version.

3. In project root directory create an `.env` file with the following settings:

   ```bash
   # Python version where the dependencies are installed
   USE_PYTHON_VER=3.XY

   # E-Mail credentials
   EMAIL_TO=john@example.com
   EMAIL_FROM=john@example.com
   EMAIL_PORT=587
   EMAIL_SMTP=mail.example.com
   EMAIL_USER=john@example.com
   EMAIL_PW="secret pw"

   # freedns.afraid.org credentials
   FREEDNS_USER=username
   FREEDNS_PW="secret pw"
   ```
   - Use **double-quotes** around the values if they contain **spaces or special characters**.
   - Replace `-3.XY` with your Python version.

4. Setup a Windows Task Scheduler to run *auto-login-sites.bat* daily or weekly. In the Task Scheduler Settings check **"Run whether user is logged on or not"** to hide the batch script window and to hide also the opened browser in case it runs in non-headless mode. **Do not use the SYSTEM account, use your Windows account**, that's because Python is usually installed for a specific user which has user specific packages installed.
