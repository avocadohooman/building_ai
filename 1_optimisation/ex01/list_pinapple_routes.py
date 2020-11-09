def main():
	portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
	port1 = 0
	for port2 in range(1, 5):
		for port3 in range(1, 5):
			for port4 in range(1, 5):
				for port5 in range(1, 5):				
					route = [port1, port2, port3, port4, port5]
					num = [0, 1, 2, 3, 4]
					check = 0
					for i in num:
						if (i in route):
							check += 1
					if (check == 5):
						print(' '.join([portnames[i] for i in route]))
					# do not modify the print statement

main()