from selenium import webdriver
from time import sleep
import re
import paramiko
from web自动化.data.duqu import duqu
a=duqu()
b=a.du()


class 登录防火墙():
    dr =webdriver.Firefox()
    def denglu(self):
        dr =self.dr
        dr.get('http://192.168.0.254')
        sleep(1)
        dr.find_element_by_name('txt_password').send_keys('Bane@7766')
        wd=dr.find_element_by_id('checkinfo').find_elements_by_tag_name('img')
        for i in wd:
            a=i.get_attribute('src')#获取标签名中的属性
            b=re.compile(r'imgs/(.*?).gif')
            c=b.findall(a)
            dr.find_element_by_id('input1').send_keys(c)
        sleep(2)
        dr.find_element_by_name('dosubmit').click()
        sleep(2)
        w=dr.switch_to_alert()#切换到弹出框
        w.accept()#点击确定
        sleep(4)
        wd=dr.find_element_by_xpath('/html/frameset/frameset/frame[1]')
        dr.switch_to_frame(wd)
        dr.find_element_by_xpath('//*[@id="04"]').click()
        sleep(1)
        dr.find_element_by_xpath('//*[@id="041"]').click()
        sleep(2)
        dr.switch_to_default_content()
        cd=dr.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]')
        dr.switch_to_frame(cd)
        dr.find_element_by_xpath('//*[@id="nav_1"]').click()
    def xinjian(self,wenjian):
        dr = self.dr
        dr.switch_to_default_content()
        sleep(2)
        dd=dr.find_element_by_xpath('//*[@id="main"]')
        dr.switch_to_frame(dd)
        dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/div/div/a').click()
        dr.find_element_by_xpath('/html/body/div[2]/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr/td[2]/input').clear()
        dr.find_element_by_xpath('/html/body/div[2]/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr/td[2]/input').send_keys(
            wenjian[1])
        dr.find_element_by_xpath('/html/body/div[2]/form/table[1]/tbody/tr[2]/td/table/tbody/tr[5]/td[3]/table/tbody/tr/td[2]/div/input[3]').click()
        dr.find_element_by_xpath('/html/body/div[2]/form/table[1]/tbody/tr[2]/td/table/tbody/tr[5]/td[3]/table/tbody/tr/td[2]/div/div/table/tbody/tr[2]/td').click()
        wd = dr.window_handles
        cd = dr.current_window_handle
        dr.switch_to_window(wd[-1])
        sleep(2)
        dr.find_element_by_id('txt_addressName').send_keys(wenjian[2])
        dr.find_element_by_xpath('//*[@id="txt_address"]').send_keys(wenjian[3])
        dr.find_element_by_xpath('//*[@id="com_netmasktxt"]').send_keys(wenjian[4])
        dr.find_element_by_xpath('/html/body/form/table/tbody/tr[16]/td/div/div[2]/a').click()
        if wenjian[0] == '4':
            sleep(2)
            ww=dr.switch_to_alert()
            mm=ww.text
            ww.accept()
            dr.close()
            md=dr.window_handles
            dr.switch_to_window(md[0])
            dr.get('http://192.168.0.254')
            return mm
        else:

            dr.switch_to_window(cd)
            dr.switch_to_default_content()
            md = dr.find_element_by_xpath('//*[@id="main"]')
            dr.switch_to_frame(md)
            sleep(1)
            dr.find_element_by_xpath('/html/body/div[2]/form/table[1]/tbody/tr[2]/td/table/tbody/tr[6]/td[3]/table/tbody/tr/td[2]/div/input[3]').click()
            dr.find_element_by_xpath('/html/body/div[2]/form/table[1]/tbody/tr[2]/td/table/tbody/tr[6]/td[3]/table/tbody/tr/td[2]/div/div/table/tbody/tr[1]/td').click()
            wd = dr.window_handles
            cd = dr.current_window_handle
            dr.switch_to_window(wd[-1])
            sleep(1)
            dr.find_element_by_xpath('//*[@id="txt_addressName"]').send_keys(wenjian[5])
            dr.find_element_by_xpath('/html/body/form/table/tbody[1]/tr[4]/td[3]/table/tbody/tr/td[2]/input[1]').send_keys(wenjian[6])
            dr.find_element_by_xpath('/html/body/form/table/tbody[1]/tr[4]/td[3]/table/tbody/tr/td[2]/input[2]').send_keys(wenjian[7])
            dr.find_element_by_xpath('/html/body/form/table/tbody[2]/tr/td/div/div[2]/a').click()

            dr.switch_to_window(cd)
            dr.switch_to_default_content()
            md = dr.find_element_by_xpath('//*[@id="main"]')
            dr.switch_to_frame(md)
            dr.find_element_by_xpath('/html/body/div[2]/form/table[1]/tbody/tr[2]/td/table/tbody/tr[10]/td[3]/table/tbody/tr/td[2]/div/input[3]').click()
            dr.find_element_by_xpath('/html/body/div[2]/form/table[1]/tbody/tr[2]/td/table/tbody/tr[10]/td[3]/table/tbody/tr/td[2]/div/div/table/tbody/tr[4]/td').click()
            dr.find_element_by_xpath('/html/body/div[2]/form/table[2]/tbody/tr/td/div/div[1]/a').click()
            if wenjian[0] == '2' :

                sleep(2)
                ww = dr.switch_to_alert()
                mm= ww.text
                ww.accept()
                dr.get('http://192.168.0.254')
                return mm
            elif wenjian[0] == '3':
                sleep(2)
                ww = dr.switch_to_alert()
                mm = ww.text
                ww.accept()
                dr.get('http://192.168.0.254')
                return mm
            elif wenjian[0] == '5':
                ww = dr.switch_to_alert()
                mm = ww.text
                ww.accept()
                sleep(1)
                md = dr.window_handles
                dr.switch_to_window(md[-1])
                dr.close()
                md = dr.window_handles
                dr.switch_to_window(md[0])
                dr.get('http://192.168.0.254')
                return mm
    def chaxun(self,wenjian):
        dr =self.dr
        dr.switch_to_default_content()
        md = dr.find_element_by_xpath('//*[@id="main"]')
        dr.switch_to_frame(md)
        sleep(2)
        dr.find_element_by_link_text('按条件查询').click()
        sleep(1)
        dr.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/input').send_keys(wenjian[2])
        dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div/a').click()
        sleep(2)
        m = dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[3]/div/p')
        m = m.text
        dr.get('http://192.168.0.254')
        return m
    def houtai(self):
        ssh =paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect('192.168.0.254',22,'root','N@9!0~6$Bane3')
        a,b,c=ssh.exec_command('iptables -t nat -nvL')
        b= b.read().decode()
        ssh.close()
        return b