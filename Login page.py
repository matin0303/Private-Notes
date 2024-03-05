from PyQt5 import QtGui ,QtCore , QtWidgets
import sys
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
                                 "QPushButton#insta_btn:pressed{\n"
                                 "padding-left:5px;padding-top:5px} \n"
                                 "QPushButton#tel_btn:pressed{\n"
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
        self.font.setFamily("Cooper Black")
        self.font.setPointSize(25)
        self.new_ex_lable.setFont(self.font)

        self.create_lable=QtWidgets.QLabel(self.widget)
        self.create_lable.setGeometry(QtCore.QRect(610, 570, 300, 100))
        self.create_lable.setStyleSheet("color:#ffffff")
        self.create_lable.setText("Don’t have an account?")
        self.font=QtGui.QFont()
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


        self.tel_btn=QtWidgets.QPushButton(self.widget)
        self.tel_btn.setObjectName("tel_btn")
        self.tel_btn.setGeometry(QtCore.QRect(610,660,51,41))
        self.icon2=QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap(":/image/icons8-telegram-48.png"))
        self.tel_btn.setIcon(self.icon2)
        self.tel_btn.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.tel_btn.setIconSize(QtCore.QSize(100,50))


        self.insta_btn=QtWidgets.QPushButton(self.widget)
        self.insta_btn.setObjectName("insta_btn")
        self.insta_btn.setGeometry(QtCore.QRect(694,660,41,41))
        self.icon3=QtGui.QIcon()
        self.icon3.addPixmap(QtGui.QPixmap(":/image/icons8-instagram-48.png"))
        self.insta_btn.setIcon(self.icon3)
        self.insta_btn.setIconSize(QtCore.QSize(100,50))
        self.insta_btn.setStyleSheet("background-color:rgba(0,0,0,0)")

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