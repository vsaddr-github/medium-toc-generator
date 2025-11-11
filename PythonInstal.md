🐍 Installing Python (All Platforms)

Before running this app, make sure you have Python 3.10 or newer installed.
You only need to do this once.
________________________________________
🪟 Windows (Simplest — Microsoft Store)
1.	Open the Start menu, search for Microsoft Store, and open it.
2.	Search for “Python 3.12” (or the latest version).
3.	Select the one published by the Python Software Foundation (official blue-and-yellow logo).
4.	Click Get or Install.
5.	When it’s done, open Command Prompt and run:
6.	python --version
You should see something like:
Python 3.12.x
If that works — you’re good! ✅
(Tip: if python doesn’t work, try py --version instead.)
7.	Optional: verify pip (Python’s package manager):
8.	pip --version
If that prints a version, everything’s ready for the next step.

________________________________________
🍏 macOS
1.	Open Terminal (⌘ + Space → type Terminal).
2.	Check if Python 3 is already there:
3.	python3 --version
4.	If not installed, install Homebrew (if you don’t have it):
5.	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
6.	Then install Python:
7.	brew install python
8.	Confirm:
9.	python3 --version

________________________________________
🐧 Linux (Ubuntu / Debian / Mint / Raspberry Pi etc.)
Most distributions already include Python 3, but you can update it:
sudo apt update
sudo apt install python3 python3-pip -y
Then verify:
python3 --version
pip3 --version
For Fedora or Red Hat:
sudo dnf install python3 python3-pip -y

________________________________________
🧩 After Installing Python
Once Python is installed, open your terminal (or Command Prompt) and verify:
python --version
or
python3 --version
Then move on to installing the project dependencies:
pip install -r requirements.txt
and run the app:
python app.py
Finally, visit
👉 http://127.0.0.1:7860
to use your Medium Table of Contents Generator.
________________________________________

⚡ Quick Install & Run (One-Line Setup)
If you just want to get the app running as fast as possible, here are copy-paste commands for each system.
They’ll install Python (if needed), required packages, and start the server automatically.
________________________________________
🪟 Windows (PowerShell)
💡 Requires Windows 10/11 with Microsoft Store enabled.
Copy this entire block and paste it into PowerShell (press Win + X → Windows PowerShell):
# Install Python 3.12 from Microsoft Store (if not already installed)
winget install -e --id Python.Python.3.12

# Verify installation
python --version

# Create project folder and enter it
mkdir medium-toc-generator -ErrorAction SilentlyContinue
cd medium-toc-generator

# Clone the repo (replace with your GitHub username)
git clone https://github.com/YOURUSERNAME/medium-toc-generator.git .
# Install required Python packages
pip install -r requirements.txt

# Run the app
python app.py
Then open your browser at:
👉 http://127.0.0.1:7860
________________________________________
🍏 macOS (Terminal)
# Install Homebrew if missing
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3 and Git
brew install python git

# Clone the repo (replace with your GitHub username)
git clone https://github.com/YOURUSERNAME/medium-toc-generator.git
cd medium-toc-generator

# Install dependencies
pip3 install -r requirements.txt

# Run the app
python3 app.py
Then visit → http://127.0.0.1:7860
________________________________________
🐧 Linux (Ubuntu / Debian / Mint)
sudo apt update
sudo apt install -y python3 python3-pip git

git clone https://github.com/YOURUSERNAME/medium-toc-generator.git
cd medium-toc-generator

pip3 install -r requirements.txt
python3 app.py
Then open your browser at:
👉 http://127.0.0.1:7860
________________________________________
✅ Notes
•	If python doesn’t work, try python3.
•	The app will start on port 7860 (default for local testing).
•	Stop it anytime by pressing CTRL + C in the terminal.

