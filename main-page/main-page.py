
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
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form=QtWidgets.QStackedWidget()
    ui = main_page()
    Form.addWidget(ui)
    Form.show()
    sys.exit(app.exec_())