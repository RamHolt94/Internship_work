from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from app.application import Application


def browser_init(context):
    """
    Initialize the browser with the given context.

    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, timeout=10)

    context.app = Application(context.driver)


def before_all(context):
    """
    Hook to run before all tests.
    """
    browser_init(context)


def before_scenario(context, scenario):
    """
    Hook to run before each scenario.
    """
    print(f'\nStarted scenario: {scenario.name}')
    if not context.driver:
        browser_init(context)


def after_scenario(context, scenario):
    """
    Hook to run after each scenario.
    """
    if context.driver:
        context.driver.delete_all_cookies()
        context.driver.quit()


def before_step(context, step):
    """
    Hook to run before each step.
    """
    print(f'\nStarted step: {step}')


def after_step(context, step):
    """
    Hook to run after each step.
    """
    if step.status == 'failed':
        print(f'\nStep failed: {step}')