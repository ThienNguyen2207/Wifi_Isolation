
#*************************************************
import subprocess
import xlrd
import os
from xlutils.copy import copy
import time
import paramiko

#*************************************************

book1 = xlrd.open_workbook("excel.xls")
wb = copy(book1)
s = wb.get_sheet(0)
#*************************************************

attempt=1

#*************************************************
SSID_List1 = [
'AAA_SSID_5G_1',
'AAA_SSID_5G_2',
'AAA_SSID_5G_3',] 

SSID_List2 = [
'AAA_SSID_5G_1',
'AAA_SSID_5G_2',
'AAA_SSID_5G_3',]

def ssh_PC(ssh,hostname,username,password):
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username,password)
	return ssh

def PC_connect(ssh,ssid):
	print(("Waiting for PC1 connecting to ssid{}").format(ssid))
	ssh.exec_command("netsh wlan disconnect")
	stdin, stdout, stderr = ssh.exec_command("netsh wlan connect name=\"" + str(ssid) + "\"")
	time.sleep(5)
	stdin, stdout, stderr = ssh.exec_command("netsh interface ip show address \"%s\"").format(Wifi_card)
	log= stdout.readlines()[3]
	return log

def Verify_IPaddr(log,IP_address):
	if "192.168" in log:
		IP_address=log.split(':')[1]
		return IP_address
	else:
		while attempt<3:
			PC_connect(ssh,ssid,stdout,log)
			if "192.168" in log:
				IP_address=log.split(':')[1]
				return IP_address
				break
			else:
				print("PC1: was failed at getting IP address")
				continue

def Ping_process():
	ping_in, ping_out, ping_err=ssh_1.exec_command("ping -n 3 {0}".format(IP_address2))
	ping_log=ping_out.read().decode()
	return ping_log

def Ping_result():
	print(ping_log)
	if "Approximate" in ping_log:
		print("******** Ping OK *********\n")
		s.write(local_index,remote_index,'OK')
		wb.save('excel.xls')
	else:
		print("******** Ping Fail *********\n")
		s.write(local_index,remote_index,'NOK')
		wb.save('excel.xls')


ssh1=ssh_PC(ssh1,"10.72.119.100","Dasan","123456")
ssh2=ssh_PC(ssh2,"10.72.120.100","Dasan","123456")

for ssid1 in SSID_List1:
log1=PC_connect(ssh1,ssid1,stdout)
IP_address1=Verify_IPaddr(log1,IP_address)
	for ssid2 in SSID_List2:
		log2=PC_connect(ssh2,ssid2,stdout)
		IP_address2=Verify_IPaddr(log2,IP_address)
		ping_log=Ping_process()
		Ping_result()

