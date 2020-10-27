#levensthein_distance.py
import numpy

def printLD(array2D, rows, columns):
	for r in range(rows+1):
		for c in range(columns+1):
			print(array2D[r][c], end=' ')
		print()

def rawString(string):
	print( string.replace(' ','').lower() )
	return ( string.replace(' ','').lower() )

def levenshteinDistance(string1, string2):
	array2D = numpy.zeros((len(string1)+1, len(string2)+1),dtype = int)

	for row in range(len(string1)+1):
		array2D[row][0] = row

	for column in range(len(string2)+1):
		array2D[0][column] = column

	for i in range(1, len(string1)+1):
		for j in range(1, len(string2)+1):
			if(string1[i-1]==string2[j-1]):
				array2D[i][j] = array2D[i-1][j-1]
			else:
				if( array2D[i][j-1] <= array2D[i-1][j] and array2D[i][j-1] <= array2D[i-1][j-1]):
					array2D[i][j] = array2D[i][j-1] +1
				elif( array2D[i-1][j] <= array2D[i][j-1] and array2D[i-1][j] <= array2D[i-1][j-1]):
					array2D[i][j] = array2D[i-1][j] +1
				else:
					array2D[i][j] = array2D[i-1][j-1] +1

	printLD(array2D, len(string1), len(string2))
	return array2D[len(string1), len(string2)]



def main():
	string1 = 'sloworafa'
	string2 = 'slowo'

	raw_string1 = rawString(string1)
	raw_string2 = rawString(string2)
	distance = levenshteinDistance(raw_string1, raw_string2)
	print('\nThe distance between this two strings equals {}'.format(distance))


if __name__ == "__main__":
    main()