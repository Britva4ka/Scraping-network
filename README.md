# Scraping-network

## Installation

Clone repository
```
git clone https://github.com/Britva4ka/Scraping-network
```

Create and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```
pip3 install -r requirements.txt 
```

Create `.env` from `env.example` file and update as needed
```
cp env.example .env
```

### Chromedriver
Download from official website proper version of chromedriver for your OS: https://chromedriver.chromium.org/downloads
- Update path to `chromedriver` executable in env variable
- Allow `chromedriver` to run on macOS 
```
xattr -d com.apple.quarantine chromedriver
```
### Run application

Ensure, that `social-network` application is running
```
cd scraping-selenium
python3 app.py
```
### NEW FEATURES:
1. Can fake user (`fake=True` while initialisation class)
2. Can fake content (`fake=True` in add_post method arguments)
3. Can make delay between actions (`delay = config.CHROME_DRIVER_DELAY` while initialisation class)


* Make sure that user data from env is correct. Good luck. 
