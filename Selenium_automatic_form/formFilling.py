from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def fill_form():
    try:
        driver = webdriver.Chrome()

        # Open the Google Form
        driver.get("https://forms.gle/WT68aV5UnPajeoSc8")

        # Wait for the page to load (optional)
        time.sleep(2)

        # Find the input element using aria-labelledby
        full_name_input = driver.find_element(By.XPATH, "//input[@aria-labelledby='i1']")
        full_name_input.send_keys("Vikas Kansotiya")

        contact_number_input = driver.find_element(By.XPATH, "//input[@aria-labelledby='i5']")
        contact_number_input.send_keys("9664229639")

        email_id_input = driver.find_element(By.XPATH, "//input[@aria-labelledby='i9']")
        email_id_input.send_keys("vikaskansotiyasujangarh@gmail.com")

        full_address_input = driver.find_element(By.XPATH, "//textarea[@aria-labelledby='i13']")
        full_address_input.send_keys("Sujangarh(Churu), Rajasthan")

        pin_code_input = driver.find_element(By.XPATH, "//input[@aria-labelledby='i17']")
        pin_code_input.send_keys("331507")

        dob_input = driver.find_element(By.XPATH, "//input[@aria-labelledby='i25']")
        dob_input.send_keys("09-07-2002")
        dob_input.send_keys(Keys.ENTER)

        gender_input = driver.find_element(By.XPATH, "//input[@aria-labelledby='i26']")
        gender_input.send_keys("Male")

        code_input = driver.find_element(By.XPATH, "//input[@aria-labelledby='i30']")
        code_input.send_keys("GNFPYC")

        driver.save_screenshot("filled_form.png")

        # Submit the form
        submit_button = driver.find_element(By.XPATH, "//div[@role='button' and @aria-label='Submit']")
        submit_button.click()

        # Wait for the confirmation page to load
        time.sleep(3)

        # Take a screenshot of the confirmation page
        driver.save_screenshot("confirmation_page.png")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    fill_form()