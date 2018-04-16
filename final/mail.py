import imaplib
def mail():
	imap_host = 'imap.gmail.com'
	imap_user = 'swapnil.tech@global.org.in'
	imap_pass = 'Swapnil@tgs'
	# open a connection
	imap = imaplib.IMAP4_SSL(imap_host)
	# login
	imap.login(imap_user, imap_pass)
	# get status for the mailbox (folder) INBOX
	folderStatus, UnseenInfo = imap.status('INBOX', "(UNSEEN)")
	# print folder Status
	NotReadCounter = str(UnseenInfo[0])
	unread=NotReadCounter.replace("b'\"INBOX\" (UNSEEN ","")
	final=unread.replace(")'","")
	#print(final))
	# print NotReadCounter
	# print "You have "+NotReadCounter+" unread emails"
	mail = "You have "+final+" unread mails."
	print("Mail Status : "+mail)
	return mail

# mail()