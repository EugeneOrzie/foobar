def answer(total_lambs):
    # your code here
    if total_lambs == 0:
    	return 0;
    generousNumber = 0;
    usedNumber = 1;
    while (usedNumber <= total_lambs):
    	usedNumber = usedNumber * 2;
    	print usedNumber;
    	if (usedNumber - 1 <= total_lambs):
    		generousNumber = generousNumber + 1;
    	else:
    		break;

    stingyNumber = 1;
    usedNumber = 1;
    a = 0;
    b = 1;
    while (usedNumber <= total_lambs):
    	tmp = a + b;
    	if (usedNumber + tmp <= total_lambs):
    		a = b;
    		b = tmp;
    		usedNumber = usedNumber + tmp;
    		stingyNumber = stingyNumber + 1;
    		print usedNumber;
    	else:
    		break;
    print stingyNumber;
    print generousNumber;
    return (stingyNumber - generousNumber);

print answer(10);
print;
print answer(143);
print;
print answer(1000000000);
print;
print answer(1);