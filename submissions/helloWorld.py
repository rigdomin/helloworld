#!/usr/bin/python

def funtest():
	return 'Hello World!'

if __name__ == '__main__':
	print('{} from {}'.format(funtest(), __name__))