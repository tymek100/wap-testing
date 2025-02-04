# Simple WAP Testing Framework by Tymek

<img src="assets/twitch.gif" width="200" />

## System requirements
Mac/Linux with Python 3.12, Chrome/Chromium and ChromeDriver installed.
### Mac:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python@3.12
brew install --cask google-chrome
brew install chromedriver
```
### Ubuntu:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.12 -y
sudo snap install chromium
sudo apt install -y chromium-chromedriver

```

## Prepare Python environment
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Run Tests
```bash
pytest
```

## Project Structure

This folder structure follows a typical Page Object Model approach combined with Pytest, making it easy to add new tests or extend existing ones by creating new page object classes or test files as needed.

```
.
├── README.md
├── pytest.ini
├── requirements.txt
├── conftest.py
├── tests
│   └── test_wap_twitch.py
├── pages
│   ├── base_page.py
│   ├── twitch_home_page.py
│   └── twitch_streamer_page.py
├── screenshots
└── assets
```

### README.md
Provides an overview of the project, instructions for installation, usage, and an explanation of the testing framework.

### pytest.ini
A configuration file for Pytest.

### requirements.txt
Lists the Python dependencies required to run the tests.

### conftest.py
A Pytest configuration file which contains a global fixture for the the setup and teardown of the Selenium WebDriver.

### tests/
This folder holds all test files. Each file should contain at least one Pytest test.
        
#### - test_wap_twitch.py
Implements the end-to-end test scenario for Twitch’s mobile web experience.

### pages/
A collection of Page Object Model (POM) classes. Each class represents a “page” or significant component within the application under test. This helps keep tests more readable and maintainable by separating page-specific details from test logic.

#### - base_page.py
A base class that contains common methods used across all pages (e.g., waiting for elements, clicking elements, taking screenshots, handling pop-ups).

#### - twitch_home_page.py
Encapsulates actions and locators related to the Twitch home or search page—such as opening the Twitch URL, clicking the search icon, and entering text into the search bar.

#### - twitch_streamer_page.py
Encapsulates actions and locators related to a streamer’s page—such as handling pop-ups, waiting for the stream to load, and taking screenshots once fully loaded.

### screenshots/
A directory that stores any screenshots captured during the test runs.

### assets/
A directory that stores a .gif file with the test demo.
