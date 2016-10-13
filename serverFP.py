# Tcp Chat server

import socket, select

#Function to broadcast chat messages to all connected clients
def broadcast_data (sock, message):
	print 'broad'
	#Do not send the message to master socket and the client who has send us the message	
#	for socket in CONNECTION_LIST:
#		if socket != server_socket and socket != sock :
#			try :
#				socket.send(message)
#			except :
				# broken socket connection may be, chat client pressed ctrl+c for example
#				socket.close()
#				CONNECTION_LIST.remove(socket)

def handshake (nama1,nama2):
	print nama1 + '---' + nama2
	counter = 0;
	for i in CONNECTION_USER :
		if i == nama1 :
			soc = CONNECTION_USER[counter-1]
			soc.send(nama2+'!!!'+' ingin chat dengan anda'+'!!!')
			break
		counter += 1


if __name__ == "__main__":
	
	# List to keep track of socket descriptors
	CONNECTION_LIST = []
	CONNECTION_USER = []
	GROUP_LIST = dict()
	RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
	PORT = 5000
	
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# this has no effect, why ?
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(("0.0.0.0", PORT))
	server_socket.listen(10)

	# Add server socket to the list of readable connections
	CONNECTION_LIST.append(server_socket)
	print "Chat server started on port " + str(PORT)

	while 1:
		# Get the list sockets which are ready to be read through select
		read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

		for sock in read_sockets:
			#New connection
			if sock == server_socket:
				# Handle the case in which there is a new connection recieved through server_socket
				sockfd, addr = server_socket.accept()
				CONNECTION_LIST.append(sockfd)	
				print "Client (%s, %s ) connected" % addr
				#broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)
			#Some incoming message from a client
			else:
#				print 'else'
				data = ''
				while 1:
					temp = sock.recv(1024)
					if(temp[-2:] == '__'):
						data+=temp
						break
					if(temp[-2:] == '++'):
						data+=temp
						break
					if(temp[-3:] == '@@@'):
						data+=temp
						break						
					if(temp[-3:] == '==='):
						data+=temp
						break
					if(temp[-3:] == '@!@'):
						data+=temp
						break	
					if(temp[-3:] == '=-='):
						data+=temp
						break	
					if(temp[-3:] == '*@*'):
						data+=temp
						break	
					if(temp[-3:] == '*#*'):
						data+=temp
						break	
					if(temp[-3:] == '=$='):
						data+=temp
						break	
					if(temp[-3:] == '=$$'):
						data+=temp
						break	
					data+=temp
				
				print data

				if(data[-2:]== '__'):
#					print('1')
					CONNECTION_USER.append(sock)
					CONNECTION_USER.append(data[:-2])				
#					for i in CONNECTION_USER :
#						print i			
					broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)                				
				elif(data[-3:]=='@@@'):
#					print('2')
					sp = data.split('@@@')
#					print '-=-=-='
					handshake(sp[0], sp[1])
				elif(data[-3:]=='*#*'):
					sp = data.split('*#*')
					if sp[0]=='remove':
						del GROUP_LIST[sp[1]][sock]
					else:
						for i in GROUP_LIST[sp[1]]:
							if(i!=sock):
								i.send(sp[2]+'>>'+sp[0]+'*@!')
				elif(data[-3:]=='=$$'):
					sp = data.split('=$$')
					print 'qwerty'
					print sp[2]
					print sp[3]
					for i in GROUP_LIST[sp[1]]:
						if(i!=sock):
							i.send('>>'+sp[2]+sp[3]+'=$$'+sp[0]+'=$$'+sp[3]+'=$$')
				elif(data[-3:]=='*@*'):
					print('asfasf')
					sp = data.split('*@*')
					print sp[0] + '>>' + sp[1]
					if(sp[0]=='create_group'):
						print 'asdasd'
						GROUP_LIST[sp[1]] = dict()
						GROUP_LIST[sp[1]][sock] = 1
					elif(sp[0]=='join_group'):
						print 'gabung'
						GROUP_LIST[sp[1]][sock] = 1
						sock.send('anda bergabung group ' + '*!*' + sp[1] + '*!*')
					print 'gav'
						
							
				elif(data[-2:]== '++'):
#					print('3')
					broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)                								
				elif(data[-3:]== '===' ):
#					print('4')
					sp = data.split('===')
					cnt=0;
					for i in CONNECTION_USER:
						if i == sp[1] :
							soc = CONNECTION_USER[cnt-1]
							soc.send(sp[0]+'-_-')
							break
						cnt += 1					
				elif(data[-3:]== '=$=' ):
#					print('4')
					sp = data.split('=$=')
					cnt=0;
					for i in CONNECTION_USER:
						if i == sp[1] :
							soc = CONNECTION_USER[cnt-1]
							soc.send(sp[0]+'=$='+sp[2]+'=$=')
							break
						cnt += 1					
				elif(data[-3:]== '@!@'):
#					print('5')
#					print 'lalalar'
					sp = data.split('@!@')
					cnt=0;
					for i in CONNECTION_USER:
						if i == sp[0] :
							soc = CONNECTION_USER[cnt-1]
							soc.send('***')
							break
						cnt += 1
				elif(data[-3:]== '=-='):
#					print('5')
#					print 'lalalar'
					sp = data.split('=-=')
					cnt=0;
					for i in CONNECTION_USER:
						if i == sp[0] :
							soc = CONNECTION_USER[cnt-1]
							soc.send('=-=')
							break
						cnt += 1

#				print 'allah'				
#				# Data recieved from client, process it
#				try:
#					#In Windows, sometimes when a TCP program closes abruptly,
#					# a "Connection reset by peer" exception will be thrown
#					data = sock.recv(RECV_BUFFER)
#					if data:
#						broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)                
#				except:
#					broadcast_data(sock, "Client (%s, %s) is offline" % addr)
#					print "Client (%s, %s) is offline" % addr
#					sock.close()
#					CONNECTION_LIST.remove(sock)
#					continue
	
	server_socket.close()
