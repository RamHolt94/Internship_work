from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open the Reelly main page')
def open_reelly_main_page(context):
    context.driver.get("https://soft.reelly.io/sign-in")


@when('Log in to the page')
def login(context):
    context.driver.find_element(By.CSS_SELECTOR, '#email-2').send_keys("test+Ram+Careerist")
    context.driver.find_element(By.CSS_SELECTOR, "[wized='passwordInput']").send_keys("Ramasses27!")
    context.driver.find_element(By.CSS_SELECTOR, "[wized='loginButton']").click()


@when('Click on Secondary option at the left side menu')
def click_on_secondary_option(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[class*='Secondary']"))
    ).click()


@then('Verify the right page opens')
def verify_right_page(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='Listings'][class*='Agents']"))
    )


@then('Filter the products by price range from 1200000 to 2000000')
def filter_products_by_price_range(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.filter-button"))
    ).click()
    context.driver.find_element(By.CSS_SELECTOR, "[wized='unitPriceFromFilter']").send_keys("1200000")
    context.driver.find_element(By.CSS_SELECTOR, "[wized='unitPriceToFilter']").send_keys("2000000")
    context.driver.find_element(By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']").click()


@then("Verify the price in all cards is inside the range (1200000 - 2000000)")
def verify_all_cards_in_price_range(context):
    cards = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[class*='w-layout-grid listing-grid']"))
    )
    for index, card in enumerate(cards):
        range_element = card.find_element(By.CSS_SELECTOR, "[wized='unitPriceMLS']")
        card_range = int(range_element.text.replace(",", ""))
        assert 1200000 <= card_range <= 2000000, f"Card {index} price {card_range} is out of range"
