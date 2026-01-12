Write-Host "Activating virtual environment..."
.\playwright_test_env\Scripts\activate

Write-Host "Running tests with Allure..."
pytest --alluredir=allure-results

Write-Host "Generating Allure report..."
allure serve allure-results