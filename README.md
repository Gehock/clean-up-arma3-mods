# Cleaning up Arma 3 mods

This script finds Arma 3 mods that are unsubscribed but still located on
the disk. The mods get moved into a separate directory (displayed at the end
of the script) where the user can then delete them.

## Setting up

1. Copy (or rename) `secret.py.example` to `secret.py` and add your steam
   profile URL, steam workshop path and a steamcommunity.com cookie (see
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

5. Run the script with

   ```shell
   python3 main.py
   ```

## Finding the cookie

**Warning: This cookie gives the script full access to your steam account. Do
not input the cookie into any script you do not trust.**

1. Navigate to <https://steamcommunity.com>
2. Log in to your steam account
3. Open the Developer Tools (F12 or Ctrl+Shift+I)
4. Go to the Application tab
5. Find the cookie called `steamLoginSecure` and copy the content to
   `secret.py`
