
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import shutil
import res3
import sys

class main_page(QtWidgets.QDialog):
    def __init__(self):
        super(main_page,self).__init__()
        self.setObjectName("Form")
        self.resize(1173, 824)
        self.setMinimumSize(QtCore.QSize(1173, 824))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Halant")
        self.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)

        self.buttons_wgt = QtWidgets.QWidget(self)
        self.buttons_wgt.setMaximumSize(QtCore.QSize(270, 16777215))
        self.buttons_wgt.setMinimumSize(QtCore.QSize(270, 16777215))
        

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.buttons_wgt)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)

        self.createBTN_wgt = QtWidgets.QWidget(self.buttons_wgt)
        self.createBTN_wgt.setMinimumSize(QtCore.QSize(0, 60))
        self.createBTN_wgt.setMaximumSize(QtCore.QSize(16777215, 60))

        self.gridLayout = QtWidgets.QGridLayout(self.createBTN_wgt)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)

        self.create_btn = QtWidgets.QPushButton(self.createBTN_wgt)
        self.create_btn.setMaximumSize(QtCore.QSize(16777215, 60))

        self.create_btn.setText("Create Note")
        
        self.gridLayout.addWidget(self.create_btn, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.createBTN_wgt)

        self.notes_wgt = QtWidgets.QWidget(self.buttons_wgt)
        self.notes_wgt.setMinimumSize(QtCore.QSize(270, 0))


        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.notes_wgt)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)

        self.note_lb = QtWidgets.QLabel(self.notes_wgt)
        self.note_lb.setMinimumSize(QtCore.QSize(0, 50))
        self.note_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.note_lb.setText("Notes")
        self.verticalLayout_4.addWidget(self.note_lb)
        self.spacerItem = QtWidgets.QSpacerItem(20, 711, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(self.spacerItem)
        self.verticalLayout_3.addWidget(self.notes_wgt)
        self.horizontalLayout.addWidget(self.buttons_wgt)
        self.item_wgt = QtWidgets.QWidget(self)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.item_wgt)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        self.nav_wgt = QtWidgets.QWidget(self.item_wgt)
        self.nav_wgt.setMinimumSize(QtCore.QSize(0, 60))
        self.nav_wgt.setMaximumSize(QtCore.QSize(16666448, 60))

   
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.nav_wgt)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)

        self.logo_wgt = QtWidgets.QWidget(self.nav_wgt)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.logo_wgt)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        spacerItem1 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.logo_btn = QtWidgets.QPushButton(self.logo_wgt)
        self.logo_btn.setMinimumSize(QtCore.QSize(250, 60))
        self.logo_btn.setMaximumSize(QtCore.QSize(800, 60))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/logo.png"))
        self.logo_btn.setIcon(icon)
        self.logo_btn.setIconSize(QtCore.QSize(200, 200))
        self.logo_btn.setObjectName("logo_btn")
        self.logo_btn.setStyleSheet(".QPushButton{\n"
        "    background-color:transparent;\n"
        "    border:none;}")
        self.horizontalLayout_5.addWidget(self.logo_btn)
        spacerItem2 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.logo_wgt)
        self.widget_2 = QtWidgets.QWidget(self.nav_wgt)
        self.widget_2.setMinimumSize(QtCore.QSize(340, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(340, 16777215))

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)

        self.upload_wgt = QtWidgets.QWidget(self.widget_2)


        self.gridLayout_2 = QtWidgets.QGridLayout(self.upload_wgt)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
   
        self.upload_btn = QtWidgets.QPushButton(self.upload_wgt)
        self.upload_btn.setMaximumSize(QtCore.QSize(16777215, 70))

        self.upload_btn.setText("Upload")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/icons8-down-arrow-50.png"))
        self.upload_btn.setIcon(icon1)

        self.menu=QtWidgets.QMenu()
        self.image_menu_btn=QtWidgets.QAction("Image",self)
        self.noteFile_menu_btn=QtWidgets.QAction("Note",self)
        self.upload_btn.setMenu(self.menu)
        self.menu.addAction(self.image_menu_btn)
        self.menu.addAction(self.noteFile_menu_btn)
        self.menu.setFixedWidth(112)

        self.gridLayout_2.addWidget(self.upload_btn, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.upload_wgt)
        self.del_wgt = QtWidgets.QWidget(self.widget_2)


        self.gridLayout_3 = QtWidgets.QGridLayout(self.del_wgt)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.del_btn = QtWidgets.QPushButton(self.del_wgt)
        self.del_btn.setMaximumSize(QtCore.QSize(16777215, 70))
        self.del_btn.setText("Delete")

        self.gridLayout_3.addWidget(self.del_btn, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.del_wgt)
        self.save_wgt = QtWidgets.QWidget(self.widget_2)

        self.gridLayout_4 = QtWidgets.QGridLayout(self.save_wgt)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)

        self.save_btn = QtWidgets.QPushButton(self.save_wgt)
        self.save_btn.setMaximumSize(QtCore.QSize(16777215, 70))
        self.save_btn.setText("Save")

        self.gridLayout_4.addWidget(self.save_btn, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.save_wgt)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.nav_wgt)
        self.body_wgt = QtWidgets.QWidget(self.item_wgt)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body_wgt)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.texts_wgt = QtWidgets.QWidget(self.body_wgt)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.texts_wgt)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)

        self.lineEdit_wgt = QtWidgets.QWidget(self.texts_wgt)
        self.lineEdit_wgt.setMinimumSize(QtCore.QSize(563, 382))
        self.lineEdit_wgt.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.gridLayout_5 = QtWidgets.QGridLayout(self.lineEdit_wgt)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 1)
        self.gridLayout_5.setSpacing(0)

        self.textEdit1 = QtWidgets.QTextEdit(self.lineEdit_wgt)
        self.textEdit1.setDisabled(True)
        self.textEdit1.setFont(font)
        self.textEdit1.setPlaceholderText("Note")
        self.textEdit1.setStyleSheet("background-color:transparent;border:none;\n"
        "padding-left:20px;\n"
        "padding-top:20px;\n"
        "font-size:20px;")
        self.gridLayout_5.addWidget(self.textEdit1, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.lineEdit_wgt)
        self.lineEdit2_wgt = QtWidgets.QWidget(self.texts_wgt)
        self.lineEdit2_wgt.setMinimumSize(QtCore.QSize(563, 382))


        self.gridLayout_6 = QtWidgets.QGridLayout(self.lineEdit2_wgt)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)

        self.textEdit2 = QtWidgets.QTextEdit(self.lineEdit2_wgt)
        self.textEdit2.setDisabled(True)
        self.textEdit2.setPlaceholderText("Upload Note File")
        self.textEdit2.setStyleSheet("background-color:transparent;border:none;\n"
        "padding-left:20px;\n"
        "padding-top:20px;\n"
        "font-size:20px;")


        self.gridLayout_6.addWidget(self.textEdit2, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.lineEdit2_wgt)
        self.horizontalLayout_2.addWidget(self.texts_wgt)
        self.image_wgt = QtWidgets.QWidget(self.body_wgt)
        self.image_wgt.setMinimumSize(QtCore.QSize(340, 0))
        self.image_wgt.setMaximumSize(QtCore.QSize(340, 16777215))

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.image_wgt)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)

        self.image_lb = QtWidgets.QLabel(self.image_wgt)
        self.image_lb.setMinimumSize(QtCore.QSize(0, 50))
        self.image_lb.setFont(font)
        self.image_lb.setText("Images")
        self.image_lb.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.image_lb)
        self.spacerItem3 = QtWidgets.QSpacerItem(20, 711, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(self.spacerItem3)
        self.horizontalLayout_2.addWidget(self.image_wgt)
        self.verticalLayout.addWidget(self.body_wgt)
        self.horizontalLayout.addWidget(self.item_wgt)
        self.logo_btn.clicked.connect(self.theme)

        self.next_theme="light"
        self.note_btn=QtWidgets.QPushButton()
        self.image_btn=QtWidgets.QPushButton()
        #for create note def
        self.note_num=1
        self.noteBTN_list=[]#for btn codes
        self.senderBTN_list=[]#for change style when clicked
        self.btns_height=0

    def resizeEvent(self, event):
        self.scroll.setFixedHeight(self.height()-70)

    def add_scroll(self):
        if self.btns_height>self.height() - 70:
            self.scroll.setHidden(False)
            self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.scroll.setWidgetResizable(True)
            self.scroll.setFixedHeight(self.height()-70)
            self.scroll.setWidget(self.notes_wgt)
        else:
            self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    def create_note(self):
        self.verticalLayout_4.removeItem(self.spacerItem)
        self.note_btn=QtWidgets.QPushButton(f"Note {self.note_num}",self)
        self.note_btn.setObjectName(f"{self.note_btn}")
        self.note_btn.setFixedHeight(70)
        if self.next_theme=="dark":
            self.note_btn.setStyleSheet(".QPushButton{background-color:transparent;border: 1px solid rgb(230, 230, 230)} \n"
                                        "::hover{background-color: rgb(230, 230, 230)}")
        else:
            self.note_btn.setStyleSheet(".QPushButton{background-color:transparent;border: 1px solid rgba(42, 41, 41, 1)} \n"
                            "::hover{background-color: rgba(42, 41, 41, 1)}")
        self.verticalLayout_4.addWidget(self.note_btn)
        self.btns_height+=70
        self.note_num+=1
        self.noteBTN_list.append(self.note_btn.objectName())
        self.senderBTN_list.append(self.note_btn)
        self.note_btn.clicked.connect(self.click)
        self.verticalLayout_4.addItem(self.spacerItem)
    
    def click(self):
        #for set buttons bg transparent:
        for i in self.senderBTN_list:
            if self.next_theme=="dark":
                i.setStyleSheet("background-color:transparent;\n"
                    "border: 1px solid rgb(230, 230, 230)")
            else:
                i.setStyleSheet("background-color:transparent;\n"
                    "border: 1px solid rgba(42, 41, 41, 1)")
        #btn code
        self.item_code=self.notes_wgt.sender()
        self.selected_btn_now=self.item_code
        #for change selected btn bg
        if self.next_theme=="dark":
            self.item_code.setStyleSheet("background-color:rgb(217, 217, 217);border: 1px solid rgb(230, 230, 230)")
        else:
            self.item_code.setStyleSheet("background-color:rgba(42, 41, 41, 1);border: 1px solid rgba(42, 41, 41, 1)")
        
        #btn index+1 in list
        self.note_number=int(self.senderBTN_list.index(self.item_code))+1
        #for line edit 
        self.textEdit1.setPlaceholderText(f"Note {self.note_number}")
        self.textEdit1.setText("")
        self.textEdit1.setDisabled(False)
        self.textEdit2.setDisabled(False)
        self.note_selected=True
        self.textEdit2.setText("")
        print(self.note_number)
    def delete_note(self):
        try:
            self.btn_selected=self.senderBTN_list[(self.note_number)-1] #(self.note_number)-1 is btn index in list
            self.btn_selected.setHidden(True)
            #self.noteBTN_list.pop((self.note_number)-1) #for delete btn code from list
            self.textEdit1.setPlaceholderText(f"Note")
            self.btns_height-=70
            self.add_scroll()
            self.note_selected=False
            self.textEdit1.setText("")
            self.textEdit2.setText("")
            self.textEdit1.setDisabled(True)
            self.textEdit2.setDisabled(True)
        except:
            print("select note")
    def theme(self):
        if self.next_theme=="dark":
            self.setStyleSheet("*{\n"
                        "    font-family:Halant;\n"
                        "    font-size:16px;\n"
                        "    color:white;\n"
                        "}\n"
                        ".QWidget{\n"
                        "    \n"
                        "    background-color: rgba(66, 66, 66, 1);\n"
                        "}")
            self.createBTN_wgt.setStyleSheet("border-right:1px solid rgba(36, 33, 33, 1);\n"
            "border-bottom:1px solid rgba(36, 33, 33, 1);")
            
            self.notes_wgt.setStyleSheet("border-right:1px solid rgba(36, 33, 33, 1);")

            self.nav_wgt.setStyleSheet("border-bottom:1px solid rgba(36, 33, 33, 1);")

            self.upload_wgt.setStyleSheet("border-left:1px solid rgba(36, 33, 33, 1);")

            self.del_wgt.setStyleSheet("border-left:1px solid rgba(36, 33, 33, 1);")

            self.save_wgt.setStyleSheet("border-left:0.5px solid rgba(36, 33, 33, 1);")

            self.lineEdit_wgt.setStyleSheet("border-bottom:1px solid rgba(36, 33, 33, 1);")

            self.image_wgt.setStyleSheet("border-left:1px solid rgba(36, 33, 33, 1);")

            self.menu.setStyleSheet(".QMenu{\n"
                                "background-color:rgba(66, 66, 66, 1)}\n"
                                "::item::selected{ \n"
                                "background-color:rgba(66, 66, 66, 1)}\n"
                                "::item{ \n"
                                "padding:10px;border-top:1px solid white;color:white}\n"
                                "::drop-down{\n"
                                "border:none}")
            
            #______________HOVER
            self.create_btn.setStyleSheet(".QPushButton{\n"
                                        "    background-color:transparent;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "::pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "}\n"
                                        "::hover{\n"
                                        "    background-color: rgba(42, 41, 41, 1);\n"
                                        "}\n"
                                        "")
            
            self.upload_btn.setStyleSheet(".QPushButton{\n"
                                        "    background-color:transparent;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "::pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "}\n"
                                        "::hover{\n"
                                        "    background-color: rgba(42, 41, 41, 1);\n"
                                        "}\n"
                                        "")
            self.del_btn.setStyleSheet(".QPushButton{\n"
                                        "    background-color:transparent;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "::pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "}\n"
                                        "::hover{\n"
                                        "    background-color: rgba(42, 41, 41, 1);\n"
                                        "}\n"
                                        "")
            self.save_btn.setStyleSheet(".QPushButton{\n"
                                        "    background-color:transparent;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "::pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "}\n"
                                        "::hover{\n"
                                        "    background-color: rgba(42, 41, 41, 1);\n}")
            self.note_btn.setStyleSheet(".QPushButton{background-color:transparent;border: 1px solid rgba(42, 41, 41, 1)} \n"
                            "::hover{background-color: rgba(42, 41, 41, 1)}")
            self.image_btn.setStyleSheet(".QPushButton{background-color:transparent;border: 1px solid rgba(42, 41, 41, 1);} \n"
                                        "::hover{background-color: rgba(42, 41, 41, 1)}")

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("dark logo.png"))
            self.logo_btn.setIcon(icon)

            for i in self.senderBTN_list:
                    i.setStyleSheet("background-color:transparent;\n"
                        "border: 1px solid rgba(42, 41, 41, 1)")
            try:
                self.selected_btn_now.setStyleSheet("background-color:rgba(42, 41, 41, 1);border: 1px solid rgba(42, 41, 41, 1)")
            except:
                pass
            self.next_theme="light"
        else:
            self.setStyleSheet("*{\n"
                        "    font-family:Halant;\n"
                        "    font-size:16px;\n"
                        "    color:black;\n"
                        "}\n"
                        ".QWidget{\n"
                        "    \n"
                        "    background-color: #ffffff;\n"
                        "}")
            self.createBTN_wgt.setStyleSheet("border-right:1px solid rgb(217, 217, 217);\n"
            "border-bottom:1px solid rgb(217, 217, 217);")
            
            self.notes_wgt.setStyleSheet("border-right:1px solid rgb(217, 217, 217);")

            self.nav_wgt.setStyleSheet("border-bottom:1px solid rgb(217, 217, 217);")

            self.upload_wgt.setStyleSheet("border-left:1px solid rgb(217, 217, 217);")

            self.del_wgt.setStyleSheet("border-left:1px solid rgb(217, 217, 217);")

            self.save_wgt.setStyleSheet("border-left:0.5px solid rgb(217, 217, 217);")

            self.lineEdit_wgt.setStyleSheet("border-bottom:1px solid rgb(217, 217, 217);")

            self.image_wgt.setStyleSheet("border-left:1px solid rgb(217, 217, 217);")
            
            self.menu.setStyleSheet(".QMenu{\n"
                                "background-color:white}\n"
                                "::item::selected{ \n"
                                "background-color:rgb(217, 217, 217)}\n"
                                "::item{ \n"
                                "padding:10px;border-top:1px solid black}\n"
                                "::drop-down{\n"
                                "border:none}")
            

                        #______________HOVER
            self.create_btn.setStyleSheet(".QPushButton{\n"
                                        "    background-color:transparent;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "::pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "}\n"
                                        "::hover{\n"
                                        "    background-color: rgb(230, 230, 230);\n"
                                        "}\n"
                                        "")
            self.upload_btn.setStyleSheet(".QPushButton{\n"
                                        "    background-color:transparent;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "::pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "}\n"
                                        "::hover{\n"
                                        "    background-color: rgb(230, 230, 230);\n"
                                        "}\n"
                                        "")

            self.del_btn.setStyleSheet(".QPushButton{\n"
                                    "    background-color:transparent;\n"
                                    "    border:none;\n"
                                    "}\n"
                                    "::pressed{\n"
                                    "    padding-left:5px;\n"
                                    "    padding-top:5px;\n"
                                    "}\n"
                                    "::hover{\n"
                                    "    background-color: rgb(230, 230, 230);\n"
                                    "}\n"
                                    "")
            self.save_btn.setStyleSheet(".QPushButton{\n"
                                    "    background-color:transparent;\n"
                                    "    border:none;\n"
                                    "}\n"
                                    "::pressed{\n"
                                    "    padding-left:5px;\n"
                                    "    padding-top:5px;\n"
                                    "}\n"
                                    "::hover{\n"
                                    "    background-color: rgb(230, 230, 230);\n"
                                    "}\n")
            self.note_btn.setStyleSheet(".QPushButton{background-color:transparent;border: 1px solid rgb(230, 230, 230)} \n"
                            "::hover{background-color: rgb(230, 230, 230)}")
            self.image_btn.setStyleSheet(".QPushButton{background-color:transparent;border: 1px solid rgb(230, 230, 230);} \n"
                                        "::hover{background-color: rgb(230, 230, 230)}")
            
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/image/logo.png"))
            self.logo_btn.setIcon(icon)
            for i in self.senderBTN_list:
                i.setStyleSheet("background-color:transparent;\n"
                    "border: 1px solid rgb(230, 230, 230)")
            try:
                self.selected_btn_now.setStyleSheet("background-color:rgb(217, 217, 217);border: 1px solid rgb(230, 230, 230)")
            except:
                pass
            self.next_theme="dark"

    def upload_img(self):
        self.image_num+=1
        self.copy_img()
        if self.image_num <= 10 and self.selected==True and self.note_selected==True :        
            self.verticalLayout_5.removeItem(self.spacerItem3)
            self.image_btn=QtWidgets.QPushButton(f'{self.image_name[-1]}',self.image_wgt)
            self.image_btn.installEventFilter(self)
            self.image_btn.setFixedHeight(70)
            if self.next_theme=="dark":
                self.image_btn.setStyleSheet(".QPushButton{background-color:transparent;border: 1px solid rgb(230, 230, 230)} \n"
                                            "::hover{background-color: rgb(230, 230, 230)}")
            else:
                self.image_btn.setStyleSheet(".QPushButton{background-color:transparent;border: 1px solid rgba(42, 41, 41, 1)} \n"
                                "::hover{background-color: rgba(42, 41, 41, 1)}")
    
            self.image_local[self.image_btn]=self.hide_file_url_for_image #add btn code and image url in dict
            self.image_btn.clicked.connect(self.open_img)
            self.verticalLayout_5.addWidget(self.image_btn)
            self.verticalLayout_5.addItem(self.spacerItem3)
        else:
            print("select a notes")
    def copy_img(self):
        self.dialog=QtWidgets.QFileDialog(self.image_wgt,"Upload Image",r"","*.png")
        self.dialog.exec_()
        self.urls=self.dialog.selectedUrls()
        try:
            self.image_url=self.urls[0].toLocalFile()
            self.image_name=self.image_url.split('/')
            self.hide_file_url_for_image=f'.images\\{self.image_name[-1]}.png'
            shutil.copyfile(self.image_url ,self.hide_file_url_for_image )
            self.selected=True 
        except:
            self.selected=False 

    def open_img(self):
        self.image_code=self.image_wgt.sender()
        for i in self.image_local.keys():
            if i == self.image_code :
                image=Image.open(self.image_local[i])
                image.show()
                break
            else:
                pass
    def eventFilter(self,source,event):
        def delete_image():
            self.image_code.hide()
        if event.type()==QtCore.QEvent.ContextMenu :
            self.deleteMenu = QtWidgets.QMenu()
            self.deleteMenu.addAction("Delete")
            self.image_code=source# it's .sender() code
            self.deleteMenu.triggered.connect(delete_image)
            self.deleteMenu.exec_(event.globalPos())
        return super().eventFilter(source,event)
    
    def upload_text(self):
        if self.note_selected==True :
            dialog2=QtWidgets.QFileDialog()
            dialog2.setFileMode(QtWidgets.QFileDialog.AnyFile)
            dialog2.setFilter(QtCore.QDir.Files)
            if dialog2.exec_():
                filename=dialog2.selectedFiles()
                try:
                    with open(filename[0],"r") as f:
                        date=f.read()
                        self.textEdit2.setText(date)
                        f.close()
                except:
                    print("can't open file")
        else:
            print("select a note")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form=QtWidgets.QStackedWidget()
    ui = main_page()
    Form.addWidget(ui)
    Form.show()
    sys.exit(app.exec_())