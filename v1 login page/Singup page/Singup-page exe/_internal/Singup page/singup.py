from PyQt5 import QtGui ,QtCore , QtWidgets
import sys
import res2
import webbrowser


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

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    Form1=QtWidgets.QStackedWidget()
    Form1.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    Form1.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    Form1.setFixedSize(1097,799)
    ui=singup()   
    Form1.addWidget(ui)
    Form1.show()
    app.exit(app.exec_())
