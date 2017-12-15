'''Q1.
Given an integer, find its kth digit.
Example
For n = 578943 and k = 2, the output should be
kthDigit(n, k) = 7.
Input/Output
[time limit] 3000ms (java)
[input] integer n
Guaranteed constraints:
105 ≤ n ≤ 106.
[input] integer k
A non-negative integer.
Guaranteed constraints:
1 ≤ k ≤ 7.
[output] integer
kth digit of the given number or -1 there are less than k digits.
'''

def kthDigit(n, k):
    s=str(n)
    if(k<=len(s)):
        return int(s[k-1])
    else:
        return -1
'''
Q2.
You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.
Given the starting HTML tag, find the appropriate end tag which your editor should propose.
If you are not familiar with HTML, consult with this note.
Example
For startTag = "<button type='button' disabled>", the output should be
htmlEndTagByStartTag(startTag) = "</button>";
For startTag = "<i>", the output should be
htmlEndTagByStartTag(startTag) = "</i>".
Input/Output
[time limit] 3000ms (java)
[input] string startTag
Guaranteed constraints:
3 ≤ startTag.length ≤ 75.
[output] string
'''

####Code#####

def htmlEndTagByStartTag(startTag):
    s=startTag.split()
    m=s[0]
    if(">" in m):
        return m[0]+"/"+m[1:]
    else:
        return m[0]+"/"+m[1:]+">"



'''Q3.
When you recently visited your little nephew, he told you a sad story: there's a bully at school who steals his lunch every day, and locks it away in his locker. He also leaves a note with a strange, coded message. Your nephew gave you one of the notes in hope that you can decipher it for him. And you did: it looks like all the digits in it are replaced with letters and vice versa. Digit 0 is replaced with 'a', 1 is replaced with 'b' and so on, with digit 9 replaced by 'j'.
The note is different every day, so you decide to write a function that will decipher it for your nephew on an ongoing basis.
Example
For note = "you'll n4v4r 6u4ss 8t: cdja", the output should be
stolenLunch(note) = "you'll never guess it: 2390".
Input/Output
[time limit] 4000ms (py)
[input] string note
A string consisting of lowercase English letters, digits, punctuation marks and whitespace characters (' ').
Guaranteed constraints:
0 ≤ note.length ≤ 500.
[output] string
The deciphered note.
'''
#####Code######

def stolenLunch(note):
    d = '0123456789'
    a = 'abcdefghij'
    r = '' 
    for i in note:
        if i in d: 
            r+= a[d.index(i)]
            
        elif i in a:
            r+= d[a.index(i)]
        else: 
            r+=i
    return r




'''
Q.Given a divisor and a bound, find the largest integer N such that:
N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
It is guaranteed that such a number exists.
Example
For divisor = 3 and bound = 10, the output should be
maxMultiple(divisor, bound) = 9.
The largest integer divisible by 3 and not larger than 10 is 9.
Input/Output
[time limit] 3000ms (java)
[input] integer divisor
Guaranteed constraints:
2 ≤ divisor ≤ 10.
[input] integer bound
Guaranteed constraints:
5 ≤ bound ≤ 100.
[output] integer
The largest integer not greater than bound that is divisible by divisor
'''

int maxMultiple(int divisor, int bound) {
    int ans=0;
    for(int i=bound;i>0;i--)
    {
        if(i%divisor==0)
        {
            ans=i;
            break;
        }
    }
    return ans;
}



'''
Q.
In Thumbtack, users are able to rate Pros based on their experience working with them. Each rating is an integer ranging from 1 to 5, and all ratings are averaged to produce a single number rating for any given Pro. Those Pros who have a rating lower than a specified threshold are manually reviewed by Thumbtack staff to ensure high quality of service.
You're given a list of ratings for some Pros. Find out which Pros should be manually reviewed.
Example
For threshold = 3.5 and
ratings = [[3, 4],
           [3, 3, 3, 4],
           [4]]
the output should be ratingThreshold(threshold, ratings) = [1].
Assume that we have 3 Pros that have received the following ratings: [3, 4], [3, 3, 3, 4] and [4]. Then
And if threshold = 3.5 the answer is ratingThreshold(threshold, ratings) = [1].
The first Pro's rating is 3.5, the second one's is 3.25, and the last one's is 4, so only the second Pro should be reviewed manually (the output is their 0-based index).
Input/Output
[time limit] 4000ms (py)
[input] float threshold
A positive number not greater than 5. Those Pros whose ratings are lower than threshold should be manually reviewed.
Guaranteed constraints:
1 ≤ threshold ≤ 5.
[input] array.array.integer ratings
For each valid i, ratings[i] is a non-empty array that represents the last ratings the ith Pro has received.
Guaranteed constraints:
0 ≤ ratings.length ≤ 5,
1 ≤ ratings[i].length ≤ 15,
1 ≤ ratings[i][j] ≤ 5.
[output] array.integer
0-based indices of the Pros that should be reviewed, sorted in ascending order.
Code:
def ratingThreshold(threshold, ratings):
    hasil = []
    for x in ratings:
        if (sum(x)/float(len(x))) < threshold:
            hasil.append(ratings.index(x))
    return hasil
Q
Find the sum of cubes of all integers starting from 1 up to the given integer n, inclusive.
Example
For n = 3, the output should be
sumOfCubes(n) = 36.
Because 13 + 23 + 33 = 1 + 8 + 27 = 36.
Input/Output
[time limit] 4000ms (py)
[input] integer n
Guaranteed constraints:
1 ≤ n ≤ 10.
[output] integer
'''

def cube(n):
    return n*n*n
def sumOfCubes(n):
    sum=0
    for i in range(n+1):
        sum+=cube(i)
    return sum



'''Q
Find the longest string from the given array.
Example
For inputArray = ["a", "ab", "c"], the output should be
longestString(inputArray) = "ab".
Input/Output
[time limit] 4000ms (py3)
[input] array.string inputArray
A non-empty array of strings.
Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.
[output] string
The longest string of inputArray. It's guaranteed that there is always a unique output.

'''

#Code:
def longestString(inputArray):
    return max(inputArray,key=len)



'''Q.

You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
Example
For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
Input/Output
[time limit] 4000ms (py)
[input] array.integer inputArray
Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-105 ≤ inputArray[i] ≤ 105.
[output] integer
The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.'''
#Code:

def arrayChange(inputArray):
    result = 0
    for i in range(1, len(inputArray)):
        if (inputArray[i] <= inputArray[i - 1]):
            result += inputArray[i-1] - inputArray[i] +1;
            inputArray[i] = inputArray[i-1] + 1;
    return result




'''Q.
For a string consisting of only '('s and ')'s, determine if it is a regular bracket sequence or not.
Example
For sequence = "()()", the output should be
regularBracketSequence1(sequence) = true.
We could insert (1 + 2) * (2 + 4) which is a valid arithmetic expression, so the answer is true.
Input/Output
[time limit] 4000ms (py)
[input] string sequence
Guaranteed constraints:
4 ≤ sequence.length ≤ 10.
[output] boolean
true if the bracket sequence is regular, false otherwise.
GIVE UP'''

#CODE:

def regularBracketSequence1(sequence):
    balance = 0
    for i in range(len(sequence)):
        if sequence[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return  False 
    if balance != 0:
        return False
    return True



'''Q.
Elections are in progress!
Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.
The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.
Example
For votes = [2, 3, 5, 2] and k = 3, the output should be
electionsWinners(votes, k) = 2.
The first candidate got 2 votes. Even if all of the remaining 3 candidates vote for him, he will still have only 5 votes, i.e. the same number as the third candidate, so there will be no winner.
The second candidate can win if all the remaining candidates vote for him (3 + 3 = 6 > 5).
The third candidate can win even if none of the remaining candidates vote for him. For example, if each of the remaining voters cast their votes for each of his opponents, he will still be the winner (the votes array will thus be [3, 4, 5, 3]).
The 
last candidate can't win no matter what (for the same reason as the first candidate).
Thus, only 2 candidates can win (the second and the third), which is the answer.
Input/Output
[time limit] 4000ms (py)
[input] array.integer votes
A non-empty array of non-negative integers. Its ith element denotes the number of votes cast for the ith candidate.
Guaranteed constraints:
4 ≤ votes.length ≤ 105,
0 ≤ votes[i] ≤ 104.
[input] integer k
The number of voters who haven't cast their vote yet.
Guaranteed constraints:
0 ≤ k ≤ 105.
[output] integer
GIVE UP
'''

#CODE:

def electionsWinners(votes, k):
    possible_winners = 0
    m = max(votes)
    if k == 0 and votes.count(m) == 1:
        return 1
    for v in votes:
        if v + k > m:
            possible_winners += 1
    return possible_winners





'''Q.
Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.
Given the first element a0, find the length of the sequence.
Example
For a0 = 16, the output should be
squareDigitsSequence(a0) = 9.
Here's how elements of the sequence are constructed:
a0 = 16
a1 = 12 + 62 = 37
a2 = 32 + 72 = 58
a3 = 52 + 82 = 89
a4 = 82 + 92 = 145
a5 = 12 + 42 + 52 = 42
a6 = 42 + 22 = 20
a7 = 22 + 02 = 4
a8 = 42 = 16, which has already occurred before (a0)
Thus, there are 9 elements in the sequence.
For a0 = 103, the output should be
squareDigitsSequence(a0) = 4.
The sequence goes as follows: 103 -> 10 -> 1 -> 1, 4 elements altogether.
Input/Output
[time limit] 4000ms (py)
[input] integer a0
First element of a sequence, positive integer.
Guaranteed constraints:
1 ≤ a0 ≤ 650.
[output] integer
'''
#CODE:

def squareDigitsSequence(a0):

    cur = a0
    was = set()

    while not (cur in was):
        was.add(cur)
        nxt = 0
        while cur > 0:
            nxt += (cur % 10) * (cur % 10)
            cur /= 10
        cur =  nxt
        print cur

    return len(was) + 1





'''Q.
For given integers a and b, find the last digit of ab.
Example
For a = 2 and b = 5, the output should be
lastDigit(a, b) = 2.
Explanation: 25 = 32.
Input/Output
[time limit] 3000ms (java)
[input] integer a
A positive integer.
Guaranteed constraints:
2 ≤ a ≤ 105.
[input] integer b
A non-negative integer.
Guaranteed constraints:
0 ≤ b ≤ 105.
[output] integer
The last digit of ab.
GIVE UP
'''


#CODE:
def lastDigit(a, b):
  res=1
  for i in range(b):
    res=(res*a)%10
  return res

#We can directly does by writing only one line as
#return (a**b)%10
#but for long number it take so much time

'''Q
Given two integers a and b, find the remainder of a when divided by b.
Example
For a = 5 and b = 3, the output should be
findTheRemainder(a, b) = 2.
Input/Output
[time limit] 4000ms (py)
[input] integer a
Guaranteed constraints:
2 ≤ a ≤ 20.
[input] integer b
Guaranteed constraints:
2 ≤ b ≤ 20.
[output] integer
GIVE UP
'''
#Code:
def findTheRemainder(a, b):
    while a >= b:
         a%= b
    return a




'''
Q.Imagine the following situation for a given integers n and k. There are n people standing in a circle. They are numbered from 1 through n in clockwise direction. The counting out begins at person #1 and continues around the circle in a clockwise direction. In each step, k-1 people are skipped and the next person is removed from the circle. The elimination proceeds around the circle (which is becoming smaller and smaller as people get removed), until only one person remains, who is announced a winner.
The task is to find the place in the initial circle that would guarantee a win.
Example
For n = 3 and k = 2, the output should be
josephusProblem(n, k) = 3.
Check out the image below for better understanding:

Input/Output
[time limit] 4000ms (py)
[input] integer n
A positive integer representing the number of people.
Guaranteed constraints:
3 ≤ n ≤ 10.
[input] integer k
A positive integer.
Guaranteed constraints:
2 ≤ k ≤ 10.
[output] integer
The index of the winning place.
GIVE UP
'''

#Code:
def josephusProblem(n, k):

    removed = []
    currentPerson = 0

    for i in range(n):
        removed.append(False)

    for i in range(1, n):
        skipped = 0
        while skipped < k - 1:
            if not removed[currentPerson]:
                skipped += 1
            currentPerson = (currentPerson+1)%n
        while removed[currentPerson]:
            currentPerson = (currentPerson + 1) % n
        removed[currentPerson] = True

    for i in range(n):
        if not removed[i]:
            return i + 1




'''Q.
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
Example
For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
Input/Output
[time limit] 4000ms (py)
[input] array.integer inputArray
Guaranteed constraints:
3 ≤ inputArray.length ≤ 10,
-15 ≤ inputArray[i] ≤ 15.
[output] integer
The maximal absolute difference.
GIVE UP
'''


#Code:

def arrayMaximalAdjacentDifference(inputArray):
    ans = 0
    for i in range(1, len(inputArray)):
        if abs(inputArray[i] - inputArray[i - 1]) > ans:
            ans = abs(inputArray[i] - inputArray[i - 1])
    return ans






'''Q.
Given a positive integer n, construct a number which has a single 1 bit, which is at the position of the least significant 1 bit in n.
Example
For n = 12, the output should be
leastSignificantBit(n) = 4.
12 (decimal) = 1100 (binary).
The least significant bit is the second from the left, so the answer is 100 (binary) = 4 (decimal).
Input/Output
[time limit] 4000ms (py)
[input] integer n
A positive integer.
Guaranteed constraints:
10 ≤ n ≤ 550.
[output] integer
GIVE UP
'''
#Code:
def leastSignificantBit(n):

    ans = 1
    while ((n & 1) == 0):
        n >>= 1
        ans <<= 1

    return ans




'''Q.Given array of arrays of integers sets, check whether it is possible to reorder the given arrays in such way that for each i, sets[i] will be a subset of sets[i + 1].
Example
For sets = [[1, 3, 2], [2], [1, 2], [2, 1]], the output should be
subsetsSequence(sets) = true;
For sets = [[1, 3, 2], [1, 2], [2, 3], [2]], the output should be
subsetsSequence(sets) = false.
Input/Output
[time limit] 4000ms (py)
[input] array.array.integer sets
Elements of each of the arrays are pairwise distinct.
Guaranteed constraints:
1 ≤ sets.length ≤ 10,
1 ≤ sets[i].length ≤ 5,
1 ≤ sets[i][j] ≤ 10.
[output] boolean
true if the desired reordering is possible, false otherwise.
'''
#Code:

def subsetsSequence(sets):

    def isSubset(setA, setB):
        j = 0
        for i in range(len(setB)):
            if j < len(setA) and setA[j] == setB[i]:
                j += 1
        if j == len(setA):
            return True
        else:
            return False

    supersets = [0] * len(sets)
    
    for i in range(len(sets)):
        sets[i].sort()
        
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            if isSubset(sets[i], sets[j]):
                supersets[i] += 1
            if isSubset(sets[j], sets[i]):
                supersets[j] += 1

    supersets.sort()

    for i in range(len(sets)):
        if supersets[i] < i:
            return False

    return True






'''Q.
Define a word as a sequence of consecutive English letters. Find the longest wordfrom the given string.
Example
For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".
Input/Output
[time limit] 4000ms (py)
[input] string text
Guaranteed constraints:
4 ≤ text.length ≤ 50.
[output] string
The longest word from text. It's guaranteed that there is a unique output.
GIVE UP
'''
#Code:

def longestWord(text):

    answer = ''
    current = []

    for i in range(len(text)):
        if ('a' <= text[i] and text[i] <= 'z'
                or 'A' <= text[i] and text[i] <= 'Z'):
            current.append(text[i])
            if len(current) > len(answer):
                answer = ''.join(current)
        else:
            current = []

    return answer







'''Q.
Given a rectangular matrix of integers and integers n and m, we are looking for the submatrix of size n × m that has the maximal sum among all submatrices of the given size.
Example
For
matrix = [[1, 12, 11, 10], 
          [4,  3,  2,  9], 
          [5,  6,  7,  8]]
n = 2 and
m = 1, the output should be
maxSubmatrixSum(matrix, n, m) = 19.
Input/Output
[time limit] 4000ms (py)
[input] array.array.integer matrix
2-dimensional array of integers representing a rectangular matrix.
Guaranteed constraints:
1 ≤ matrix.length ≤ 5,
1 ≤ matrix[0].length ≤ 5,
-15 ≤ matrix[i][j] ≤ 15.
[input] integer n
A positive integer not greater than the number of matrix rows.
Guaranteed constraints:
1 ≤ n ≤ matrix.length.
[input] integer m
A positive integer not greater than the number of matrix columns.
Guaranteed constraints:
1 ≤ m ≤ matrix[i].length.
[output] integer
The sum of all elements in the desired n × m submatrix.
'''
#Code:
def maxSubmatrixSum(matrix, n, m):

    result = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - m + 1):
            sumValue = 0
            for x in range(n):
                for y in range(m):
                    sumValue += matrix[i + x][j + y] 
            if i == 0 and j == 0 or sumValue > result:
                result = sumValue

    return result





'''Q.
Solve quadratic equation of the form a * x2 + b * x + c = 0 and return sorted array of all its different real roots.
Example
For a = 1, b = -3 and c = 2, the output should be
quadraticEquation(a, b, c) = [1, 2];
For a = 1, b = 2 and c = 1, the output should be
quadraticEquation(a, b, c) = [-1];
For a = 2, b = 2 and c = 1, the output should be
quadraticEquation(a, b, c) = [].
Input/Output
[time limit] 4000ms (py)
[input] integer a
Guaranteed constraints:
-50 ≤ a ≤ 50,
a ≠ 0.
[input] integer b
Guaranteed constraints:
-50 ≤ b ≤ 50.
[input] integer c
Guaranteed constraints:
-50 ≤ c ≤ 50.
[output] array.float
'''
#Code:
def quadraticEquation(a, b, c):
    if (b*b - 4 * a * c) < 0:
        return []
    
    sol1 = ((-1*b) + math.sqrt(b*b - 4*a*c))/(2*a)
    sol2 = ((-1*b) - math.sqrt(b*b - 4*a*c))/(2*a)
    
    if abs(sol1 - sol2) < 0.00000001:
        return [sol1]
    else:
        return sorted([sol1,sol2])
    




'''Q.For a given integer n, return the shortest possible list of distinct Fibonacci numbersthat sum up to n, sorted in ascending order.
Example
For n = 20, the output should be
fibonacciSum(n) = [2, 5, 13].
Input/Output
[time limit] 4000ms (py)
[input] integer n
Guaranteed constraints:
20 ≤ n ≤ 6000.
[output] array.integer
'''

#Code:
def fibonacciSum(n):

    fib = []
    fib0 = 1
    fib1 = 1
    fib.append(fib1)
    while fib1 < n:
        fib2 = fib0 + fib1
        fib.append(fib2)
        fib0 = fib1
        fib1 = fib2

    ans = []
    for i in range(len(fib) - 1, -1, -1):
        if n >= fib[i]:
            n -= fib[i] 
            ans.append(fib[i])

    return list(reversed(ans))








'''Q.You are given an array of up to four non-negative integers, each less than 256.
Your task is to pack these integers into one number M in the following way:
The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.
Return the obtained integer M.
Note: the phrase "first bits of M" refers to the least significant bits of M - the right-most bits of an integer. For further clarification see the following example.
Example
For a = [24, 85, 0], the output should be
arrayPacking(a) = 21784.
An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.
After packing these into one number we get 00000000 01010101 00011000 (spaces are placed for convenience), which equals to 21784.
Input/Output
[time limit] 4000ms (py)
[input] array.integer a
Guaranteed constraints:
1 ≤ a.length ≤ 4,
0 ≤ a[i] < 256.
[output] integer
'''
#Code:
def arrayPacking(a):

    res = 0
    for i in range(len(a)):
        res |= a[i] << (8 * i)

    return res





'''Q.
Given a rectangular matrix consisting of zeroes, replace each zero with the number of neighboring cells for that cell.
Example
For
matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
the output should be
neighboringCells(matrix) = [[2, 3, 2],
                            [3, 4, 3],
                            [2, 3, 2]]
Input/Output
[time limit] 4000ms (py)
[input] array.array.integer matrix
A rectangular matrix of zeros.
Guaranteed constraints:
1 ≤ matrix.length ≤ 5,
1 ≤ matrix[0].length ≤ 5.
[output] array.array.integer
'''
#Code:
def neighboringCells(m):
    l=len(m)
    for i in range(l):
        for j in range(len(m[i])):

            if i!=l-1:
                m[i][j]+=1
                
            if i!=0:
                m[i][j]+=1
            
            if j!=len(m[i])-1:
                m[i][j]+=1
                
            if j!=0:
                m[i][j]+=1
                
    return m







'''Q.
Given array of integers, for each position i, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position i in the answer. If no such value can be found, store -1 instead.
Example
For items = [3, 5, 2, 4, 5], the output should be
arrayPreviousLess(items) = [-1, 3, -1, 2, 4].
Input/Output
[time limit] 4000ms (py)
[input] array.integer items
Non-empty array of positive integers.
Guaranteed constraints:
3 ≤ items.length ≤ 15,
1 ≤ items[i] ≤ 200.
[output] array.integer
Array containing answer values computed as described above.
GIVE UP
'''

#Code:
def arrayPreviousLess(items):

    result = []
    for i in range(len(items)):
        substitute = -1
        for j in range(i):
            if items[j] < items[i]:
                substitute = items[j]
        result.append(substitute)

    return result







'''Q.
You are playing an RPG game. Currently your experience points (XP) total is equal to experience. To reach the next level your XP should be at least at threshold. If you kill the monster in front of you, you will gain more experience points in the amount of the reward.
Given values experience, threshold and reward, check if you reach the next level after killing the monster.
Example
For experience = 10, threshold = 15 and reward = 5, the output should be
reachNextLevel(experience, threshold, reward) = true;
For experience = 10, threshold = 15 and reward = 4, the output should be
reachNextLevel(experience, threshold, reward) = false.
Input/Output
[time limit] 4000ms (py)
[input] integer experience
Guaranteed constraints:
3 ≤ experience ≤ 250.
[input] integer threshold
Guaranteed constraints:
5 ≤ threshold ≤ 300.
[input] integer reward
Guaranteed constraints:
2 ≤ reward ≤ 65.
[output] boolean
true if you reach the next level, false otherwise.
GIVE UP
'''

#Code:
def reachNextLevel(experience, threshold, reward):
    experience += reward
    if experience >= threshold:
        return True
    return False





'''Q.
Find the smallest prime number strictly greater than the given n.
Example
For n = 7, the output should be
nextPrime(n) = 11.
Input/Output
[time limit] 4000ms (py)
[input] integer n
A positive integer.
Guaranteed constraints:
1 ≤ n ≤ 250.
[output] integer
GIVE UP
'''

#Code:
def nextPrime(n):
    n+=1
    for i in range(2,n):
        if(n%i==0):
            n+=1
            i=2
    return n






'''Q.
Given a number and a range, find the largest integer within the given range that's divisible by the given number.
Example
For left = 1, right = 10 and divisor = 3, the output should be
maxDivisor(left, right, divisor) = 9.
The largest integer divisible by 3 in range [1, 10] is 9.
Input/Output
[time limit] 4000ms (py)
[input] integer left
The left bound of the given range.
Guaranteed constraints:
-100 ≤ left ≤ right.
[input] integer right
The right bound of the given range.
Guaranteed constraints:
left ≤ right ≤ 100.
[input] integer divisor
Guaranteed constraints:
2 ≤ divisor ≤ 10.
[output] integer
Maximal integer in the range [left, right] which is divisible by divisor or -1 if there in no such number.
GIVE UP
'''
#CODE:

def maxDivisor(left, right, divisor):

    i = right
    while i >= left:
        if i % divisor == 0:
            return i
        i -= 1
    return -1






'''Q.You work in a company that prints and publishes books. You are responsible for designing the page numbering mechanism in the printer. You know how many digits a printer can print with the leftover ink. Now you want to write a function to determine what the last page of the book is that you can number given the current page and numberOfDigits left. A page is considered numbered if it has the full number printed on it (e.g. if we are working with page 102 but have ink only for two digits then this page will not be considered numbered).
It's guaranteed that you can number the current page, and that you can't number the last one in the book.
Example
For current = 1 and numberOfDigits = 5, the output should be
pagesNumberingWithInk(current, numberOfDigits) = 5.
The following numbers will be printed: 1, 2, 3, 4, 5.
For current = 21 and numberOfDigits = 5, the output should be
pagesNumberingWithInk(current, numberOfDigits) = 22.
The following numbers will be printed: 21, 22.
For current = 8 and numberOfDigits = 4, the output should be
pagesNumberingWithInk(current, numberOfDigits) = 10.
The following numbers will be printed: 8, 9, 10.
Input/Output
[time limit] 4000ms (py)
[input] integer current
A positive integer, the number on the current page which is not yet printed.
Guaranteed constraints:
1 ≤ current ≤ 1000.
[input] integer numberOfDigits
A positive integer, the number of digits which your printer can print.
Guaranteed constraints:
1 ≤ numberOfDigits ≤ 1000.
[output] integer
The last printed page number.
GIVE UP
'''

#Code:
def pagesNumberingWithInk(current, numberOfDigits):

    def countDigitsInNumber(n):
        count = 0
        while n > 0:
            count += 1
            n /= 10
        return count
    digitsInCurrent = countDigitsInNumber(current)
    while numberOfDigits >= digitsInCurrent:
        numberOfDigits -= digitsInCurrent
        current += 1
        digitsInCurrent = countDigitsInNumber(current)
    return current - 1




'''Q.Determine whether the given string can be obtained by one concatenation of some string to itself.
Example
For inputString = "tandemtandem", the output should be
isTandemRepeat(inputString) = true;
For inputString = "qqq", the output should be
isTandemRepeat(inputString) = false;
For inputString = "2w2ww", the output should be
isTandemRepeat(inputString) = false.
Input/Output
[time limit] 4000ms (py)
[input] string inputString
Guaranteed constraints:
2 ≤ inputString.length ≤ 20.
[output] boolean
true if inputString represents a string concatenated to itself, falseotherwise
'''

#Code:
def isTandemRepeat(inputString):

    length =  len(inputString)
    if length % 2 == 1:
        return False

    for i in range(length / 2):
        if inputString[i] != inputString[i + length / 2]:
            return False

    return True




'''Q.Given a reduced improper fraction output it as a reduced mixed fraction.
Example
For a = [7, 2], the output should be
improperFractionToMixed(a) = [3, 1, 2].
Explanation: 7/2 = 3 + 1/2.
Input/Output
[time limit] 4000ms (py)
[input] array.integer a
Array of two positive integers representing a reduced improper fraction a[0] / a[1].
Guaranteed constraints:
2 ≤ a[i] ≤ 25.
[output] array.integer
Array of three integers representing the reduced mixed fraction equal to a in the form b[0] + b[1] / b[2].
GIVE UP
'''

#Code:
def improperFractionToMixed(a):
        b=[a[0]/a[1],0,0]
        b[1]=a[0]-a[1]*b[0]
        b[2]=a[1]
        
        return b
        







'''Q.Given a number of the pages in some book find the number of digits one needs to print to enumerate the pages of the book.
Example
For n = 11, the output should be
pagesNumbering(n) = 13.
Input/Output
[time limit] 4000ms (py)
[input] integer n
A positive integer.
Guaranteed constraints:
1 ≤ n ≤ 108.
[output] integer
'''
#Code:
def pagesNumbering(n):
    s = 0
    d = 1
    p = 1
    while d*10 <= n:
        s += 9*d*p
        d *= 10
        p += 1
    if d <= n:
        s += (n-d+1)*p
    return s






'''Q.Your friend advised you to see a new performance in the most popular theater in the city. He knows a lot about art and his advice is usually good, but not this time: the performance turned out to be awfully dull. It's so bad you want to sneak out, which is quite simple, especially since the exit is located right behind your row to the left. All you need to do is climb over your seat and make your way to the exit.
The main problem is your shyness: you're afraid that you'll end up blocking the view (even if only for a couple of seconds) of all the people who sit behind you and in your column or the columns to your left. To gain some courage, you decide to calculate the number of such people and see if you can possibly make it to the exit without disturbing too many people.
Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.
Example
For nCols = 16, nRows = 11, col = 5 and row = 3, the output should be
seatsInTheater(nCols, nRows, col, row) = 96.
Here is what the theater looks like:

Input/Output
[time limit] 4000ms (py)
[input] integer nCols
An integer, the number of theater's columns.
Guaranteed constraints:
1 ≤ nCols ≤ 1000.
[input] integer nRows
An integer, the number of theater's rows.
Guaranteed constraints:
1 ≤ nRows ≤ 1000.
[input] integer col
An integer, the column number of your own seat (1-based).
Guaranteed constraints:
1 ≤ col ≤ nCols.
[input] integer row
An integer, the row number of your own seat (1-based).
Guaranteed constraints:
1 ≤ row ≤ nRows.
[output] integer
The number of people who sit strictly behind you and in your column or to the left.
'''

#Code:
def seatsInTheater(nCols, nRows, col, row):
    return (nCols-col+1)*(nRows-row)





'''Q
Define an integer's roundness as the number of trailing zeros in it. Sometimes it is possible to increase a number's roundness by swapping two of its digits.
Given an integer n, find the minimum number of swaps required to maximize n's roundness.
Example
For n = 902200100, the output should be
maximizeNumberRoundness(n) = 1.
It's enough to swap the leftmost 0 with 1.
For n = 11000, the output should be
maximizeNumberRoundness(n) = 0.
n already has the maximum roundness possible.
Input/Output
[time limit] 4000ms (py)
[input] integer n
A positive integer.
Guaranteed constraints:
104 ≤ n ≤ 109.
[output] integer
The minimum number of swaps required to maximize n's roundness.
'''

#Code:
def maximizeNumberRoundness(m):
    n=map(int, str(m))
    s=0
    z=0
    nz=len(n)
    for i in range(z,nz):
        z=n.index(0)
        for i in range(len(n)-1,-1,-1):
            if(int(n[i])!=0):
                nz=i
                break
        if(z<nz):
            n[z],n[nz]=n[nz],n[z]
            s+=1
    return s








'''Q.Given integers a and b, determine whether the following pseudocode results in an infinite loop
while a is not equal to b do
  increase a by 1
  decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.
Example
For a = 2 and b = 6, the output should be
isInfiniteProcess(a, b) = false;
For a = 2 and b = 3, the output should be
isInfiniteProcess(a, b) = true.
Input/Output
[time limit] 4000ms (py)
[input] integer a
Guaranteed constraints:
0 ≤ a ≤ 20.
[input] integer b
Guaranteed constraints:
0 ≤ b ≤ 20.
[output] boolean
true if the pseudocode will never stop, false otherwise.
'''

#Code:
def isInfiniteProcess(a, b):
    if(a>b):
        return True
    if(a==b):
        return False
    if(a < b):
        if((b-a)%2==0):
            return False
        else:
            return True





'''Q.
Given an array of integers, find the maximal difference among all possible pairs of its elements.
Example
For inputArray = [19, 32, 11, 23], the output should be
arrayMaximalDifference(inputArray) = 21.
Input/Output
[time limit] 4000ms (py)
[input] array.integer inputArray
Guaranteed constraints:
3 ≤ inputArray.length ≤ 10,
-50 ≤ inputArray[i] ≤ 50.
[output] integer
The maximal difference.
GIVE UP
'''

#Code:
def arrayMaximalDifference(a):
    m=0
    for i in range(len(a)):
        for j in range(1,len(a)):
            if(abs(a[j]-a[i])>m):
                m=abs(a[j]-a[i])
    return m





'''Q.Consider the Fibonacci sequence: 0 1 1 2 3 5 8 13 21 ...
We can see that 7 is the smallest 0-based index k for which F(k) has exactly 2 decimal digits.
What is the smallest index k for which F(k) has exactly n decimal digits?
Example
For n = 1, the output should be
fibonacciIndex(n) = 0;
For n = 2, the output should be
fibonacciIndex(n) = 7.
Input/Output
[time limit] 4000ms (py)
[input] integer n
Guaranteed constraints:
1 ≤ n ≤ 10.
[output] integer

Code:
def fibonacciIndex(n):

  a = 0
  b = 1
  i = 0
  while len(str(a)) < n:
    c = a + b
    a = b
    b = c
    i += 1

  return i
Q.Given an array of integers, find the rightmost round number in it and output its position in the array (0-based). If there are no round numbers in the given array, output -1.
Example
For inputArray = [0, 5, 10, 15], the output should be
rightmostRoundNumber(inputArray) = 2;
For inputArray = [1, 2, 3, 4, 5], the output should be
rightmostRoundNumber(inputArray) = -1.
Input/Output
[time limit] 4000ms (py)
[input] array.integer inputArray
Guaranteed constraints:
0 ≤ inputArray.length ≤ 10,
0 ≤ inputArray[i] ≤ 104.
[output] integer
GIVE UP
'''

#Code:
def rightmostRoundNumber(inputArray):
    ans=-1
    for i in range(len(inputArray)):
        if inputArray[i]%10==0:
            ans=i
    return ans
