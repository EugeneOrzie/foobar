def answer(l):
    # your code here
    if ((len(l) > 2000) or (len(l) < 2)):
    	return 0;
    count = 0;

    for i in range(len(l)):
        pair = 0;
        for j in range(i + 1, len(l)):
            if (l[j] % l[i] == 0):
                pair = pair + 1;
        for k in range(0, i):
            if (l[i] % l[k] == 0):
                count = count + pair;

    return count;

a = [1, 1, 1];
print answer(a);

a = [1, 2, 3, 4, 5, 6];
print answer(a);