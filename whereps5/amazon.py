from selenium.common.exceptions import NoSuchElementException

def check_disc(driver):
    driver.get('https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG?ref_=ast_sto_dp')
    try:
        # look for availability element
        availability = driver.find_element_by_css_selector('#availability')
    except NoSuchElementException:
        # if we can't find it, assume out of stock
        return False
    else:
        return 'Currently unavailable' not in availability.text

def check_digital(driver):
    driver.get('https://www.amazon.com/PlayStation-5-Digital/dp/B08FC6MR62?ref_=ast_sto_dp')
    try:
        # look for availability element
        availability = driver.find_element_by_css_selector('#availability')
    except NoSuchElementException:
        # if we can't find it, assume out of stock
        return False
    else:
        return 'Currently unavailable' not in availability.text