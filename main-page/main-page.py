
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form=QtWidgets.QStackedWidget()
    ui = main_page()
    Form.addWidget(ui)
    Form.show()
    sys.exit(app.exec_())