def answer(data, n):
    # your code here
    dataMap = {};
    for number in data:
    	strNumber = str(number);
    	if dataMap.has_key(strNumber):
    		dataMap[strNumber] = dataMap[strNumber] + 1;
    	else:
    		dataMap[strNumber] = 1;
    ret = [];
    for number in data:
    	strNumber = str(number);
    	if dataMap[strNumber] <= n:
    		ret.append(number);
    return ret;

a = [1,2,3];
n = 0;
b = answer(a, n);
print b;
a = [1, 2, 2, 3, 3, 3, 4, 5, 5];
n = 1;
b = answer(a, n);
print b;
a = [1,2,3];
n = 6;
b = answer(a, n);
print b;