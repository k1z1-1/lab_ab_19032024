from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import reg
import vxod
import otpravka
import bd
import shifrsa
import shifdiff
import shifcaes



class Ui_MainWindow(object):





    def setupUi(self, MainWindow):

        self.flag = -1
        self.who = 0
        self.kod = 0
        self.textlog = ""
        self.textpas = ""
        self.textkey = ""
        self.N = 0
        self.Y = 0


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 371)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.tabWidget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Text_log = QtWidgets.QPlainTextEdit(self.tab)
        self.Text_log.setGeometry(QtCore.QRect(239, 70, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Text_log.setFont(font)
        self.Text_log.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Text_log.setObjectName("Text_log")

        self.Text_key = QtWidgets.QPlainTextEdit(self.tab)
        self.Text_key.setGeometry(QtCore.QRect(130, 220, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Text_key.setFont(font)
        self.Text_key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Text_key.setObjectName("Text_key")

        self.Text_pas = QtWidgets.QPlainTextEdit(self.tab)
        self.Text_pas.setGeometry(QtCore.QRect(240, 150, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Text_pas.setFont(font)
        self.Text_pas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Text_pas.setPlainText("")
        self.Text_pas.setObjectName("Text_pas")
        self.lb_vxod = QtWidgets.QLabel(self.tab)
        self.lb_vxod.setGeometry(QtCore.QRect(270, 10, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_vxod.setFont(font)
        self.lb_vxod.setObjectName("lb_vxod")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(150, 80, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(150, 160, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.bt_vxod = QtWidgets.QPushButton(self.tab)
        self.bt_vxod.setGeometry(QtCore.QRect(270, 220, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bt_vxod.setFont(font)
        self.bt_vxod.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_vxod.setObjectName("bt_vxod")
        self.lb_Cap = QtWidgets.QLabel(self.tab)
        self.lb_Cap.setGeometry(QtCore.QRect(0, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_Cap.setFont(font)
        self.lb_Cap.setObjectName("lb_Cap")
        self.bt_dev_vx = QtWidgets.QPushButton(self.tab)
        self.bt_dev_vx.setGeometry(QtCore.QRect(20, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bt_dev_vx.setFont(font)
        self.bt_dev_vx.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_dev_vx.setObjectName("bt_dev_vx")
        self.bt_dev_reg = QtWidgets.QPushButton(self.tab)
        self.bt_dev_reg.setGeometry(QtCore.QRect(20, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bt_dev_reg.setFont(font)
        self.bt_dev_reg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_dev_reg.setObjectName("bt_dev_reg")
        self.bt_dev_r = QtWidgets.QPushButton(self.tab)
        self.bt_dev_r.setGeometry(QtCore.QRect(20, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bt_dev_r.setFont(font)
        self.bt_dev_r.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_dev_r.setObjectName("bt_dev_r")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(230, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Text_pas_reg = QtWidgets.QPlainTextEdit(self.tab_2)
        self.Text_pas_reg.setGeometry(QtCore.QRect(220, 120, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Text_pas_reg.setFont(font)
        self.Text_pas_reg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Text_pas_reg.setObjectName("Text_pas_reg")
        self.Text_log_reg = QtWidgets.QPlainTextEdit(self.tab_2)
        self.Text_log_reg.setGeometry(QtCore.QRect(220, 50, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Text_log_reg.setFont(font)
        self.Text_log_reg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Text_log_reg.setObjectName("Text_log_reg")
        self.bt_reg = QtWidgets.QPushButton(self.tab_2)
        self.bt_reg.setGeometry(QtCore.QRect(220, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bt_reg.setFont(font)
        self.bt_reg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_reg.setObjectName("bt_reg")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(130, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(0, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.btgiga = QtWidgets.QPushButton(self.tab_2)
        self.btgiga.setGeometry(QtCore.QRect(10, 70, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btgiga.setFont(font)
        self.btgiga.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btgiga.setObjectName("btgiga")
        self.btrab = QtWidgets.QPushButton(self.tab_2)
        self.btrab.setGeometry(QtCore.QRect(10, 130, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btrab.setFont(font)
        self.btrab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btrab.setObjectName("btrab")
        self.btchep = QtWidgets.QPushButton(self.tab_2)
        self.btchep.setGeometry(QtCore.QRect(10, 190, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btchep.setFont(font)
        self.btchep.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btchep.setObjectName("btchep")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(11, 101, 91, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(0, 160, 181, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(0, 220, 111, 20))
        self.label_12.setObjectName("label_12")
        self.bt_q_log = QtWidgets.QPushButton(self.tab_2)
        self.bt_q_log.setGeometry(QtCore.QRect(190, 90, 21, 28))
        self.bt_q_log.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_q_log.setObjectName("bt_q_log")
        self.bt_q_pas = QtWidgets.QPushButton(self.tab_2)
        self.bt_q_pas.setGeometry(QtCore.QRect(190, 160, 21, 28))
        self.bt_q_pas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_q_pas.setObjectName("bt_q_pas")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(160, 210, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.Text_kod = QtWidgets.QPlainTextEdit(self.tab_2)
        self.Text_kod.setGeometry(QtCore.QRect(150, 240, 101, 31))
        self.Text_kod.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Text_kod.setObjectName("Text_kod")
        self.bt_got = QtWidgets.QPushButton(self.tab_2)
        self.bt_got.setGeometry(QtCore.QRect(270, 240, 93, 28))
        self.bt_got.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_got.setObjectName("bt_got")
        self.bt_q_got = QtWidgets.QPushButton(self.tab_2)
        self.bt_q_got.setGeometry(QtCore.QRect(370, 240, 21, 28))
        self.bt_q_got.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_q_got.setObjectName("bt_q_got")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.bt_giga_s = QtWidgets.QPushButton(self.tab_3)
        self.bt_giga_s.setGeometry(QtCore.QRect(110, 50, 181, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bt_giga_s.setFont(font)
        self.bt_giga_s.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.bt_giga_s.setObjectName("bt_giga_s")
        self.bt_rab_s = QtWidgets.QPushButton(self.tab_3)
        self.bt_rab_s.setGeometry(QtCore.QRect(10, 130, 61, 61))
        self.bt_rab_s.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.bt_rab_s.setObjectName("bt_rab_s")
        self.bt_chep_s = QtWidgets.QPushButton(self.tab_3)
        self.bt_chep_s.setGeometry(QtCore.QRect(310, 160, 71, 31))
        self.bt_chep_s.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.bt_chep_s.setObjectName("bt_chep_s")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(0, 100, 81, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(110, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(310, 130, 71, 20))
        self.label_9.setObjectName("label_9")
        self.lb_who = QtWidgets.QLabel(self.tab_3)
        self.lb_who.setGeometry(QtCore.QRect(120, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(12)
        self.lb_who.setFont(font)
        self.lb_who.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 0, 0);")
        self.lb_who.setText("")
        self.lb_who.setObjectName("lb_who")
        self.tabWidget.addTab(self.tab_3, "")
        self.lb_error = QtWidgets.QLabel(self.centralwidget)
        self.lb_error.setGeometry(QtCore.QRect(0, 299, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_error.setFont(font)
        self.lb_error.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.lb_error.setText("")
        self.lb_error.setObjectName("lb_error")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.add_functions()




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_error.setText(_translate("MainWindow", "Выберите действие"))
        self.lb_vxod.setText(_translate("MainWindow", "Вход:"))
        self.label_3.setText(_translate("MainWindow", "Логин:"))
        self.label_4.setText(_translate("MainWindow", "Пароль:"))
        self.bt_vxod.setText(_translate("MainWindow", "Войти"))
        self.lb_Cap.setText(_translate("MainWindow", "Выберите действие:"))
        self.bt_dev_vx.setText(_translate("MainWindow", "Вход"))
        self.bt_dev_reg.setText(_translate("MainWindow", "Регистрация"))
        self.bt_dev_r.setText(_translate("MainWindow", "Начать заново"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Вход"))
        self.label.setText(_translate("MainWindow", "Регистрация:"))
        self.bt_reg.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.label_2.setText(_translate("MainWindow", "Логин:"))
        self.label_5.setText(_translate("MainWindow", "Пароль:"))
        self.label_6.setText(_translate("MainWindow", "Выберите  роль:"))
        self.btgiga.setText(_translate("MainWindow", "Глава"))
        self.btrab.setText(_translate("MainWindow", "Работник"))
        self.btchep.setText(_translate("MainWindow", "Юзер"))
        self.label_10.setText(_translate("MainWindow", "Шифровка Rsa"))
        self.label_11.setText(_translate("MainWindow", "Шифровка Эль-Гамаля"))
        self.label_12.setText(_translate("MainWindow", "Шифровка Цезарь"))
        self.bt_q_log.setText(_translate("MainWindow", "?"))
        self.bt_q_pas.setText(_translate("MainWindow", "?"))
        self.label_13.setText(_translate("MainWindow", "Введите код подтверждения"))
        self.bt_got.setText(_translate("MainWindow", "Готово"))
        self.bt_q_got.setText(_translate("MainWindow", "?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Зарегистрироваться"))
        self.bt_giga_s.setText(_translate("MainWindow", "Сюрприз"))
        self.bt_rab_s.setText(_translate("MainWindow", "Сюрприз"))
        self.bt_chep_s.setText(_translate("MainWindow", "Сюрприз"))
        self.label_7.setText(_translate("MainWindow", "Для работников"))
        self.label_8.setText(_translate("MainWindow", "ДЛЯ Главы"))
        self.label_9.setText(_translate("MainWindow", "Для Юзера"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Защищенный объект"))

        self.flag = 0

    def q(self, num):
        if num == 1:
            error = QMessageBox()
            error.setWindowTitle("Подсказка")
            error.setText("Вводите почту @mail.ru или @gmail.com, остальные появятся позже")
            error.setIcon(QMessageBox.Information)
            error.setStandardButtons(QMessageBox.Ok)

            error.exec_()
        elif num == 2:
            error2 = QMessageBox()
            error2.setWindowTitle("Подсказка")
            error2.setText("Доступные спец. символы ~, !, @, #, $, %, ^, &, *, <, >, -, _, ., ,, :, ;, (, ), ?, ', /")
            error2.setIcon(QMessageBox.Information)
            error2.setStandardButtons(QMessageBox.Ok)

            error2.exec_()
        elif num == 3:
            error3 = QMessageBox()
            error3.setWindowTitle("Подсказка")
            error3.setText("Код пришел вам на почту, проверте ее, если не пришел начните заново и вводите данные внимательнее")
            error3.setIcon(QMessageBox.Information)
            error3.setStandardButtons(QMessageBox.Ok)

            error3.exec_()


    def surprise(self, num):
        if self.flag == 6:
            if self.who2 == 1:
                self.lb_who.setText("Ты Глава")
                if num == 1:
                    self.lb_error.setText("Ты крутая вафля, спасибо за участие")
                else:
                    self.lb_error.setText("Выбери свой сюрприз!")
            elif self.who2 == 2:
                self.lb_who.setText("Ты работник")
                if num == 2:
                    self.lb_error.setText("Ты обычная вафля, спасибо за участие")
                else:
                    self.lb_error.setText("Выбери свой сюрприз!")
            elif self.who2 == 2:
                self.lb_who.setText("Ты Юзер")
                if num == 2:
                    self.lb_error.setText("Ты покусаная вафля, спасибо за участие")
                else:
                    self.lb_error.setText("Выбери свой сюрприз!")







    def gotov(self):
        if self.flag == 4:
            text_gotov = self.Text_kod.toPlainText()
            if text_gotov == str(self.kod):

                if self.who == 1:
                    tl = self.textlog
                    self.textlog, self.textpas, self.Y, self.N = shifrsa.sRsa(self.textlog, self.textpas)
                    self.lb_error.setText("Вы зарегистрировались как Глава. На почте код для входа")
                    self.kod = int(otpravka.snd_kod(tl, self.Y))
                    bd.base(int(self.who), str(self.textlog), str(self.textpas), int(self.Y), int(self.N))
                    self.flag = 5
                elif self.who == 2:
                    tl = self.textlog
                    self.textlog, self.textpas, self.Y, self.N = shifdiff.sDif(self.textlog, self.textpas)
                    self.lb_error.setText("Вы зарегистрировались как работник. На почте код для входа")
                    self.kod = int(otpravka.snd_kod(tl, self.Y))
                    bd.base(int(self.who), str(self.textlog), str(self.textpas), int(self.Y), int(self.N))
                    self.flag = 5
                elif self.who == 3:
                    tl = self.textlog
                    self.textlog, self.textpas, self.Y, self.N = shifcaes.sCea(self.textlog, self.textpas)
                    self.lb_error.setText("Вы зарегистрировались как юзер. На почте код для входа")
                    self.kod = int(otpravka.snd_kod(tl, self.Y))
                    bd.base(int(self.who), str(self.textlog), str(self.textpas), int(self.Y), int(self.N))
                    self.flag = 5

            else:
                self.lb_error.setText("Код неверный, повторите попытку или начните заново")


    def regist(self):
        if self.flag == 3:
            #bd.base(1,"2","3",4,5)

            text_log = self.Text_log_reg.toPlainText()
            text_pas = self.Text_pas_reg.toPlainText()


            #self.textlog, self.textpas, self.Y, self.N = shifrsa.sRsa(text_log, text_pas)


            #self.textlog, self.textpas = shifrsa.dRsa(text_log, text_pas, self.Y, self.N)



            proverka = int(reg.rg(text_log, text_pas))
            if proverka == 1:
                self.lb_error.setText("Логин введен неверно")
            elif proverka == 2:
                self.lb_error.setText("Недопустимый пароль, добавьте большие буквы")
            elif proverka == 3:
                self.lb_error.setText("Недопустимый пароль, добавьте маленькие буквы")
            elif proverka == 4:
                self.lb_error.setText("Недопустимый пароль, добавьте цифры")
            elif proverka == 5:
                self.lb_error.setText("Недопустимый пароль, добавьте спец. символы")
            elif proverka == 6:
                self.lb_error.setText("На вашей почте код подтверждения, введите его")
                self.kod = int(otpravka.snd(text_log))
                self.textpas = text_pas
                self.textlog = text_log
                self.flag = 4


    def who_u(self, n):
        if self.flag == 2:

            if n == 1:
                self.who = 1
                self.flag = 3
                self.lb_error.setText("Введите логин и пароль в поля регистрации")
            elif n == 2:
                self.who = 2
                self.flag = 3
                self.lb_error.setText("Введите логин и пароль в поля регистрации")
            elif n == 3:
                self.who = 3
                self.flag = 3
                self.lb_error.setText("Введите логин и пароль в поля регистрации")

    def vxo(self):
        if self.flag == 1:
            text_log = self.Text_log.toPlainText()
            text_pas = self.Text_pas.toPlainText()
            text_key = self.Text_key.toPlainText()
            self.textlog = text_log
            self.textpas = text_pas
            self.textkey = int(text_key)
            n, self.textkey = bd.base2(self.textkey)
            if n == 1:
                self.who2, self.textlog2, self.textpas2, self.Y2, self.N2 = bd.base3(self.textkey)
                if self.who2 == 1:
                    self.textlog, self.textpas = shifrsa.dRsa(self.textlog, self.textpas, self.Y2, self.N2)
                    if (self.textlog == self.textlog2) and (self.textpas == self.textpas2):
                        self.lb_error.setText("Вы успешно вошли в аккаунт")
                        self.flag = 6
                    else:
                        self.lb_error.setText("Данные введены неверно, за помощью к админу")
                elif self.who2 == 2:
                    self.textlog, self.textpas = shifdiff.dDif(self.textlog, self.textpas, self.Y2, self.N2)
                    if (self.textlog == self.textlog2) and (self.textpas == self.textpas2):
                        self.lb_error.setText("Вы успешно вошли в аккаунт")
                        self.flag = 6
                    else:
                        self.lb_error.setText("Данные введены неверно, за помощью к админу")
                elif self.who2 == 3:
                    self.textlog, self.textpas = shifcaes.dCea(self.textlog, self.textpas, self.Y2)
                    if (self.textlog == self.textlog2) and (self.textpas == self.textpas2):
                        self.lb_error.setText("Вы успешно вошли в аккаунт")
                        self.flag = 6
                    else:
                        self.lb_error.setText("Данные введены неверно, за помощью к админу")
            if n == 2:

                self.lb_error.setText("Данные неверны, обратитесь к админу, чтоб восстановить их")

        elif self.flag == 0:
            self.lb_error.setText("Сначала нужно выбрать, что вы хотите сделать")



        elif self.flag == 0:
            self.lb_error.setText("Сначала нужно выбрать, что вы хотите сделать")

    def write_dev(self, n):
        if self.flag == 0:
            if n == 1:
                self.flag = 1
                self.lb_error.setText("Введите Логин и Пароль,а ваш личный код в поле ниже")
            elif n == 2:
                self.flag = 2
                self.lb_error.setText('Выбери свою роль (Страница "Зарегистрироваться")')
        elif n == 3:
            self.lb_error.setText("Вы начали заново, выберите, что вы хотите сделать")
            self.flag = 0
        elif self.flag == 1:
            self.lb_error.setText('Введите логин и пароль, чтоб начать сначала "Начать заново"')
        elif self.flag == 2:
            self.lb_error.setText('Выбери свою роль (Страница "Зарегистрироваться")')
        elif self.flag == 3:
            self.lb_error.setText('Введи логин и пароль и нажми на кнопку "Зарегистрироваться"')


    def add_functions(self):
        self.bt_dev_vx.clicked.connect(lambda: self.write_dev(1))
        self.bt_dev_reg.clicked.connect(lambda: self.write_dev(2))
        self.bt_dev_r.clicked.connect(lambda: self.write_dev(3))
        self.bt_vxod.clicked.connect(lambda: self.vxo())
        self.bt_reg.clicked.connect(lambda: self.regist())
        self.btgiga.clicked.connect(lambda: self.who_u(1))
        self.btrab.clicked.connect(lambda: self.who_u(2))
        self.btchep.clicked.connect(lambda: self.who_u(3))
        self.bt_got.clicked.connect(lambda: self.gotov())
        self.bt_giga_s.clicked.connect(lambda: self.surprise(1))
        self.bt_rab_s.clicked.connect(lambda: self.surprise(2))
        self.bt_chep_s.clicked.connect(lambda: self.surprise(3))
        self.bt_q_log.clicked.connect(lambda: self.q(1))
        self.bt_q_pas.clicked.connect(lambda: self.q(2))
        self.bt_q_got.clicked.connect(lambda: self.q(3))









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

