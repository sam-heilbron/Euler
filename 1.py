#!/usr/bin/env python

##
## (Mults of 3) + (Mults of 5) - (Mults of 15)
##
## Sum(0 --> n) i = n(n+1)/2

import sys

def main(argv):
	maxNum = 1000
	
	sum3  = 3  * geoSum(multiplesUnderN( 3, maxNum))
	sum5  = 5  * geoSum(multiplesUnderN( 5, maxNum))
	sum15 = 15 * geoSum(multiplesUnderN(15, maxNum))

	print (sum3 + sum5 - sum15)
	return


def geoSum(n):
	return (n * (n+1))/2

def multiplesUnderN(mult, max):
	return int((max-1) / mult)


if __name__ == '__main__':
    main(sys.argv)
