from pwn import *

conn = remote("39.106.44.81", 10000)
# conn = remote("192.168.2.168", 10000)

# ans = conn.recvline()
# print(ans)

hello_world = conn.recvline()
print(hello_world)

# payload char range from 33 to 126, begin at 126
payload = chr(126) * 40

big = b'Wroooooog password, tooooooo big!'
let = b'Wroooooog password, tooooooo small!'
out = b'Toooooo many failed attempts, account locked!'
right = b'Congratulations !'

for i in range(0, 40):
	l = 33
	r = 126
	f = False

	while True:
			if l + 1 == r:
				if not f:
					f = True
				else:
					f = False
					l += 1
		
			curr_char = (l + r) >> 1
			print("i = {}, l = {}, r = {}, curr = {}:{}".format(i, l, r, curr_char, chr(curr_char)))
			payload = payload[:i] + chr(curr_char) + payload[i + 1:]
			print('send payload: {}'.format(payload))
			# print('ans =       : {}'.format(ans))
			conn.sendafter('> ', payload + '\n')

			rsp = conn.recvline()

			print("rsp = {}".format(rsp))

			if rsp.startswith(big):
				print('too big')
				r = curr_char
				if l == r:
					break
			elif rsp.startswith(let):
				print('too small')
				l = curr_char + 1
			elif rsp.startswith(out):
				print('too many failed attempts, out')
				exit()
			elif rsp.startswith(right):
				print('got flag')
				flag = conn.recvline()
				print('flag: {}'.format(flag))
				exit()

			print('\n')
