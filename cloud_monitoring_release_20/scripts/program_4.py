import paramiko
ip='test.rebex.net' #server ip
port=22
username='demo'
password='password'
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)
ftp_client=ssh.open_sftp()
#ftp_client.get('readme.txt', 'server_readme.txt')
ftp_client.close()
file = open("server_readme.txt")
file_content = file.read()
