# TestAssignment – Playwright Automation
# Installation & Setup

# Create and activate a virtual environment
python -m venv playwright_test_env playwright_test_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

# Run all tests (headed mode, Chrome)
pytest test_cases --headed --browser-channel=chrome

# Run a specific test
pytest test_cases/test_promotions.py --headed --browser-channel=chrome

# Run with Allure
pytest --alluredir=allure-results allure serve allure-results

# To Execute
python -m venv playwright_test_env playwright_test_env\Scripts\activate 
pip install -r requirements.txt 
playwright install 
pytest test_cases --headed --browser-channel=chrome
