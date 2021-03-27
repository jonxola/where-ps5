from selenium.common.exceptions import NoSuchElementException

def check_disc(driver):
    '''Look for a PS5 disc edition on target.com'''
    driver.get('https://www.target.com/p/playstation-5-console/-/A-81114595')
    try:
        # look for the sold out element
        driver.find_element_by_css_selector('div[data-test="soldOutBlock"]')
    except NoSuchElementException:
        # if we didn't find it, assume it's in stock
        return True
    else:
        return False

def check_digital(driver):
    '''Look for a PS5 digital edition on target.com'''
    driver.get('https://www.target.com/p/playstation-5-digital-edition-console/-/A-81114596')
    try:
        # look for the sold out element
        driver.find_element_by_css_selector('div[data-test="soldOutBlock"]')
    except NoSuchElementException:
        # if we didn't find it, assume it's in stock
        return True
    else:
        return False