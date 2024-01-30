#DataTYpes:(1)
'''Integer:2 300 200
,Floating point: 2.3 4.5 1000.0
,strings:"10","ten " " " "##" ,
 lists:['store any data type'] [1 , "1", "one", 1.0,["store any data type"]]
,dictionary:
,Tupules,Sets,Booleans'''


#python number:OPerators:
'''
** [From R to L]
/ * % {from L to R}
+ -  {from L to R}

'''

#creation and assigninging variables
'''So that we can reference them [refer the variable to access that data]
RULESl:
1.lowercase generally [not mandatory]
2.Python uses Dynamic Typing__
my_dogs =2
my_dogs="Laddu"
print(my_dog)

p:fast and less time ,c: lead to bugs , need to know type()
s=1,sr=0.1,new_s=s*sr.THen what will be the type of nw_s
'''

#String Intro
'''
'hello'
"hello"
" I don't do that"
1.are ordered so can USE Indexing and Access that character
    {form}==[start:stop:steps]  NOTE:"stop" will not to included
    str="MyString"
    \\: to use slash 
    \": to use this->" in string 
    \': same 
    \n: to make new line
    \t: to indent 
2. reverse Indexing 
'''
#String slicing using Indexing
'''
1. Grab a single character suppose 
1 is default 
my_str="ABCDEFG"
my_str[-1]
my-str[0]
my_str=[1]
2. Grab group of chars
my_str[2:]
my_str[:4]
my_str[2:5]

3. How steps work
my_str[1:5:1]
my-str[1:5:2]
my-str[::1]

3.1 Reverse the string using step fn
my_str=[::-1]
alternate for pros::


'''
#String :Properties
'''
1. string is immutable
name="bro"
if i wnat to make this bro to pro
pro=pro
bro=p+bro[0:]
????
here
:first we ll grab the neeeded chars. here is 'ro'
new_name=name[1:]
:add required new chars to make a change 
new_name='p'+name[1:]
new_name+=name[2:]
The above method or way also called concatenation
but need to know corrrect dataType to make concatenation possibble
    1+"1"=??
    1+1=??
    "1"+"1"=??
2. How to edit the string w/o making a new string [here edit means to make it upper lower ]
my_str.upper()
Pro tip: need to use these--> () , to make the funtion work

3.Split method: return a new string , not edit the existing string 
x.split[:3]
can be assinght to a new variable suppose y =x.split[1:]
'''

#print formatting with string
''''''

