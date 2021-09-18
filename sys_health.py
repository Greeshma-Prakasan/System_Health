import os

from rich.console import Console
from rich.text import Text

console = Console()

def get_mem():
	mem = os.popen("free").read()
	return "Available Memory",mem
	
def get_load_average():
	load_avg = os.popen("cat /proc/loadavg").read()
	return "Load Average",load_avg
	
	
def get_host_details():
	host_details = os.popen("hostnamectl").read()
	return "Hostname Details",host_details
	

def get_process_count():
	process_count = os.popen("ps -e | wc -l").read()
	return "All Process Count",process_count

def get_uptime():
	time = os.popen("uptime -s").read()
	return "Uptime",time

def print_res(res):
	text = Text(res[0]+"\n\n").append(res[1])
	text.stylize("bold green")
	console.print(text)



def menu():
	console.print(Text("1. Display Available Ram\n2. Display Load Average\n3. Display Hostname Details\n4. Display All Process Count\n5. Display Uptime\n6. Exit\n",style="bold blue"))

while True:
	menu()
	c = int(input(Text("Enter the choice : ",style="bold magenta")))
	if c == 1:
		res = get_mem()
		print_res(res)
	elif c == 2:
		res = get_load_average()
		print_res(res)
	elif c == 3:
		res = get_host_details()
		print_res(res)
	elif c == 4:
		res = get_process_count()
		print_res(res)
	elif c == 5:
		res = get_uptime()
		print_res(res)
	else:
		break