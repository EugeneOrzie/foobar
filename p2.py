def answer(s):
    # your code here
    doubleString = s + s;
    stringLength = len(s);
    print "stringLength=";
    print stringLength;
    for partLength in range(stringLength):
    	print "partLength=";
    	print partLength;

    	if (stringLength % (partLength + 1) != 0):
    		continue;
    	for fromIndex in range(stringLength):
    		partNumber = stringLength / (partLength + 1);
    		baseStr = doubleString[fromIndex:fromIndex + partLength + 1];
    		print "baseStr=" + baseStr;

    		found = True;
    		for k in range(partNumber):
    			begin = fromIndex + k * (partLength + 1);
    			end = fromIndex + (k + 1) * (partLength + 1);
    			print "doubleString=" + doubleString[begin : end];
    			if doubleString[begin : end] != baseStr:
    				found = False;
    				break;
    		if found:
    			return partNumber;

    return 1;

s = "abccbaabccba";
print answer(s);

print "################"
s = "abcabcabcabc";
print answer(s);

print "################"
s = "aaaaaaaaaaaa";
print answer(s);