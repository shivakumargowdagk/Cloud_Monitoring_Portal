import paramiko
ip='test.rebex.net' #server ip
port=22
username='demo'
password='password'
cmd='echo test'
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)
stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
print(outlines)
for each_file in outlines:
    each_file = each_file.strip()
    print(each_file)
    if each_file == 'test':
        print ('command executed succesfully')
    else:
        print('command not found')

