from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
def send(Text):
    strFrom = 'Review Snail<snail@reviewsnail.com>'
    strTo = ['korhanozdemir90@gmail.com']
    #strTo='korhanozdemir90@gmail.com'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'New Review at Your Product!'
    msgRoot['From'] = strFrom
    msgRoot['To'] = ",".join(strTo)

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText(Text,'html')
    msgAlternative.attach(msgText)

    ust_fp = open('/home/ReviewDetectorbot/.local/mail/ust.png', 'rb')
    msgust = MIMEImage(ust_fp.read())
    ust_fp.close()
    msgust.add_header('Content-ID', '<ust>')
    msgRoot.attach(msgust)
    alt_fp = open('/home/ReviewDetectorbot/.local/mail/alt.png', 'rb')
    msgalt = MIMEImage(alt_fp.read())
    alt_fp.close()

    msgalt.add_header('Content-ID', '<alt>')
    msgRoot.attach(msgalt)

    import smtplib
    smtp = smtplib.SMTP('smtp.zoho.com',587)
    smtp.starttls()
    smtp.login('snail@reviewsnail.com', '1928374655Snail__')
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()

send("a")