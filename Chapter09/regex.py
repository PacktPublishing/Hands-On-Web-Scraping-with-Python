"""
Python Regular Expressions: re
https://regexone.com/references/python
http://www.regular-expressions.info/python.html
https://developers.google.com/edu/python/regular-expressions
# Anchors: ^ begining of Line, $ end of line
# re.search(pattern,str,re.I|re.MULTILINE|re.M)
"""
import re

sentence = """The course assumes a working knowledge of key data science topics
(statistics, machine learning, and general data analytic methods).
Programming experience in some language (such as R, MATLAB, SAS, Mathematica, Java, C, C++, VB, or FORTRAN)
is expected. In particular, participants need to be comfortable with general programming concepts like 
variables, loops, and functions. Experience with Python is helpful (but not required)."""
#source: https://www.enthought.com/training/course/python-for-data-science/#/syllabus
splitSentence=sentence.split()

print("Length of Sentence: ",len(sentence), '& splitSentence: ',len(splitSentence))
print(splitSentence)

#Findall
matches = re.findall(r"([A-Z+]+)\,",sentence)
print("Findall found total ",len(matches)," Matches >> ",matches)
#Findall found total  6  Matches >>  ['R', 'MATLAB', 'SAS', 'C', 'C++', 'VB']

matches = re.findall(r"([A-Z]+)\,",sentence)
print("Findall found total ",len(matches)," Matches >> ",matches)
#Findall found total  5  Matches >>  ['R', 'MATLAB', 'SAS', 'C', 'VB']

matches = re.findall(r"\s*([\sorA-Z+]+)\)",sentence) #r'\s*([A-Z]+)\)' matches 'FORTRAN'
print("Findall found total ",len(matches)," Matches >> ",matches)
#Findall found total  1  Matches >>  ['or FORTRAN']


#re.match
fortran = matches[0] # 'or FORTRAN'
if re.match(r'or',fortran):
    fortran = re.sub(r'or\s*','',fortran)
print(fortran)
#FORTRAN

#re.search
if re.search(r'^F.*N$',fortran):
    print("True")
#True

matches  = re.findall(r'\s(MAT.*?)\,',sentence,flags=re.IGNORECASE)
print("(MAT.*?)\,: ",matches)  #r'(?i)\s(MAT.*?)\,' can also be used
#(MAT.*?)\,: ['MATLAB', 'Mathematica']

matches = re.findall(r'\s(MAT.*?)\,',sentence)
print("(MAT.*?)\,: ",matches)
#(MAT.*?)\,: ['MATLAB']

matches = re.findall(r'\s(C.*?)\,',sentence)
print("\s(C.*?)\,: ",matches)
#\s(C.*?)\,: ['C', 'C++']


#re.split
matchesOne = re.split(r"\W+",sentence)  #\w (word characters, \W - nonword)
print("Regular Split '\W+' found total: ",len(matchesOne ),"\n",matchesOne)
#Regular Split '\W+' found total: 63
#['The', 'course', 'assumes', 'a', 'working', 'knowledge', 'of', 'key', 'data', 'science', 'topics', 'statistics', ......, 'such', 'as', 'R', 'MATLAB', 'SAS', 'Mathematica', 'Java', 'C', 'C', 'VB', 'or', 'FORTRAN', 'is', 'expected', .........., 'and', 'functions', 'Experience', 'with', 'Python', 'is', 'helpful', 'but', 'not', 'required', '']

matchesTwo = re.split(r"\s",sentence)
print("Regular Split '\s' found total: ",len(matchesTwo),"\n", matchesTwo)
#Regular Split '\s' found total: 63 :
#['The', 'course', 'assumes', 'a', 'working', 'knowledge', 'of', 'key', 'data', 'science', 'topics', '(statistics,', ........., '(such', 'as', 'R,', 'MATLAB,', 'SAS,', 'Mathematica,', 'Java,', 'C,', 'C++,', 'VB,', 'or', 'FORTRAN)', 'is', ......., 'and', 'functions.', 'Experience', 'with', 'Python', 'is', 'helpful', '(but', 'not', 'required).']


timeDate= '''<time datetime="2019-02-11T18:00:00+00:00"></time>
<time datetime="2018-02-11T13:59:00+00:00"></time>
<time datetime="2019-02-06T13:44:00.000002+00:00"></time>
<time datetime="2019-02-05T17:39:00.000001+00:00"></time>
<time datetime="2019-02-04T12:53:00+00:00"></time>
'''

pattern = r'(20\d+)([-]+)(0[1-9]|1[012])([-]+)(0[1-9]|[12][0-9]|3[01])'
recompiled = re.compile(pattern)  # <class '_sre.SRE_Pattern'>
dateMatches = recompiled.search(timeDate)


print("Group : ",dateMatches.group())
#Group : 2019-02-11

print("Groups : ",dateMatches.groups())
#Groups : ('2019', '-', '02', '-', '11')

print("Group 1 : ",dateMatches.group(1))
#Group 1 : 2019

print("Group 5 : ",dateMatches.group(5))
#Group 5 : 11


for match in re.finditer(pattern, timeDate): # <class '_sre.SRE_Match'>
        #for match in re.finditer(recompiled, timeDate):
        s = match.start()
        e = match.end()
        l = match.lastindex
        g = match.groups()
        print('Found {} at {}:{}, groups{} lastindex:{}'.format(timeDate[s:e], s, e,g,l))


# Found 2019-02-11 at 16:26, groups('2019', '-', '02', '-', '11') lastindex:5
# Found 2018-02-11 at 67:77, groups('2018', '-', '02', '-', '11') lastindex:5
# Found 2019-02-06 at 118:128, groups('2019', '-', '02', '-', '06') lastindex:5
# Found 2019-02-05 at 176:186, groups('2019', '-', '02', '-', '05') lastindex:5
# Found 2019-02-04 at 234:244, groups('2019', '-', '02', '-', '04') lastindex:5


pDate = r'(?P<year>[0-9]{4})(?P<sep>[-])(?P<month>0[1-9]|1[012])-(?P<day>0[1-9]|[12][0-9]|3[01])'
recompiled = re.compile(pDate)
for match in re.finditer(recompiled,timeDate):
        s = match.start()
        e = match.end()
        l = match.lastindex
        print("Group ALL or 0: ",match.groups(0)) #or match.groups()
        print("Group Year: ",match.group('year'))
        print("Group Delimiter: ",match.group('sep'))
        print('Found {} at {}:{}, lastindex: {}'.format(timeDate[s:e], s, e,l))
        print('year :',match.groupdict()['year'])
        print('day :',match.groupdict()['day'])
        print('lastgroup :',match.lastgroup)


# Group ALL or 0: ('2019', '-', '02', '11')
# Group Year: 2019
# Group Month: 02
# Group Day: 11
# Group Delimiter: -
# Found 2019-02-11 at 16:26, lastindex: 4
# year : 2019
# day : 11
# lastgroup : day


pTime = r'(?P<hour>[0-9]{2})(?P<sep>[:])(?P<min>[0-9]{2}):(?P<sec_mil>[0-9.:+]+)'
recompiled = re.compile(pTime)
for match in re.finditer(recompiled,timeDate):
        print("Group String: ",match.group())
        print("Group ALL or 0: ",match.groups())
        print("Group Span: ",match.span())
        print("Group Span 1: ",match.span(1))
        print("Group Span 4: ",match.span(4))
        print('hour :',match.groupdict()['hour'])
        print('minute :',match.groupdict()['min'])
        print('second :',match.groupdict()['sec_mil'])
        print('lastgroup :',match.lastgroup)


# Group String: 12:53:00+00:00
# Group ALL or 0: ('12', ':', '53', '00+00:00')
# Group Span: (245, 259)
# Group Span 1: (245, 247)
# Group Span 4: (251, 259)
# hour : 12
# minute : 53
# second : 00+00:00
# lastgroup : sec_mil
