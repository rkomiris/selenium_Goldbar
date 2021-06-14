#Author: Rohan Komirishetty

import selenium
import time
from selenium import webdriver



driver=webdriver.Chrome(executable_path="C:\\Users\\tarun\\Downloads\\chromedriver.exe")

#print(type(driver))

driver.get("http://ec2-54-208-152-154.compute-1.amazonaws.com/")

pageTitle=driver.title

#print(pageTitle)

assert("React App" in pageTitle)

#Buttons on the ReactApp brought on to the py script

reset_button=driver.find_element_by_xpath('//button[text()="Reset"]')
weigh_button=driver.find_element_by_id("weigh")
zero_button = driver.find_element_by_id("coin_0")
one_button = driver.find_element_by_id("coin_1")
two_button = driver.find_element_by_id("coin_2")
three_button = driver.find_element_by_id("coin_3")
four_button = driver.find_element_by_id("coin_4")
five_button = driver.find_element_by_id("coin_5")
six_button = driver.find_element_by_id("coin_6")
seven_button = driver.find_element_by_id("coin_7")
eight_button = driver.find_element_by_id("coin_8")

#print(type(reset_button))

#Input fields on the ReactApp left and right bowls brought on to the py script

#So, we have already divided it into three groups
#IDs are left_0, left_1 and left_2. Have to add 0, 1 and 2 
#IDs are right_0, right_1 and right_2. Have to add 3, 4 and 5
#In any scenario the above mentioned two group will be weighed against each other first

driver.find_element_by_xpath('//*[@id="left_0"]').send_keys("0")
driver.find_element_by_xpath('//*[@id="left_1"]').send_keys("1")
driver.find_element_by_xpath('//*[@id="left_2"]').send_keys("2")

driver.find_element_by_xpath('//*[@id="right_0"]').send_keys("3")
driver.find_element_by_xpath('//*[@id="right_1"]').send_keys("4")
driver.find_element_by_xpath('//*[@id="right_2"]').send_keys("5")

#so group one left will be weigh more/less or equal to group two

weigh_button.click()


#Got the answer, there will be three cases from here 


#function when evoked that prints all the weighings and number of weighings to the terminal

def number_of_weighings():
    print("Weighting list is: ---------------------------------")

    weight_counts = 0
    html_list = driver.find_element_by_xpath('//*[@class="game-info"]')
    items = html_list.find_elements_by_tag_name("li")
    for item in items:
        weight_counts += 1
        text = item.text
        print(text)
    print("Number of weighings:", weight_counts)
    print("----------------------------------------------------")

#function when evoked will print the alert message to the terminal

def alert_message():
    obj = driver.switch_to.alert
    print("Alert message says:")
    print(obj.text)

#The algorithm does the weighing only twice the below function evaluates the results from first time weighing and calculates the 
#the results accordingly; which_group will point to the groups we've created and obtained is the operator that pops in results area after weighing
#after determining the gold bar .click() function will trigger the alert message on the react App

def give_the_result(which_group, obtained):
    print("The obatined is: ", obtained)
    if which_group == 0:
        if obtained == "=":
            #print("The answer is 2")
            number_of_weighings()
            two_button.click()
        elif obtained == ">":
            #print("The answer is 1")
            number_of_weighings()
            one_button.click()
        else:
            #print("The answer is 0")
            number_of_weighings()
            zero_button.click()
    
    if which_group == 1:
        if obtained == "=":
            #print("The answer is 5")
            number_of_weighings()
            five_button.click()
        elif obtained == ">":
            #print("The answer is 4")
            number_of_weighings()
            four_button.click()
        else:
            #print("The answer is 3")
            number_of_weighings()
            three_button.click()
    
    if which_group == 2:
        if obtained == "=":
            #print("The answer is 8")
            number_of_weighings()
            eight_button.click()
        elif obtained == ">":
            #print("The answer is 7")
            number_of_weighings()
            seven_button.click()
        else:
            #print("The answer is 6")
            number_of_weighings()
            six_button.click()
    
    alert_message()

#The function below returns the value that pops up on the button in results sections, we have to use .sleep() in order for the 
# value to actually change on the button while the app is running    

def see_the_result():
    time.sleep(3)
    html_list = driver.find_element_by_xpath('//*[@class="result"]')
    items = html_list.find_element_by_id("reset")
    return items.text

result_value = see_the_result()

#The code section below evaluates weights of the gold bars in groups of three for the first time 
#In our case we always evaluate groups [0,1,2] and [3,4,5] first

if(result_value == "<") :
    #print("This means that group 0,1,2 has the lighter one")
    reset_button.click()
    driver.find_element_by_xpath('//*[@id="left_0"]').send_keys("0")
    driver.find_element_by_xpath('//*[@id="right_0"]').send_keys("1")
    weigh_button.click()
    give_the_result(0, see_the_result())
    
elif(result_value == ">"):
    #print("This means that group 3,4,5 has the lighter one")
    reset_button.click()
    driver.find_element_by_xpath('//*[@id="left_0"]').send_keys("3")
    driver.find_element_by_xpath('//*[@id="right_0"]').send_keys("4")
    weigh_button.click()
    give_the_result(1, see_the_result())

elif(result_value == "="):
    #print("This means that group 6,7,8 has the lighter one")
    reset_button.click()
    driver.find_element_by_xpath('//*[@id="left_0"]').send_keys("6")
    driver.find_element_by_xpath('//*[@id="right_0"]').send_keys("7")
    weigh_button.click()
    give_the_result(2, see_the_result())

else:
    print("DEBUG: There's an error in obtaining the weight listing")