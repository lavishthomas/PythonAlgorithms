'''{a,e,i,o,u,A,E,I,O,U}

Natural Language Understanding is the subdomain of Natural Language Processing where people used to design AI based applications have ability to understand the human languages. HashInclude Speech Processing team has a project named Virtual Assistant. For this project they appointed you as a data engineer (who has good knowledge of creating clean datasets by writing efficient code). As a data engineer your first task is to make vowel recognition dataset. In this task you have to find the presence of vowels in all possible substrings of the given string. For each given string you have to print the total number of vowels.

 

Input

First line contains an integer T, denoting the number of test cases.

Each of the next lines contains a string, string contains both lower case and upper case .

Output

Print the vowel sum
Answer for each test case should be printed in a new line.

Input Constraints

1<=T<=10

1<=|S|<=100000

 

 

SAMPLE INPUT 
1
baceb
SAMPLE OUTPUT 
16
Explanation
First line is number of input string, In given example, string is "baceb" so the substrings will be like -"b, ba, bac, bace, a, ac, ace, aceb, c, ce, ceb, e, eb, baceb" now the number of vowels in each substring will be 0, 1, 1, 2, 1, 1, 2, 2, 0, 1, 1, 1, 1, 2  and the total number will be sum of all presence which is 16.

Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Marks are awarded when all the testcases pass.
Allowed Languages:	Bash, C, C++, C++14, C++17, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, R(RScript), Racket, Ruby, Rust, Scala, Swift, Swift-4.1, TypeScript, Visual Basic
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
vowels = {'a','e','i','o','u','A','E','I','O','U'}

testcases = input ()

for i in range (0,int(testcases)):
    total_count = 0
    string = input()
    string_len = len(string)
    substrings = []
    for i in range(0,string_len):
        for j in range(i,string_len):
            substring = string[i:j+1]
            if substring not in substrings:
                substrings.append(substring)
                for char in substring:
                    if char in vowels:
                        total_count += 1

            
    #print (substrings)
    print (total_count)