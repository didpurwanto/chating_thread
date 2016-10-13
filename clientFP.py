# telnet program example
import socket, select, string, sys

def prompt() :
	sys.stdout.write('<You> ')
#	sys.stdout.flush()

#main function
if __name__ == "__main__":		
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# connect to remote host
	try :
		s.connect(('localhost', 5000))
	except :
		print 'Unable to connect'
		sys.exit()
	
	print 'username'
	username = raw_input()	
	s.send(username+'__')
	
	print 'Connected to remote host. Start sending messages'
	prompt()
	
	flag = 0
	chatpartner= ''
	partner =''
	while 1:
		socket_list = [sys.stdin, s]
		
		# Get the list sockets which are readable
		read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
		
		for sock in read_sockets:
			#incoming message from remote server
			if sock == s:
				dat = ''
				while 1:
					tmp = sock.recv(1024)
					if tmp[-3:] == '!!!':
						dat+=tmp
						break
					elif tmp[-3:] == '-_-':
						dat+=tmp
						break	
					elif tmp[-3:] == '=-=':
						dat+=tmp
						break	
					elif tmp[-3:] == '***':
						flag=1
						break
					elif tmp[-3:] == '*!*':
						dat+=tmp
						break
					elif tmp[-3:] == '*@!':
						dat+=tmp
						break
					elif tmp[-3:] == '=$=':
						dat+=tmp
						break
					elif tmp[-3:] == '=$$':
						dat+=tmp
						break
					dat+=tmp

				if dat[-3:] == '!!!' :
					sp = dat.split('!!!')
					print sp[0] + sp[1] + '   ok/no?'
					partner = sp[0]
				elif dat[-3:] == '=$$' :
					sp = dat.split('=$$')
					print sp[0]
					zzzz = username + sp[2]
				#	print sp[2]
				#	print zzzz
					getfile = open(zzzz,'w')
					getfile.write(sp[1])
					getfile.close()
				elif dat[-3:] == '=$=' :
					sp = dat.split('=$=')
				#	print sp[0]
					getfile = open(username+sp[1],'w')
					getfile.write(sp[0])
					getfile.close()
				elif dat[-3:] == '*@!' :
					sp = dat.split('*@!')
					print sp[0]
				elif dat[-3:] == '-_-' :
					sp = dat.split('-_-')
					print chatpartner + '>>' +sp[0]
				elif dat[-3:] == '=-=' :
					flag=0
				elif dat[-3:] == '*!*' :
					flag=2
					sp = dat.split('*!*')
					gChat = sp[1]
					print sp[0] + sp[1]
				else :
					sp = dat.split('***')
					print sp[0]
				
					
#				if not data :
#					print '\nDisconnected from chat server'
#					sys.exit()
#				else :
#					print data
#					sys.stdout.write(data)
#					prompt()
			
			#user entered a message
			else :
				if(flag==1):
					print 'you>>'
					cmd = raw_input()
					if(cmd == '###'):
						s.send(chatpartner+'=-=')
						flag=0
					elif(cmd == 'kirim_file'):
						print 'namafile'
						msg = raw_input()
						berkas = open(msg,'r')
						databerkas = berkas.read()
						s.send(databerkas+'=$='+chatpartner+'=$='+'kirim'+msg+'=$=')
					else :
						s.send(cmd+'==='+chatpartner+'===')
				elif(flag==2):
					print 'you>>'
					msg = raw_input()
					if(msg=='###'):
						s.send('remove'+'*#*'+gChat+'*#*')
						flag = 0
					elif(msg == 'kirim_file'):
						print 'namafile'
						cmd = raw_input()
						berkas = open(cmd,'r')
						databerkas = berkas.read()
						s.send(databerkas+'=$$'+gChat+'=$$'+username+'=$$'+'kirim '+cmd+'=$$')
					else :
						s.send(msg+'*#*'+gChat+'*#*'+username+'*#*')
				else:
					cmd = raw_input()
					if(cmd == '@@@'):
						#print 'if1'
						msg = raw_input()
						print msg + '-----'
						chatpartner = msg
						s.send(msg+'@@@'+username+'@@@')
					elif(cmd == 'ok'):
						#print 'if2'
						flag=1
						chatpartner = partner
						s.send(chatpartner+'@!@')
					elif(cmd == 'create_group'):
						print 'masukan nama group'
						msg = raw_input()
						flag=2
						gChat = msg
						s.send(cmd + '*@*' +msg+'*@*')
					elif(cmd == 'join_group'):
						print 'masukan nama groupp'
						msg = raw_input()
						gChat = msg
						s.send(cmd + '*@*' +msg+'*@*')
			#		else:
			#			#print 'if3'
			#			msg = sys.stdin.readline()
			#			s.send(msg+'++')
			#			prompt()
