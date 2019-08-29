#using paramiko for ssh
import paramiko
p = paramiko.SSHClient()

#reading server details from a csv file and connecting to the host to execute commands
server_details = open("server_list.csv","r")
for each in server_details.readlines():
        strip_each=each.strip()
        line=strip_each.split(",")
        p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        p.connect("%s"%line[0],port =22, username = "%s"%line[1], password="%s"%line[2])
        stdin, stdout, stderr = p.exec_command("df -Pkh")
        output = stdout.readlines()
        output ="".join(output)
        result = open("%s.txt"%line[0],"w")
        result.write(output)
        result.close()
server_details.close()
