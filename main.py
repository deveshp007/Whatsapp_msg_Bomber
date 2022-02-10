from selenium import webdriver

# Adding Firefox driver(geckodriver) path 
driver = webdriver.Firefox(executable_path='/home/devesh/selenium_firefox/drivers/geckodriver')
 
driver.get("https://web.whatsapp.com/")

print("Login")

name = input("Enter the name of person or Group : ")
count = int(input("Message count : "))
message = input("Enter the message : ")

user = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div/div/div/div[2]/div[1]/div[1]/span[@title="{}"]'.format(name))

user.click()

msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

for i in range(count):
    msgBox.send_keys(message)
    sendbtn = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    sendbtn.click()



