def answer(x, y):
    # your code here
    if ((x > 100000) and (x < 1)):
    	return "0";
    if ((y > 100000) and (y < 1)):
    	return "0";

    offset = (x + y - 1) * (x + y - 2) / 2;
    ret = offset + x;
    return str(ret);

print answer(3, 2);
print;
print answer(5, 10);
print;
print answer(1, 1);
print;
print answer(100000, 100000);
print;