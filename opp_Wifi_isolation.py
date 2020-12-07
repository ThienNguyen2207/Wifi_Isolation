class PC:

	def __init__(self):
		self.ssh=ssh
		self.log=log
		self.IP_address=IP_address

	def ssh(ssh, hostname, username, password):
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname,username,password)
		return ssh
	
	def connect_wifi():
		print(("Waiting for PC1 connecting to ssid{}").format(ssid))
		ssh.exec_command("netsh wlan disconnect")
		stdin, stdout, stderr = ssh.exec_command("netsh wlan connect name=\"" + str(ssid) + "\"")
		time.sleep(5)
		stdin, stdout, stderr = ssh.exec_command("netsh interface ip show address \"%s\"").format(Wifi_card)
		log= stdout.readlines()[3]
		return log

	def Verify_IP():
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

	def Ping_process(ssh):
		ping_in, ping_out, ping_err=ssh.exec_command("ping -n 3 {0}".format(IP_address2))
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


ssh1=PC.ssh(ssh_1, )