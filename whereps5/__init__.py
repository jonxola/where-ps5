from pathlib import Path
from selenium import webdriver

from . import target
from . import bestbuy
from . import amazon

def check():
    driver = webdriver.Chrome(
        executable_path=Path(__file__).parent.joinpath('chromedriver')
    )
    driver.implicitly_wait(10)
    stock = {
        'Target': {
            'disc': target.check_disc(driver),
            'digital': target.check_digital(driver)
        },
        'Best Buy': {
            'disc': bestbuy.check_disc(driver),
            'digital': bestbuy.check_digital(driver)
        },
        'Amazon': {
            'disc': amazon.check_disc(driver),
            'digital': amazon.check_digital(driver)
        }
    }
    driver.quit()
    show_results(stock)

def show_results(stock):
    headers = ('Retailer', 'Disc', 'Digital')
    print(f'{headers[0]:15}{headers[1]:15} {headers[2]:15}')
    print('=' * (15 * 3))
    for retailer in stock:
        disc = '🟢' if stock[retailer]['disc'] else '❌'
        digital = '🟢' if stock[retailer]['digital'] else '❌'
        print(f'{retailer:15}{disc:15}{digital:15}')