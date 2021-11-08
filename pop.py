import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
email = 'user14885233@mail4.nospoofing.cn'
password = "19YkkJKn0p31"
pop3_server = 'mail4.nospoofing.cn' 
server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))
server.user(email)
server.pass_(password)
print('Messages: %s. Size: %s' % server.stat())
resp, mails, octets = server.list()
print(mails)
index = len(mails)
resp, lines, octets = server.retr(index)
msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)
print(msg)
server.quit()