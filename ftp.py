import ftplib, os

def download(ftp,directory,file):
    ftp.cwd(directory)
    f = open(file,"wb")
    ftp.retrbinary("RETR " + file,f.write)
    f.close()
    


def get_ftp_files(ftp,directory):
	dirlist = []
	files_list = []
	ftp.cwd(directory)
	ftp.retrlines('LIST',dirlist.append)
	for lines in dirlist:
		lines_split = lines.split()
		files_list.append(lines_split[8])

	return files_list


ftp = ftplib.FTP("ftp.cisco.com")
ftp.login("anonymous", "email@mail.com")

txt = open('MBS.txt').read()
txt = txt.split()

ftp_list = get_ftp_files(ftp,'/pub/mibs/v2/')
fail_ctr = 0
fail_list = []
for lines in txt:
	i = 0
	try:
		i = ftp_list.index(lines+'.my')
	except ValueError:
		i = -1 # no match
	print str(i)
	if i == -1: 
		print lines + " not found on the server    <<<========= ERROR"
		fail_ctr += 1
		fail_list.append(lines)
	else:
		print lines + " was found on FTP server - DOWNLOADING..."
		download(ftp, "/pub/mibs/v2/", lines+".my")
		print lines + ".my was succsessfully downloaded to " + os.getcwd()
		
print str(fail_ctr) + " files were not found on the server:"
print fail_list


