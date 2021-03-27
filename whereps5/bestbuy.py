from selenium.common.exceptions import NoSuchElementException

def check_disc(driver):
    '''Check for a PS5 disc edition on bestbuy.com'''
    driver.get('https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')
    try:
        # look for the add to cart button
        btn = driver.find_element_by_css_selector('button.add-to-cart-button')
    except NoSuchElementException:
        # if we didn't find it, assume it's out of stock
        return False
    else:
        # otherwise check if it says sold out
        return not btn.text == 'Sold Out'

def check_digital(driver):
    '''Check for a PS5 digital edition on bestbuy.com'''
    driver.get('https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161')
    try:
        # look for the add to cart button
        btn = driver.find_element_by_css_selector('button.add-to-cart-button')
    except NoSuchElementException:
        # if we didn't find it, assume it's out of stock
        return False
    else:
        # otherwise check if it says sold out
        return not btn.text == 'Sold Out'