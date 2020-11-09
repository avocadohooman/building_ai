# appends it to the list route
# removes it from the list of available ports, and
# calls the same function with the remaining ports

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
	# write the recursive function here
	# remember to print out the route as the recursion ends
	if len(ports) < 1:
		print(' '.join([portnames[i] for i in route]))
		route.pop(-1)
	else:
		x = 0
		for i in ports:
			route.append(i)
			permutations(route, ports[:x]+ports[x+1:])
			x += 1
		route.pop(-1)
# this will start the recursion with 0 as the first stop
permutations([0], list(range(1, len(portnames))))