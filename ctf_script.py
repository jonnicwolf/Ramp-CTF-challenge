from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://tns4lpgmziiypnxxzel5ss5nyu0nftol.lambda-url.us-east-1.on.aws/challenge")

chars = []
class_attrs = []

sections = driver.find_elements(By.CSS_SELECTOR, 'section[data-id^="92"]')
for section in sections:
  articles = section.find_elements(By.CSS_SELECTOR, 'article[data-class$="45"]')
  for article in articles:
    divs = article.find_elements(By.CSS_SELECTOR, 'div[data-tag*="78"]')
    for div in divs:
      bs = div.find_elements(By.TAG_NAME, 'b')
      for b in bs:
          class_attr = b.get_attribute('class')
          class_attrs.append(class_attr)
          if class_attr == "ramp ref":
            value = b.get_attribute("value")
            if value:
              chars.append(value)

print('classes: ', class_attrs)

hidden_url = ''.join(chars)
print("url: ", hidden_url)

input("Enter to exit")
driver.quit()