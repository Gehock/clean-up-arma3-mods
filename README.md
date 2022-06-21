# Cleaning up Arma 3 mods

This script cleans up Arma 3 mods that are unsubscribed but still located on
the disk.

## Setting up

1. Copy `secret.py.example` to `secret.py` and add your steam username, steam
   workshop path and a steamcommunity.com cookie (see
   [below](#finding-the-cookie)).

2. Create a virtual environment:

   ```shell
   sudo apt install python3-venv python3-pip
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```shell
   source venv/bin/activate
   ```

4. Install required packages:

   ```shell
   pip install -r requirements.txt
   ```

## Finding the cookie

1. Navigate to <https://steamcommunity.com>
2. Log in to your steam account
3. Open the Developer Tools (F12 or Ctrl+Shift+I)
4. Go to the Application tab
5. Find the cookie called `steamLoginSecure` and copy the content to `secret.py`

**Warning: This cookie gives the script full access to your steam account. Do
not input the cookie into any script you do not trust.**
