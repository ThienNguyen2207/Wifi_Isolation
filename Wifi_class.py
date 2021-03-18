import subprocess
import xlrd
import os
from xlutils.copy import copy
import time
import paramiko
#################################

ssh_PC1=paramiko.SSHClient()
ssh_PC2=paramiko.SSHClient()

#################################
SSID_List1 = [
'B-LINK_B5F164',
'B-LINK_B5F164',] 

SSID_List2 = [
'B-LINK_B5F164',
'B-LINK_B5F164',]


class Windows:
	
	retries=3

	def __init__(self, hostname,username,password):
		self.hostname=hostname
		self.username=username
		self.password=password
#		self.retries=retries
		
	def ssh(self,ssh_pc):
		ssh_pc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		for i in range(self.retries):
			try:
				ssh_pc.connect(self.hostname,22, self.username,self.password)
				return True
			except paramiko.SSHException as e:
   				print("We have an issue in connectivity!")
   				print(e)
   				return False

	def Connect_ssid(self, ssh_pc):
		ssh_pc.exec_command("netsh wlan disconnect")
		print(("Waiting for PC connecting to ssid {}").format(ssid))
		ssh_pc.exec_command("netsh wlan connect name=\"" + str(ssid) + "\"")
		time.sleep(5)
		stdin, stdout, stderr = ssh_pc.exec_command(("netsh interface ip show address \"%s\"").format("Wi-Fi"))
		stdout=stdout.read().decode()
		print(stdout)
		


	def Verify_IPaddr():
		pass


	def Pingprogress():
		pass


	def Ping_Result():
		pass

PC1= Windows("192.168.100.111", "MinhThien", "ds1234$$")
PC2= Windows("192.168.100.222", "thiennguyen", "ds1234$$")


PC1.ssh(ssh_PC1)
PC2.ssh(ssh_PC2)

for ssid in SSID_List1:
	PC1.Connect_ssid(ssh_PC1)
	PC2.Connect_ssid(ssh_PC2)