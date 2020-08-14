import sys
import socket
import optparse

def get_argument():

	parser=optparse.OptionParser()	
	parser.add_option("-i","--input",dest="input_file",help="Add a input with the path")
	parser.add_option("-o", "--output", dest="output_file", help="Add a output file")
	(options,arguments) = parser.parse_args()

	if not options.input_file:
		parser.error("\n[-] Specify an input file to scan --help for more details")
	if not options.output_file:
		parser.error("\n[-] Specify an output file file to scan --help for more details")

	return options

options = get_argument()






read_file = open(options.input_file,'r')
write_file = open(options.output_file, 'w+')
for host in read_file:
    a = socket.gethostbyname(host.rstrip("\n"))
    write_file.write(a + "\n")   
read_file.close()
write_file.close()