from selenium import webdriver
from pyvirtualdisplay import Display
import os
import time
import yagmail
from random import randint,choice

Review_Dates ={}
Review_Stars ={}

Path_of_main = os.path.realpath(__file__)
Path_of_database= Path_of_main.replace("Review.py",R"databases")
Path_to_asins =Path_of_main.replace("Review.py",R"Asins")
Path_of_newreviews = Path_of_main.replace("Review.py",R"New reviews")

ASIN_list = open(Path_to_asins +r"/"+ "ASINs.txt").readlines()

to_adrss = ["korhanozdemir90@gmail.com"]
subject = "New Review at your product!"
yag = yagmail.SMTP({"reviewdetectorbot@gmail.com" : "Review Detector Bot"}, "abcd5dcba")
msg="\n" \
    "---------------------------------------------------------\n" \
    "Please do not reply to this mail. Thank you\n" \
    "---------------------------------------------------------\n"

date = time.localtime(time.time())
hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
def sortfiles(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    return a

name = "%d_%d_%d_%d_%d.txt"%(date[1],date[2],date[0],hour,minute)
name_new = "New reviews %d_%d_%d_%d_%d.txt"%(date[1],date[2],date[0],hour,minute)
Name_of_lasttxt = sortfiles(Path_of_database)[-1]
print(Name_of_lasttxt)
Test_file = open(Path_of_database+r"/"+Name_of_lasttxt, "r")
New_file = open((Path_of_database+r"/"+name),'w+')
New_Reviews = open(Path_of_newreviews+r"/"+ name_new,"w+")

with Display():
    driver = webdriver.Firefox()
    for ASIN in ASIN_list:
        driver.get(
            "https://www.amazon.com/product-reviews/" + ASIN + "/ref=cm_cr_othr_d_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent#R2OYJFRLIO5YER")

        time.sleep(2)

        if not driver.find_elements_by_css_selector("span[data-hook='review-date']") == []:
            reviewws = driver.find_elements_by_css_selector("span[data-hook='review-date']")
            starss = driver.find_elements_by_css_selector("i[data-hook='review-star-rating'] span")
            staars = list(map(lambda x: x.get_attribute("innerHTML"), starss))
            dates = list(map(lambda x: x.text, reviewws))
            stars = list(map(lambda x: x.replace(".0 out of 5 stars"," star"), staars))

        else:
            reviews =["no review yet"]

        Review_Dates[ASIN.rstrip()]=dates[0]
        Review_Stars[ASIN.rstrip()]=stars[0]

        Wait_time= randint(1, 5)
        time.sleep(Wait_time)

        for line in Test_file:
            linne = line.rstrip()
            old_review = linne.split("Last review ")[-1]
            Token = linne.split(":")[0]
            new_review = Review_Dates[Token]
            if not old_review == new_review:
                html_link = '<a href=' + "https://www.amazon.com/product-reviews/" + Token + "/ref=cm_cr_othr_d_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent#R2OYJFRLIO5YER" + ' title="decorated!"> Link!</a>'
                text = "Hi!\nIt's Amazon Review Detector Bot!\nYou have a new <b>{}</b> review on the listing below:\n".format(Review_Stars[Token]) + html_link + "\n" + msg  # '<img src="https://drive.google.com/file/d/13PUeXQwSpe2KGNRWtkt25OmmhLlz_jW1/edit" alt="logo" style="display:block" title="logo" height ="256" width="256">'
                """if not Review_Stars[Token] == "Unable to find any review on this product":
                    yag.send(to_adrss, subject, text)"""
                print("New " + Review_Stars[Token] + " review on " + "https://www.amazon.com/product-reviews/" + Token + "/ref=cm_cr_othr_d_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent#R2OYJFRLIO5YER")
                New_Reviews.write("New " + Review_Stars[Token] + " review: " + "https://www.amazon.com/product-reviews/" + Token + "/ref=cm_cr_othr_d_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent#R2OYJFRLIO5YER\n")

print("-------------------")
print("       DONE")
print("-------------------")
New_file.close()
Test_file.close()
New_Reviews.close()
yag.close()

