from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
def send(Text):
    strFrom = 'Review Snail<snail@reviewsnail.com>'
    strTo = ['info@reviewsnail.com']
    #strTo='kologluege@gmail.com'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = "Review Snail'in Kapalı Beta Programına Hoş Geldiniz! "
    msgRoot['From'] = strFrom
    msgRoot['To'] = ",".join(strTo)

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText(Text,'html')
    msgAlternative.attach(msgText)

    ust_fp = open('/home/ReviewDetectorbot/.local/mail/Logo.png', 'rb')
    msgust = MIMEImage(ust_fp.read())
    ust_fp.close()
    msgust.add_header('Content-ID', '<ust>')
    msgRoot.attach(msgust)
    orta_fp = open('/home/ReviewDetectorbot/.local/mail/Bars.png', 'rb')
    msgorta = MIMEImage(orta_fp.read())
    orta_fp.close()
    msgorta.add_header('Content-ID', '<orta1>')
    msgRoot.attach(msgorta)
    orta2_fp = open('/home/ReviewDetectorbot/.local/mail/sari.png', 'rb')
    msgorta2 = MIMEImage(orta2_fp.read())
    orta2_fp.close()
    msgorta2.add_header('Content-ID', '<orta2>')
    msgRoot.attach(msgorta2)
    alt_fp = open('/home/ReviewDetectorbot/.local/mail/Bars2.png', 'rb')
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


text2=r'<style>@font-face {    font-family: "Rock Salt";    src: url(RockSalt.tff);}</style><body>    <div id="main" style="width: 900px;margin: auto;">        <div id="upper" class="tcenter" style="text-align: center;margin-top: 60px;margin-bottom: 50px;">            <img id="logo" class="" src="cid:ust" alt="" style="vertical-align: middle;padding-right: 35px; width: 35%">            <span class="font bold header inline " style="display: inline-block;font-family: &quot;Roboto&quot;;font-weight: 400;font-size: 32pt;">Merhabalar</span></div>        <div id="colorful" class="" style="padding-top: 10px;padding-bottom: 10px;">            <img class="m35 left" src="cid:orta1" alt="" style="float: left;margin-right: 15px;margin-top: 8px;margin-left: 55px;">            <p id="" class="midtext font" style="font-family: &quot;Roboto&quot;;font-size: 14pt;width: 95%;"><span class="rocksalt" style="font-family: &quot;Rock salt&quot;;">Review Snail</span> sizin için ürünlerinize gelen geribildirimleri 7/24 takip eden ve <span class="red" style="color: #cd1437;">olumsuz müşteri deneyimlerini</span> iyileştirmeniz için size yardımcı olan bir hizmettir.</p>        </div>            <div id="midlogo" class="tcenter" style="text-align: center; padding-top: 20px;">            <img src="cid:orta2" alt="">        </div>         <div id="colorful2" class="" style="padding-top: 15px;padding-bottom: 15px;margin-top: 30px;">            <img class="m36 left" src="cid:alt" alt="" style="float: left;margin-right: 15px;margin-left: 55px;margin-bottom: 8px;">            <p id="lowtext" class="midtext font " style="font-family: &quot;Roboto&quot;;font-size: 14pt;width: 100%;">Kapalı beta programımıza <span class="blue" style="color: #0a91c6;">hoşgeldiniz.</span><br>Yeni bir "Review"de görüşmek üzere. </p>        </div>        <div id="footer" class="tcenter font" style="text-align: center;font-family: &quot;Roboto&quot;;color: darkgrey;font-size: 10pt;">            <p>                Copyright Ⓒ ReviewSnail.com, 2019 <br> All Rights Reserved. <br>info@reviewsnail.com            </p>        </div>    </div>    </body>'
send(text2)



