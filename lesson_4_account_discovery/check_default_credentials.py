import paramiko
import telnetlib

def ssh_login(host, port, username, password):
    """
    ssh: For secure remote access and command execution, SSH is the recommended approach. Libraries like paramiko in Python provide robust SSH client capabilities.

    Uses an ssh client to attempt to connect to local host, printing any successful attempts. 
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            print (f"ssh login successful on {host}:{port} with {username} & {password}")
    except Exception as e:
        print (e)
        return
    ssh.close()

# WARNING: Code using telnetlib will break in Python 3.13, with the library marked for removal due to its insecure nature.
def telnet_login(host, port, arg_username, arg_password):
    """
    telnet: The telnetlib module implements the Telnet protocol, which is an insecure, unencrypted protocol.

    Uses a telnet client that checks for telnet server messages, printing any username + passwords that produce a successful login.
    """
    username = bytes(arg_username + "\n", "utf-8")
    password = bytes(arg_password + "\n", "utf-8")

    tn = telnetlib.Telnet(host, port)
    tn.read_until(bytes("login: ", "utf-8"))
    tn.write(username)
    tn.read_until(bytes("password: ", "utf-8"))
    tn.write(password)
    try:
        result = tn.expect([bytes("last login", "utf-8")], timeout=2)
        if (result [0] >= 0):
            print (f"telnet login successful on {host}:{port} with {username} & {password}")
        tn.close()
    except EOFError:
        print (f"login failed with {username} and {password}")


host = "127.0.0.1"

with open ("defaults.txt", "r") as f:
    for line in f:
        vals = line.split()
        username = vals[0].strip()
        password = vals[1].strip()
        ssh_login(host, 22, username, password)
        telnet_login(host, 23, username, password)