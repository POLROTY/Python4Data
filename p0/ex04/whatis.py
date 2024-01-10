import sys


if len(sys.argv) != 1:
	assert len(sys.argv) == 2, "more than one argument is provided"

	# see if int
	try:
		number = int(sys.argv[1])
	except ValueError:
		raise AssertionError("argument is not an integer")

	# check even or odd
	if number % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")