from selenium import webdriver
from pyvirtualdisplay import Display
import os
import time
from Datecompare import dateBeautify,dateComparison
import mail.Mail
import ast

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1")

Review_Dates ={}
Review_Stars ={}

Path_of_main = os.path.realpath(__file__)
Path_of_database= Path_of_main.replace("reviewbeta.py",R"databases")
Path_to_asins =Path_of_main.replace("reviewbeta.py",R"Asins")
Path_of_newreviews = Path_of_main.replace("reviewbeta.py",R"New reviews")
Path_of_edited= Path_of_main.replace("reviewbeta.py",R"Edited")

ASIN_list = open(Path_to_asins +r"/"+ "ASINs.txt").readlines()
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
Name_of_lasttxt2 = sortfiles(Path_of_edited)[-1]

print(Name_of_lasttxt)
Test_file = open(Path_of_database+r"/"+Name_of_lasttxt, "r")
New_file = open((Path_of_database+r"/"+name),'w+')
New_Reviews = open(Path_of_newreviews+r"/"+ name_new,"w+")

empty_asins=[]
changed_reviews={}
with Display():
    with open((Path_of_edited+r"/"+name),'w+') as Edit_file, open(Path_of_edited+r"/"+Name_of_lasttxt2, "r") as edited_file:
        driver = webdriver.Firefox(profile)
        for ASIN,line in zip(ASIN_list,edited_file):
            driver.get(
                "https://www.amazon.com/product-reviews/" + ASIN + "/ref=cm_cr_othr_d_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent#R2OYJFRLIO5YER")

            time.sleep(2)

            if len(driver.find_elements_by_css_selector("b.h1"))>0:
                if driver.find_elements_by_css_selector("b.h1")[0].text == "Looking for something?":
                    print("No product exists at " + ASIN)
                    empty_asins.append(ASIN.rstrip())
                    continue

            if not driver.find_elements_by_css_selector("span[data-hook='review-date']") == []:
                print("Succesful request!")
                reviewws = driver.find_elements_by_css_selector("span[data-hook='review-date']")
                starss = driver.find_elements_by_css_selector("i[data-hook='review-star-rating'] span")
                staars = list(map(lambda x: x.get_attribute("innerHTML"), starss))
                dates = list(map(lambda x: x.text, reviewws))
                stars = list(map(lambda x: x.replace(".0 out of 5 stars"," star"), staars))
                id= driver.find_elements_by_css_selector("div[data-hook='review']")
                parsedid= list(map(lambda x: x.get_attribute("id"), id))
                editTest= dict(zip(parsedid, stars))


                stripline = line.rstrip()
                oldstars= ast.literal_eval("{"+stripline.split("{")[-1])
                print(oldstars)
                print("new")

                Edit_file.write(ASIN.rstrip() + ":" + " " + str(editTest) + "\n")
                if oldstars==editTest:
                    continue
                else:
                    for key in editTest:
                        if editTest[key]!=oldstars[key]:
                            changed_reviews[ASIN]=key
                            changed_reviews[oldstars[key]]=editTest[key]
            else:
                dates =["no review yet"]
                stars =["no review yet"]
                editTest=["no review yet"]

            Review_Dates[ASIN.rstrip()]=dates[0]
            Review_Stars[ASIN.rstrip()]=stars[0]
            New_file.write(ASIN.rstrip() + ":" + "Last review " + Review_Dates[ASIN.rstrip()] + "\n")
        driver.close()

print(changed_reviews)

for line in Test_file:
    linne = line.rstrip()
    old_review =dateBeautify(linne.split("Last review ")[-1].rstrip())
    Token = linne.split(":")[0]
    if Token in empty_asins:
        continue

    print("Review_Dates",Review_Dates,dates)
    new_review =dateBeautify(Review_Dates[Token].rstrip())
    print(old_review,new_review)
    if not old_review == new_review:
        if dateComparison(new_review,old_review):
            text = ' <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"><div style=" background-color: white;  width: 693px; border: #cea62c solid 2px; border-radius: 1rem"><div style=""><img src="cid:ust" alt=""></div><div style="font-family: Roboto;font-size: 27pt; text-align: center">You have a new<b style="display: block;" >{} review.</b></div><div style="text-align: center; margin: 115px;"><a style="border: 14px solid #f5edd5;background-color: #bd3535;color: white;padding: 61px 14px;font-size: 35px;font-family: roboto;border-radius: 100%; text-decoration:none;" href="https://www.amazon.com/product-reviews/{}/ref=cm_cr_othr_d_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent#R2OYJFRLIO5YER" ><b>Check it!</b></a></div><div ><img src="cid:alt" alt=""></div></div></div><div style="font-family: Roboto; font-size: 8pt; color: darkgray; text-align: center; width: 693px;"><p>Copyright Ⓒ ReviewSnail.com, 2018 <br>All Rights Reserved. <br>info@reviewsnail.com</p></div>'.format(Review_Stars[Token],Token)
            mail.Mail.send(text)
            print("Email sent.")
        print("New " + Review_Stars[Token] + " review on " + "https://www.amazon.com/product-reviews/" + Token + "/ref=cm_cr_othr_d_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent#R2OYJFRLIO5YER")
        New_Reviews.write("New " + Review_Stars[Token] + " review: " + "https://www.amazon.com/product-reviews/" + Token + "/ref=cm_cr_othr_d_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent#R2OYJFRLIO5YER\n")

print("-------------------")
print("       DONE")
print("-------------------")

New_file.close()
Test_file.close()
New_Reviews.close()

