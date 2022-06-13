import paramiko
ip='test.rebex.net' #server ip
port=22
username='demo'
password='password'
cmd='ls'
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)
stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
print(outlines)
for each_file in outlines:
    each_file = each_file.strip()
    if each_file == 'readme.txt':
        print ('readme.txt created')
        break
