import sys
import PyQt5.QtWidgets as qw
import Ui_dba_to_dwd
import tools

class myForm(qw.QMainWindow, Ui_dba_to_dwd.Ui_MainWindow):
    
    def __init__(self):
        super(myForm, self).__init__()
        self.setupUi(self)
        self.statusbar.showMessage("status:ok")
    
    def transfer(self):
        global dwd_tb_name
        text=self.plainTextEdit_dba.toPlainText()
        # 判断是否写了系统名称
        sysName=self.lineEdit_sysName.text()
        if sysName=='':
            self.statusbar.showMessage("status:无法获取源系统名称")
        else:    
            if self.radioButton_mysql.isChecked():
                trans_text, dwd_tb_name=tools.mysql_trans_to_dwd(text,sysName)
                self.plainTextEdit_dwd.setPlainText(trans_text)
                self.lineEdit_tbName.setText(dwd_tb_name)
                self.statusbar.showMessage("status:语句转换完成")
            elif self.radioButton_oracle.isChecked():
                self.plainTextEdit_dwd.setPlainText('该版本暂不支持Oracle语句转换')
                self.lineEdit_tbName.setText('该版本暂不支持Oracle语句转换')
        
        
    def save_sql(self):
        save_path=self.lineEdit_savePath.text()
        if save_path=='':
            self.statusbar.showMessage("status:无法获取存储路径")
        else:
            save_content=self.plainTextEdit_dwd.toPlainText()
            # 检查保存路径是否存在，若不存在则创建
            tools.check_save_path(save_path)
            # 保存解析后的建表语句
            try:
                tools.save_file(save_content,dwd_tb_name,save_path)
                self.statusbar.showMessage("status:文件保存成功")
            except:
                pass
            
            
        
        

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w1 = myForm()
    w1.pushButton_transfer.clicked.connect(w1.transfer)
    w1.pushButton_save.clicked.connect(w1.save_sql)
    w1.show()
    app.exec_()