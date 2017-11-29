from fractions import *

def gcd(a, b):
    if a > b:
        a, b = b, a;
    while b != 0:
        a, b = b, a % b;
    return a;

def lcm(a, b):
    return a * b / gcd(a, b);

def lcmm(l):
        return reduce(lambda x, y: lcm(x, y), l)

def calculateMatrixMultiplication(a, b):
    bCol = zip(*b);
    newMatrix = [];
    for row in a:
        newRow = [];
        for col in bCol:
            print zip(row, col);
            total = sum(rowElement * colElement for rowElement, colElement in zip(row, col));
            print total;
            newRow.append(total);
        newMatrix.append(newRow);
    return newMatrix;

def calculateMatrixMinor(matrix, i, j):
    newMatrix = [];
    for row in matrix[:i]:
        newRow = row[:j] + row[j+1:];
        newMatrix.append(newRow);

    for row in matrix[i+1:]:
        newRow = row[:j] + row[j+1:];
        newMatrix.append(newRow);
    return newMatrix;

def calculateMatrixDeterminant(matrix):
    if (len(matrix) == 1):
        return matrix[0][0];
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0];
    total = 0;
    for rowNumber in range(len(matrix)):
        flag = ((-1)**rowNumber);
        total = total + flag * matrix[0][rowNumber] * calculateMatrixDeterminant(calculateMatrixMinor(matrix, 0, rowNumber));
    return total;

def calculateMatrixTranspose(matrix):
    newMatrix = [];
    for rowNumber in range(len(matrix)):
        newRow = [];
        for colNumber in range(len(matrix[rowNumber])):
            newRow.append(matrix[colNumber][rowNumber]);
        newMatrix.append(newRow);
    return newMatrix;

def calculateMatrixCofactor(matrix):
    newMatrix = [];
    for rowNumber in range(len(matrix)):
        newRow = [];
        for colNumber in range(len(matrix[rowNumber])):
            flag = ((-1)**(rowNumber + colNumber));
            newRow.append(flag * calculateMatrixDeterminant(calculateMatrixMinor(matrix, rowNumber, colNumber)));
        newMatrix.append(newRow);
    return newMatrix;

def calculateMatrixInverse(matrix):
    adjugateMatrix = calculateMatrixTranspose(calculateMatrixCofactor(matrix));
    determinant = calculateMatrixDeterminant(matrix);
    for rowNumber in range(len(adjugateMatrix)):
        for colNumber in range(len(adjugateMatrix)):
            adjugateMatrix[rowNumber][colNumber] = adjugateMatrix[rowNumber][colNumber] / determinant;
    return adjugateMatrix;

def answer(m):
    # your code here
    if len(m) == 1:
        return [1,1];
    absorbingRow = [];
    nonAbsorbingRow = [];

    for i, row in enumerate(m):
        if (sum(row) == 0):
            absorbingRow.append(i);
        else:
            nonAbsorbingRow.append(i);

    if (len(absorbingRow) == 1):
        return [1,1];

    rowOrder = absorbingRow + nonAbsorbingRow;

    newMatrix = [];
    for i in rowOrder:
        newRow = [];
        for j in rowOrder:
            newRow.append(m[i][j]);
        newMatrix.append(newRow);

    #print newMatrix;

    R = [];
    Q = [];
    for row in newMatrix[len(absorbingRow):]:
        tempRow = [];
        for ele in row:
            tempRow.append(Fraction(ele, sum(row)));
        R.append(tempRow[:len(absorbingRow)]);
        Q.append(tempRow[len(absorbingRow):]);

    #print "R, Q";
    #print R;
    #print Q;

    I = [];
    for rowNumber in range(len(Q)):
        tempRow = [0] * len(Q)
        tempRow[rowNumber] = 1
        I.append(tempRow)

    #print I;
    
    IMinusQ = [];
    for rowNumber in range(len(I)):
        tempRow = []
        for colNumber in range(len(I[0])):
            tempRow.append(I[rowNumber][colNumber]-Q[rowNumber][colNumber]);
        IMinusQ.append(tempRow);
    #print IMinusQ;

    F = calculateMatrixInverse(IMinusQ);
    #print F;
    FMulR = calculateMatrixMultiplication(F, R);
    #print FMulR;
    
    newRow = []
    for i in FMulR[0]:
        newRow.append([i.numerator, i.denominator])
    

    lcmAll = lcmm([i[1] for i in newRow])
    
    # make fractions common denominator and return
    ret = [ (lcmAll/i[1]) * i[0] for i in newRow ]
    return ret + [lcmAll]

print 1;
print gcd(8, 6);
print gcd(10, 5);
print gcd(80, 100);

print lcm(8, 6);
print lcm(10, 5);
print lcm(80, 100);

m = [[0, 2, 1, 0, 0], 
    [0, 0, 0, 3, 4], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0]];
print calculateMatrixMinor(m, 0, 1);

print m;
b = [[1, 2],
    [3, 4]];
c = [[1, 2],
    [3, 4]];
print calculateMatrixMultiplication(b, c);
d = [[3, 0, 2],
    [2, 0, -2],
    [0, 1, 1]];

print "result:";
print calculateMatrixTranspose(d);
print calculateMatrixDeterminant(d);
print calculateMatrixCofactor(d);
print calculateMatrixInverse(d);
#print (*m);
print zip(*m);

m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]];
m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]];
print answer(m)