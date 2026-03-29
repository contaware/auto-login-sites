# Auto-login to sites

This project uses the [Splinter](https://splinter.readthedocs.io/) Python package to automate internet sites login. As an example we provide code for [freedns.afraid.org](https://freedns.afraid.org), but you can add any other site. Get inspiration from *freedns.py* to make your own script.


## Installation

1. Clone this repository to your local computer:

   ```bash
   git clone https://github.com/contaware/auto-login-sites.git
   ```

2. Install dependencies:

   ```bash
   pip install python-dotenv
   pip install "splinter[selenium]"
   ```

3. In project root directory create an `.env` file with the following settings:

   ```bash
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

4. Run *freedns.py* periodically:
   
   - On Windows setup a Windows Task Scheduler to run daily or weekly. In the Task Scheduler Settings check **"Run only when user is logged on"**. The action should be set to run the script with the full path, something like:

     ```bat
     pyw.exe "C:\Users\USERNAME\source\repos\auto-login-sites\freedns.py"
     ```

     Hint: **do not use the SYSTEM account, use your Windows account**, that's because Python is usually installed for a specific user which has user specific packages installed.

   - In Linux use systemd or cron and on macOS you can use cron.
