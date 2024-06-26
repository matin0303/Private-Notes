from PyQt5 import QtGui ,QtCore , QtWidgets
import webbrowser
import mysql.connector as connection
import sys
from MySql import *
import res2

class mypage(QtWidgets.QDialog):

    def __init__(self):
        super(mypage,self).__init__()
        self.widget=QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(10, 0, 1031, 811))
        self.widget.setStyleSheet("QPushButton#login_btn:pressed{\n" 
                                 "padding-left:5px ; padding-top:5px;border: 2px solid black} \n"
                                 "QPushButton#close_btn:pressed{\n"
                                 "padding-left:5px ; padding-top:5px;} \n"
                                 "QPushButton#create_btn:pressed{\n "
                                 "padding-left:5px ; padding-top:5px;} \n"
                                 "QPushButton#git_btn:pressed{\n"
                                 "padding-left:5px;padding-top:5px} \n"
                                 "QPushButton#linkedin_btn:pressed{\n"
                                 "padding-left:5px ; padding-top:5px} \n"
                                 "QPushButton#facebook_btn:pressed{\n"
                                 "padding-left:5px ; padding-top:5px} \n "
                                 "QPushButton#web_btn:pressed{\n"
                                 "padding-left:5px ; padding-top:5px}")


        self.bg_lable=QtWidgets.QLabel(self.widget)
        self.bg_lable.setStyleSheet("border-image:url(:/image/bg.png)")
        self.bg_lable.setGeometry(QtCore.QRect(70, 20, 941, 751))

        self.blur_lable=QtWidgets.QLabel(self.widget)
        self.blur_lable.setStyleSheet("border-image:url(:image/blur Frame.png)")
        self.blur_lable.setGeometry(QtCore.QRect(480,70,504,679))

        self.lock_image_lable=QtWidgets.QLabel(self.widget)
        self.lock_image_lable.setGeometry(QtCore.QRect(70,41,415,415))
        self.lock_image_lable.setStyleSheet("border-image:url(:image/lock.png)")

        self.new_ex_lable=QtWidgets.QLabel(self.widget)
        self.new_ex_lable.setGeometry(QtCore.QRect(104,480,387,70))
        self.new_ex_lable.setStyleSheet("color:#ffffff")
        self.new_ex_lable.setText("New Experience")
        self.font=QtGui.QFont()
        QtGui.QFontDatabase.addApplicationFont("Cooper Black Regular.ttf")
        self.font.setFamily("Cooper Black")
        self.font.setPointSize(25)
        self.new_ex_lable.setFont(self.font)

        self.create_lable=QtWidgets.QLabel(self.widget)
        self.create_lable.setGeometry(QtCore.QRect(610, 570, 300, 100))
        self.create_lable.setStyleSheet("color:#ffffff")
        self.create_lable.setText("Don’t have an account?")
        self.font=QtGui.QFont()
        QtGui.QFontDatabase.addApplicationFont("HARLOWSI.TTF")
        self.font.setFamily("Harlow Solid Italic")
        self.font.setPointSize(15)
        self.create_lable.setFont(self.font)

        self.text_lable=QtWidgets.QLabel(self.widget)
        self.text_lable.setGeometry(QtCore.QRect(97,530,387,200))
        self.text_lable.setStyleSheet("color:#ffffff")
        self.text_lable.setText("   We provide the security of \n \tyour information \n      Thanks for your trust")
        self.font=QtGui.QFont()
        self.font.setFamily("Harlow Solid Italic")
        self.font.setPointSize(18)
        self.text_lable.setFont(self.font)

        self.login_lable=QtWidgets.QLabel(self.widget)
        self.login_lable.setGeometry(QtCore.QRect(630,50,387,200))
        self.login_lable.setStyleSheet("color:#ffffff")
        self.login_lable.setText("Log-In")
        self.font=QtGui.QFont()
        self.font.setFamily("Cooper Black")
        self.font.setPointSize(40)
        self.login_lable.setFont(self.font)


        self.font=QtGui.QFont()
        self.font.setFamily("Impact")
        self.font.setPointSize(16)

        self.user_ent=QtWidgets.QLineEdit(self.widget)
        self.user_ent.setGeometry(QtCore.QRect(570, 290, 371, 51))
        self.user_ent.setStyleSheet("background-color:rgba(0,0,0,0) ; border:none ;border-Bottom:2px solid #aa55ff ; color:#ffffff")
        self.user_ent.setFont(self.font)
        self.user_ent.setPlaceholderText("User Name")

        self.icon_user_ent=QtWidgets.QPushButton(self.widget)
        self.icon_user_ent.setGeometry(QtCore.QRect(500,290,61,61))
        self.icon_user_ent.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.icon_user_ent.setEnabled(False)
        self.icon_user=QtGui.QIcon()
        self.icon_user.addPixmap(QtGui.QPixmap(":image/icons8-person-94.png"),QtGui.QIcon.Disabled)
        self.icon_user_ent.setIcon(self.icon_user)
        self.icon_user_ent.setIconSize(QtCore.QSize(100,70))

        self.pass_ent=QtWidgets.QLineEdit(self.widget)
        self.pass_ent.setGeometry(QtCore.QRect(570, 400, 371, 51))
        self.pass_ent.setStyleSheet("background-color:rgba(0,0,0,0) ; border:none ;border-Bottom:2px solid #aa55ff ; color:#ffffff")
        self.pass_ent.setFont(self.font)
        self.pass_ent.setPlaceholderText("Password")

        self.notif_lable=QtWidgets.QLabel(self.widget)
        self.notif_lable.setGeometry(QtCore.QRect(570, 480, 371, 30))
        self.notif_lable.setStyleSheet("color:red ")
        self.fontx=QtGui.QFont()
        self.fontx.setFamily("Times")
        self.fontx.setPointSize(10)
        self.notif_lable.setFont(self.fontx)

        self.icon_pass_ent=QtWidgets.QPushButton(self.widget)
        self.icon_pass_ent.setGeometry(QtCore.QRect(500,400,61,61))
        self.icon_pass_ent.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.icon_pass_ent.setEnabled(False)
        self.icon_pass=QtGui.QIcon()
        self.icon_pass.addPixmap(QtGui.QPixmap(":image/icons8-key-100") ,QtGui.QIcon.Disabled)
        self.icon_pass_ent.setIcon(self.icon_pass)
        self.icon_pass_ent.setIconSize(QtCore.QSize(100,70))

        self.login_btn=QtWidgets.QPushButton(self.widget)
        self.login_btn.setObjectName("login_btn")
        self.login_btn.setGeometry(QtCore.QRect(567, 520, 375, 71))
        self.login_btn.setStyleSheet("background-color:rgb(78, 20, 125);color:#ffffff ; border-radius:15px")
        self.login_btn.setShortcut("Enter")
        self.font.setPointSize(20)
        self.login_btn.setFont(self.font)
        self.login_btn.setText("Log-In")

        self.create_btn=QtWidgets.QPushButton(self.widget)
        self.create_btn.setObjectName("create_btn")
        self.create_btn.setGeometry(QtCore.QRect(850, 608, 61, 21))
        self.font.setPointSize(12)
        self.create_btn.setFont(self.font)
        self.create_btn.setStyleSheet("background-color:rgba(0,0,0,0);color:#ffffff")
        self.create_btn.setText("Create")


        self.linkedin_btn=QtWidgets.QPushButton(self.widget)
        self.linkedin_btn.setObjectName("linkedin_btn")
        self.linkedin_btn.setGeometry(QtCore.QRect(610,660,51,41))
        self.icon2=QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap(":/image/linkedin.png"))
        self.linkedin_btn.setIcon(self.icon2)
        self.linkedin_btn.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.linkedin_btn.setIconSize(QtCore.QSize(100,48))


        self.git_btn=QtWidgets.QPushButton(self.widget)
        self.git_btn.setObjectName("git_btn")
        self.git_btn.setGeometry(QtCore.QRect(694,660,41,41))
        self.icon3=QtGui.QIcon()
        self.icon3.addPixmap(QtGui.QPixmap(":/image/github.png"))
        self.git_btn.setIcon(self.icon3)
        self.git_btn.setIconSize(QtCore.QSize(100,50))
        self.git_btn.setStyleSheet("background-color:rgba(0,0,0,0)")

        self.facebook_btn=QtWidgets.QPushButton(self.widget)
        self.facebook_btn.setObjectName("facebook_btn")
        self.facebook_btn.setGeometry(QtCore.QRect(770,660,41,41))
        self.icon4=QtGui.QIcon()
        self.icon4.addPixmap(QtGui.QPixmap(":/image/icons8-facebook-48.png"))
        self.facebook_btn.setIcon(self.icon4)
        self.facebook_btn.setIconSize(QtCore.QSize(100,50))
        self.facebook_btn.setStyleSheet("background-color:rgba(0,0,0,0)")

        self.web_btn=QtWidgets.QPushButton(self.widget)
        self.web_btn.setObjectName("web_btn")
        self.web_btn.setGeometry(QtCore.QRect(850,660,41,41))
        self.icon5=QtGui.QIcon()
        self.icon5.addPixmap(QtGui.QPixmap(":/image/icons8-website-96.png"))
        self.web_btn.setIcon(self.icon5)
        self.web_btn.setIconSize(QtCore.QSize(100,45))
        self.web_btn.setStyleSheet("background-color:rgba(0,0,0,0)")

        self.close_btn=QtWidgets.QPushButton(self.widget)
        self.close_btn.setObjectName("close_btn")
        self.close_btn.setGeometry(QtCore.QRect(950, 30, 41, 41))
        self.close_btn.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.icon=QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":/image/icons8-close-64.png"))
        self.close_btn.setIcon(self.icon)
        self.close_btn.setIconSize(QtCore.QSize(100,50))
        self.shortcut()

        self.close_btn.clicked.connect(QtWidgets.qApp.quit)
        self.create_btn.clicked.connect(self.page2)
        self.login_btn.clicked.connect(self.login_check)
        self.linkedin_btn.clicked.connect(lambda:self.open_web("linkedin"))
        self.git_btn.clicked.connect(lambda:self.open_web("git"))
        self.facebook_btn.clicked.connect(lambda:self.open_web("facebook"))
        self.web_btn.clicked.connect(lambda:self.open_web("web"))
        
    def shortcut(self):
        self.login_btn.setShortcut("Return")
    def open_web(self,value):
        if  value == "git":
            webbrowser.open("https://github.com/matin0303")
        elif value == "linkedin":
            webbrowser.open("www.linkedin.com/in/matin-pirmohammadi-0733182b9")
        elif value == "facebook":
            pass
            #webbrowser.open("")
        elif value == "web":
            pass
            #webbrowser.open("")
    def page2(self):
        ui2=singup()
        Form1.addWidget(ui2)
        Form1.setCurrentIndex(Form1.currentIndex()+1)

    def shortcut(self):
        self.login_btn.setShortcut("Return")

    def login_check(self):
        cursor.execute(f'SELECT username FROM users WHERE username="{self.user_ent.text()}"')
        username=cursor.fetchone()
        if username == None:
            self.notif_lable.setText("")
            self.notif_lable.setText("Username or password is incorrect")
        else :
            self.notif_lable.setText("")
            cursor.execute(f'SELECT password FROM users WHERE username="{self.user_ent.text()}"')
            password=cursor.fetchone()
            if password[0] == self.pass_ent.text():

                #open main page
                self.mainPage = QtWidgets.QStackedWidget()
                self.ui2 = main_page()
                self.mainPage.addWidget(self.ui2)
                self.mainPage.show()

                
                
                #close login page
                Form1.close()
                
                print("login is succesfull")     
            else:
                self.notif_lable.setText("Username or password is incorrect")
        
class singup(QtWidgets.QDialog):
    def __init__(self):
        super(singup,self).__init__()
        self.widget=QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(10, 0, 1031, 811))
        self.widget.setStyleSheet("QPushButton#singup_btn:pressed{\n" 
                                 "padding-left:5px ; padding-top:5px;border: 2px solid black} \n"
                                 "QPushButton#close_btn:pressed{\n"
                                 "padding-left:5px ; padding-top:5px;} \n"
                                 "QPushButton#create_btn:pressed{\n "
                                 "padding-left:5px ; padding-top:5px;} \n"
                                 "QPushButton#git_btn:pressed{\n"
                                 "padding-left:5px;padding-top:5px} \n"
                                 "QPushButton#linkedin_btn:pressed{\n"
                                 "padding-left:5px ; padding-top:5px} \n"
                                 "QPushButton#facebook_btn:pressed{\n"
                                 "padding-left:5px ; padding-top:5px} \n "
                                 "QPushButton#web_btn:pressed{\n"
                                 "padding-left:5px ; padding-top:5px}")


        self.bg_lable=QtWidgets.QLabel(self.widget)
        self.bg_lable.setStyleSheet("border-image:url(:/image/bg.png)")
        self.bg_lable.setGeometry(QtCore.QRect(70, 20, 941, 751))

        self.blur_lable=QtWidgets.QLabel(self.widget)
        self.blur_lable.setStyleSheet("border-image:url(:image/blur Frame.png)")
        self.blur_lable.setGeometry(QtCore.QRect(480,70,504,679))

        self.cloud_image_lable=QtWidgets.QLabel(self.widget)
        self.cloud_image_lable.setGeometry(QtCore.QRect(40,30,470,470))
        self.cloud_image_lable.setStyleSheet("border-image:url(:image/zzz.png)")

        self.new_exp_lable=QtWidgets.QLabel(self.widget)
        self.new_exp_lable.setGeometry(QtCore.QRect(104,480,387,70))
        self.new_exp_lable.setStyleSheet("color:#ffffff")
        self.new_exp_lable.setText("New Experience")
        self.font=QtGui.QFont()
        QtGui.QFontDatabase.addApplicationFont("Cooper Black Regular.ttf")
        self.font.setFamily("Cooper Black")
        self.font.setPointSize(25)
        self.new_exp_lable.setFont(self.font)


        self.text_lable=QtWidgets.QLabel(self.widget)
        self.text_lable.setGeometry(QtCore.QRect(97,530,387,200))
        self.text_lable.setStyleSheet("color:#ffffff")
        self.text_lable.setText("   We provide the security of \n \tyour information \n      Thanks for your trust")
        self.font=QtGui.QFont()
        QtGui.QFontDatabase.addApplicationFont("HARLOWSI.TTF")
        self.font.setFamily("Harlow Solid Italic")
        self.font.setPointSize(18)
        self.text_lable.setFont(self.font)
        
        self.singup_lable=QtWidgets.QLabel(self.widget)
        self.singup_lable.setGeometry(QtCore.QRect(607,50,387,200))
        self.singup_lable.setStyleSheet("color:#ffffff")
        self.singup_lable.setText("Sing-Up")
        self.font=QtGui.QFont()
        self.font.setFamily("Cooper Black")
        self.font.setPointSize(40)
        self.singup_lable.setFont(self.font)


        self.font=QtGui.QFont()
        self.font.setFamily("Impact")
        self.font.setPointSize(16)

        self.user_ent=QtWidgets.QLineEdit(self.widget)
        self.user_ent.setGeometry(QtCore.QRect(570, 290, 371, 51))
        self.user_ent.setStyleSheet("background-color:rgba(0,0,0,0) ; border:none ;border-Bottom:2px solid #aa55ff ; color:#ffffff")
        self.user_ent.setFont(self.font)
        self.user_ent.setPlaceholderText("User Name")

        self.user_lable=QtWidgets.QLabel(self.widget)
        self.user_lable.setGeometry(QtCore.QRect(570, 350, 371, 20))
        self.user_lable.setStyleSheet("color:red ")
        self.fontx=QtGui.QFont()
        self.fontx.setFamily("Times")
        self.fontx.setPointSize(10)
        self.user_lable.setFont(self.fontx)
        

        self.icon_user_ent=QtWidgets.QPushButton(self.widget)
        self.icon_user_ent.setGeometry(QtCore.QRect(500,290,61,61))
        self.icon_user_ent.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.icon_user_ent.setEnabled(False)
        self.icon_user=QtGui.QIcon()
        self.icon_user.addPixmap(QtGui.QPixmap(":image/icons8-person-94.png"),QtGui.QIcon.Disabled)
        self.icon_user_ent.setIcon(self.icon_user)
        self.icon_user_ent.setIconSize(QtCore.QSize(100,70))

        self.pass_ent=QtWidgets.QLineEdit(self.widget)
        self.pass_ent.setGeometry(QtCore.QRect(570, 400, 371, 51))
        self.pass_ent.setStyleSheet("background-color:rgba(0,0,0,0) ; border:none ;border-Bottom:2px solid #aa55ff ; color:#ffffff")
        self.pass_ent.setFont(self.font)
        self.pass_ent.setPlaceholderText("Password")

        self.pass_lable=QtWidgets.QLabel(self.widget)
        self.pass_lable.setGeometry(QtCore.QRect(570, 460, 371, 20))
        self.pass_lable.setStyleSheet("color:red")
        self.pass_lable.setFont(self.fontx)

        self.icon_pass_ent=QtWidgets.QPushButton(self.widget)
        self.icon_pass_ent.setGeometry(QtCore.QRect(500,400,61,61))
        self.icon_pass_ent.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.icon_pass_ent.setEnabled(False)
        self.icon_pass=QtGui.QIcon()
        self.icon_pass.addPixmap(QtGui.QPixmap(":image/icons8-key-100") ,QtGui.QIcon.Disabled)
        self.icon_pass_ent.setIcon(self.icon_pass)
        self.icon_pass_ent.setIconSize(QtCore.QSize(100,70))



        self.email_ent=QtWidgets.QLineEdit(self.widget)
        self.email_ent.setGeometry(QtCore.QRect(570, 510, 371, 51))
        self.email_ent.setStyleSheet("background-color:rgba(0,0,0,0) ; border:none ;border-Bottom:2px solid #aa55ff ; color:#ffffff")
        self.email_ent.setFont(self.font)
        self.email_ent.setPlaceholderText("Email")

        self.email_lable=QtWidgets.QLabel(self.widget)
        self.email_lable.setGeometry(QtCore.QRect(570, 570, 371, 20))
        self.email_lable.setStyleSheet("color:red")
        self.email_lable.setFont(self.fontx)

        self.icon_email_ent=QtWidgets.QPushButton(self.widget)
        self.icon_email_ent.setGeometry(QtCore.QRect(500,510,61,61))
        self.icon_email_ent.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.icon_email_ent.setEnabled(False)
        self.icon_email=QtGui.QIcon()
        self.icon_email.addPixmap(QtGui.QPixmap(":image/icons8-email-60.png") ,QtGui.QIcon.Disabled)
        self.icon_email_ent.setIcon(self.icon_email)
        self.icon_email_ent.setIconSize(QtCore.QSize(100,70))

        self.singup_btn=QtWidgets.QPushButton(self.widget)
        self.singup_btn.setObjectName("singup_btn")
        self.singup_btn.setGeometry(QtCore.QRect(567, 620, 375, 71))
        self.singup_btn.setStyleSheet("background-color:rgb(78, 20, 125);color:#ffffff ; border-radius:15px")
        self.singup_btn.setShortcut("Enter")
        self.font.setPointSize(20)
        self.singup_btn.setFont(self.font)
        self.singup_btn.setText("Sing-Up")



        self.linkedin_btn=QtWidgets.QPushButton(self.widget)
        self.linkedin_btn.setObjectName("linkedin_btn")
        self.linkedin_btn.setGeometry(QtCore.QRect(610,700,51,41))
        self.icon2=QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap(":/image/linkedin.png"))
        self.linkedin_btn.setIcon(self.icon2)
        self.linkedin_btn.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.linkedin_btn.setIconSize(QtCore.QSize(100,50))


        self.git_btn=QtWidgets.QPushButton(self.widget)
        self.git_btn.setObjectName("git_btn")
        self.git_btn.setGeometry(QtCore.QRect(694,700,41,41))
        self.icon3=QtGui.QIcon()
        self.icon3.addPixmap(QtGui.QPixmap(":/image/github.png"))
        self.git_btn.setIcon(self.icon3)
        self.git_btn.setIconSize(QtCore.QSize(100,50))
        self.git_btn.setStyleSheet("background-color:rgba(0,0,0,0)")

        self.facebook_btn=QtWidgets.QPushButton(self.widget)
        self.facebook_btn.setObjectName("facebook_btn")
        self.facebook_btn.setGeometry(QtCore.QRect(770,700,41,41))
        self.icon4=QtGui.QIcon()
        self.icon4.addPixmap(QtGui.QPixmap(":/image/icons8-facebook-48.png"))
        self.facebook_btn.setIcon(self.icon4)
        self.facebook_btn.setIconSize(QtCore.QSize(100,50))
        self.facebook_btn.setStyleSheet("background-color:rgba(0,0,0,0)")

        self.web_btn=QtWidgets.QPushButton(self.widget)
        self.web_btn.setObjectName("web_btn")
        self.web_btn.setGeometry(QtCore.QRect(850,700,41,41))
        self.icon5=QtGui.QIcon()
        self.icon5.addPixmap(QtGui.QPixmap(":/image/icons8-website-96.png"))
        self.web_btn.setIcon(self.icon5)
        self.web_btn.setIconSize(QtCore.QSize(100,45))
        self.web_btn.setStyleSheet("background-color:rgba(0,0,0,0)")

        self.close_btn=QtWidgets.QPushButton(self.widget)
        self.close_btn.setObjectName("close_btn")
        self.close_btn.setGeometry(QtCore.QRect(950, 30, 41, 41))
        self.close_btn.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.icon=QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":/image/icons8-close-64.png"))
        self.close_btn.setIcon(self.icon)
        self.close_btn.setIconSize(QtCore.QSize(100,50))

        self.linkedin_btn.clicked.connect(lambda:self.open_web("linkedin"))
        self.git_btn.clicked.connect(lambda:self.open_web("git"))
        self.facebook_btn.clicked.connect(lambda:self.open_web("facebook"))
        self.web_btn.clicked.connect(lambda:self.open_web("web"))
        self.close_btn.clicked.connect(self.page1)
        self.shortcut()

    def shortcut(self):
        self.singup_btn.setShortcut("Return")
    def open_web(self,value):
        if  value == "git":
            webbrowser.open("https://github.com/matin0303")
        elif value == "linkedin":
            webbrowser.open("www.linkedin.com/in/matin-pirmohammadi-0733182b9")
        elif value == "facebook":
            pass
            #webbrowser.open("")
        elif value == "web":
            pass
            #webbrowser.open("")
    
    def page1(self):
        ui=mypage()
        Form1.addWidget(ui)
        Form1.setCurrentIndex(Form1.currentIndex()+1)
    def check_entry(self,user,pas,email):
    #for user 
        self.count_checking=0
        def checking_user_pass(input):
            self.count_checking+=1
            num="1234567890"
            a_z="abcdefghijklmnopqrstuvwxyz"
            have_num=False
            have_a_z=False
            self.userpass_checked=False
            for i in input:
                if i in num :
                    have_num = True
                    if self.count_checking == 1:
                        self.user_lable.setText("")
                    else:
                        self.pass_lable.setText("")


            for j in input:
                if j in a_z:
                    have_a_z=True
                    if self.count_checking == 1:
                        self.user_lable.setText("")
                    else:
                        self.pass_lable.setText("")


            if 8<=len(input)<=12 and have_num and have_a_z == True :
                self.userpass_checked=True
                if self.count_checking == 1:
                    self.user_lable.setText("")
                else:
                    self.pass_lable.setText("")
            else:
                if self.count_checking == 1:
                    if have_a_z == False:
                        self.user_lable.setText("Username must contain letters ")
                    elif have_num == False:
                        self.user_lable.setText("Username must contain numbers")
                    elif not 8<=len(input)<=12:
                        self.user_lable.setText("Username must contain 8 to 12 characters")


                else:
                    if have_a_z == False:
                        self.pass_lable.setText("Password must contain letters")
                    elif have_num == False:
                        self.pass_lable.setText("Password must contain numbers")
                    elif not 8<len(input)<12:
                        self.pass_lable.setText("Password must contain 8 to 12 characters")

        def checking_email(input):
            ok_email=["gmail.com","yahoo.com","email.com",]
            try:
                elem=input.split('@')
                self.email_checked=False
                if elem[1] in ok_email and len(elem[0])>6:
                    self.email_checked=True
                    self.email_lable.setText("")
                else:
                    self.email_lable.setText("The email is not valid")
            except:
                self.email_lable.setText("The email is not valid")
        checking_user_pass(user)  
        checking_user_pass(pas)
        checking_email(email)

        def check_exist(self,user,email):
            def check_userExists(input):
                cursor.execute(f'SELECT username FROM users WHERE username = "{input}"')
                exists_user=cursor.fetchone()
                self.user_notExists=False
                if exists_user == None:
                    self.user_notExists=True
                else:
                    self.user_lable.setStyleSheet("color:red")
                    self.user_lable.setText("This username has already been used")

            def check_emailExists(input):
                cursor.execute(f'SELECT email FROM users WHERE email = "{input}"')
                exists_user=cursor.fetchone()
                self.email_notExist=False
                if exists_user == None:
                    self.email_notExist=True
                else:
                    self.email_lable.setStyleSheet("color:red")
                    self.email_lable.setText("This email has already been used")
            
            check_userExists(user)
            check_emailExists(email)

            self.checkNotExists=False
            if self.email_notExist and self.user_notExists ==True:
                self.checkNotExists=True
    def singup_set_data(self):
        self.check_entry(self.user_ent.text(),self.pass_ent.text(),self.email_ent.text())
        self.check_exist(self.user_ent.text(),self.email_ent.text())
        if self.userpass_checked and self.email_checked and self.checkNotExists == True:
            cursor.execute(f'''INSERT INTO users(id,username,password,email)VALUES(
                        DEFAULT,
                        "{self.user_ent.text()}",
                        "{self.pass_ent.text()}",
                        "{self.email_ent.text()}")''')
            conn.commit()
            self.email_lable.setStyleSheet("color:green")
            self.email_lable.setText("Registration was successful")

            #create db for user
            cursor.execute(f'SELECT id FROM users WHERE username="{self.user_ent.text()}"')
            user_id = cursor.fetchone()
        else:
            pass

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    Form1=QtWidgets.QStackedWidget()
    Form1.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    Form1.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    Form1.setFixedSize(1097,799)
    ui=mypage()   
    Form1.addWidget(ui)
    Form1.show()
    app.exit(app.exec_())