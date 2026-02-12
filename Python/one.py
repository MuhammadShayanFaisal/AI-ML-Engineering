name="Pakistan"
print(name)
print(type(name))
print(id(name))
print([i for i in dir(name) if "__" not in i])
#  ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
#  'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
# 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
#  'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print(name.capitalize()) # captialize the single letter of First word only
print(name.casefold()) # more powerful than lower method , basically lowers the upper letters more powerful than lower
print(name.center(26,"-")) # just like padding, by default fills " "on both sides of the string of specified length, if length is less than or equal to the string, no padding is made
print(name.count("a")) # counts words or leeter in string
print(name.encode())
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace")) #uses a backslash instead of the character that could not be encoded
print(txt.encode(encoding="ascii",errors="ignore")) # ignores the characters that cannot be encoded
print(txt.encode(encoding="ascii",errors="namereplace")) # replaces the character with a text explaining the character
print(txt.encode(encoding="ascii",errors="replace")) # replaces the character with a questionmark
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))# replaces the character with an xml character

print(name.endswith("n")) # string.endswith(value,start,ends) values is required can also be tuple, whereas start and end are optional
text="S\nh\ta\ty\na\tn"
print(text.expandtabs()) # expanding tabs with string
print(name.__len__())
print(name.find("KIS",0,name.__len__())) # it dinds the substring in String 
print("Hello how are you, your age is {age}".format(age=20))
print("hello what is your name {0},and what is your age {1}".format("Shayan",20))
print("Hello what is your name {},and what is your age {}".format("Shayan",20))
price:float
my_txt = "For only {price:.2f} dollars!"
print(my_txt.format(price = 49))
txt="Left align:{:<8} characters"
print(txt.format(49))# :< Left aligns the result (within the available space)
txt="Right align:{:>8} characters"
print(txt.format(49))# :> Right aligns the result (within the available space)
txt="Centre align:{:^8} characters"
print(txt.format(49))# :^ Center aligns the result (within the available space)
txt="Centre align:{:=8} characters"
print(txt.format(49))# := Places the sign to the left most position
txt="The temperature of Karachi is: {:+} and antartica is: {:+}"
print(txt.format(49,-2))#  it is used for adding plus :+ Use a plus sign to indicate if the result is positive or negative
txt="The temperature of Karachi is: {:-} and antartica is: {:-}"
print(txt.format(49,-2)) # :- Use a minus sign for negative values only
txt="The temperature of Karachi is: {:} and antartica is: {:-}"
print(txt.format(49,-2))# : Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
txt="Comma Sign {:,} "
print(txt.format(100000))# :, Use a comma as a thousand separator
txt="underscore Sign {:_} "
print(txt.format(100000))# :_ Use a underscore as a thousand separator
txt="Binary Format Sign {:b}"
print(txt.format(123))# :b Binary format
txt="Binary Format {:c}"
print(txt.format(65))# :c Converts the value into the corresponding unicode character
txt="Decimal Format {:d}"
print(txt.format(0b1000))# :d Decimal format
txt="Scientific Format with lower case e {:e}"
print(txt.format(1000))# :e Scientific format, with a lower case e
txt="Scientific Format with upper case E {:E}"
print(txt.format(1000))# :E Scientific format, with an upper case E
txt="Fix Point Format with lower case f {:f}"
print(txt.format(1000))# :f Fix point number format
x = float('inf')
txt = "Fix point format with upper case F {:F}"
print(txt.format(x))
x = float('nan')
txt = "Fix point format with upper case F {:F}"
print(txt.format(x))# :F Fix point number format, in uppercase format (show inf and nan as INF and NAN)
print ("General format {:g}".format(12.345634))# :g General format
print ("General format with upper case E {:g}".format(0.0444563455))# :G General format (using a upper case E for scientific notations)
txt ="Octal Format: {:o}"
print(txt.format(2345))# :o Octal format
txt ="Hexa Decimal Format with lower case: {:x}"
print(txt.format(2346))# :x Hex format, lower case
txt ="Hexa Decimal Format with upper case: {:X}"
print(txt.format(2346))# :X Hex format, upper case
txt ="Number Format: {:n}"
print(txt.format(0b1010))# :n Number format
txt ="Percentage Format: {:%}"
print(txt.format(0.12))# :% Percentage format
#-------------------------------------------------------------------------------------
myvar = {"name" : "Jane", "age" : 36}
txt = "Happy birthday {name} you are now on level {age}!"
print(txt.format_map(myvar)) # format_map(dictionary) Required. A dictionary. The values in the dictionary can be formatted and used in the string.
#-------------------------------------------------------------------------------------
#string.index(value, start, end)
#value is required
# start and end is optional
txt="Hello , welcome to world"
print(txt.index('e'))
# the only differnece between find() and index() is that find() return -1 if value not found and index() return exception if value not found
#---------------------------------------------------------------------------------------
print("isalnum is: ","hello()".isalnum())
# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# Example of characters that are not alphanumeric: (space)!#%&? etc.
#------------------------------------------------------------------------------------
print("isalpha is: ","hello1".isalpha())
# It checks if the letters in the string have alphabets or not
#-------------------------------------------------------------------------------------
print("isascii is: ","hello1-ñ".isascii())
#only includes the ascii characters
# non ascii characters are like that ñ etc
#----------------------------------------------------------------------------------
print("Isdecimal"," hello".isdecimal())
print("Isdecimal",'٠'.isdecimal())   # True (Arabic-Indic digit zero)
print("Isdecimal",'²'.isdecimal())   # False
#The isdecimal() method returns True if all the characters are decimals (0-9).
# isdecimal() not includes subscript and super script
#--------------------------------------------------------------------------------
print("Isdigit","1".isdigit())
print("Isdigit",'٠'.isdigit())    # True
print("Isdigit",'²'.isdigit())    # True
#The isdigit() method returns True if all the characters are decimals (0-9).
# isdigit() includes subscript and super script
#-------------------------------------------------------------------
print("isidentifier","hello".isidentifier())
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
#-----------------------------------------------------------------------
print("islower is: ","hello".islower())
# it only checks for lower case alphabets
# Numbers, symbols and spaces are not checked, only alphabet characters.
#----------------------------------------------------------------------------
print("isnumeric is: ","2".isnumeric())
# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values.
# "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
# if there are alphabets letter sthen false
#negative numbers are also considered false
#------------------------------------------------------------------------------
print("isprintable is: ","Hello\t".isprintable())
# it checks if the text is printable then return true otherwise false
# Non printable characters are \n, \t 
#-------------------------------------------------------------------------
print("isspace is: "," ".isspace())
# it checks if all characters in the string have only whitespace characters 
#-----------------------------------------------------------------------------
print("istitle is: ","hello".istitle())
# Return True if the string is a title-cased string, False otherwise.
# In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.
# uncased characters follows upper cased and cased characters follows lower cased
#-----------------------------------------------------------------------------
print("isupper is: ","111H".isupper())
# isupper only checks if the charatcers are upper cased or not
#Numbers, symbols and spaces are not checked, only alphabet characters.
#------------------------------------------------------------------------
print("Join is: ",'.'.join('ab'))
print("Join is: ",'.'.join(txt))
mytuple=('Peter','Vicky')
print("Join is: ",'.'.join(mytuple)) # Join with tuple
mydic={"name":"John","Age":20}
mySeparator = "TEST"
print("Join is: ",mySeparator.join(mydic)) # Join with dictionary
#When using a dictionary as an iterable, the returned values are the keys, not the values.
#---------------------------------------------------------------------------------------
print("ljust is: ","Hello".ljust(10)+"hi")
#string.ljust(length, character)
#length is required
#character is optional, by default character is space " "
# we can enter only one character
print("ljust is: ","Hello".ljust(10,'_')+"hi")
#---------------------------------------------------------------------------
print("SHAYAN".lower())
# Symbols and Numbers are ignored.
#---------------------------------------------------------------------------
print("lstrip is:"+"           Hell o   s".lstrip()) #only removes the set of characters from left
#string.lstrip(characters) chaarcters is optional, by default it is space
# we can enter more characters as well
print("lstrip is:"+"!?*(#$)&^$!#*(^hell os!@#$%^&*%$#@".lstrip('!?*(#$)&^$e'))
# it identifies the string which is not removable by matching the characters in the argument
#------------------------------------------------------------------------------------
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print("maketrans: ",txt.translate(mytable))
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print("maketrans: ",txt.translate(mytable))
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print("maketrans: ",txt.translate(mytable))
#-------------------------------------------------------------------------------------
print("Partition is : ","hello".partition('o'))
# if the separator is found, then break the string in three parts like:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match" 
# return the tuple with three size
# if the separator is found, then return the orignal string in one part, then two empty strings
#it searches from left to right
#-------------------------------------------------------------------------------------
print("removeprefix is : ","llohe".removeprefix('he'))
# Return a str with the given prefix string removed if present.
# REMEMBER it is case sensitive means if the prefix id TXT then prefix in string is: TXT.a
# If the string starts with the prefix string, return string[len(prefix):].
# Otherwise, return a copy of the original string.
#------------------------------------------------------------------------------
print("removesuffix is : ","hello".removesuffix('u'))
# Return a str with the given suffix string removed if present.

# If the string ends with the suffix string and that suffix is not empty,
# return string[:-len(suffix)]. Otherwise, return a copy of the original
# string.
#------------------------------------------------------------------------------------
print("Replace is : ","Hello".replace('H','o'))
# Syntax: string.replace(oldvalue, newvalue, count)
# oldvalue: Required substring in the string
# newvalue: Required substring in the string to be replaced
# count: Optional count of how many substrings will be replaced by newvalue
# All occurrences of the specified phrase will be replaced, if nothing else is specified.
# default is all old value will be replaced
#-------------------------------------------------------------------------------------
print("rfind is : ","hello".rfind('e'))
print("rfind is : ","hello".rfind(' '))
print("rfind is : ","hello, welocme to the world".rfind('world'))
print("rfind is : ","hello, welocme to the world".rfind('world',5,10))
# Syntax: string.rfind(value, start, end)
# value is required
# start and end are index of string it is optional, default start is 0 and daefault end is the lengthodf string -1
# it finds the value from end by default
# if value not found then return -1
#---------------------------------------------------------------------------------------
print("rindex is : ","hello".rfind('e'))
print("rindex is : ","hello".rfind(' '))
print("rindex is : ","hello, welocme to the world".rfind('world'))
print("rindex is : ","hello, welocme to the world".rfind('world',5,10))
#rindex is amost same as rfind but in return rindex return exception whereas rfind return -1
# Syntax: string.rfind(value, start, end)
# value is required
# start and end are index of string it is optional, default start is 0 and daefault end is the lengthodf string -1
# it finds the value from end by default
# if value not found then return exception
#--------------------------------------------------------------------------------
print("rjust is:"+"hello".rjust(10)+'hi')
print("rjust is:"+"hello".rjust(10,'_')+'hi')
print("rjust is:"+"hello".rjust(10,'_')+'hi')
#string.rjust(length, character)
#length is required
#character is optional, by default character is space " "
# we can enter only one character
#-----------------------------------------------------------------------------------
print("rpartiton is: ","h-1ello-1".rpartition('-1'))
 #the only difference between partition and rpartition is the direction that:
# partition is left to right and rpartition is right to left
# # if the separator is found, then break the string in three parts like:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match" 
# return the tuple with three size
# if the separator is found, then return the  then two empty strings in two parts and then original string
#----------------------------------------------------------------------------------------
print("rsplit is: ","hello".rsplit())
# string.rsplit(separator, maxsplit)
# both separator and max split is optional 
# it also searches from right to left
# max split is buy default -1 which means all occurences
# When maxsplit is specified, the list will contain the specified number of elements plus one.
txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print("rsplit is: ",x)
#----------------------------------------------------------------------------------
print("rstrip is:"+"  Hell o   s-        ".rstrip()+"Shayan") #only removes the set of characters from right
#string.rstrip(characters) chaarcters is optional, by default it is space
# we can enter more characters as well
print("rstrip is:"+"!?*(#$)&^$!#*(^hell os !#$^&*$#".rstrip('!?*(#$)&^$e')+"Shayan")
# it identifies the string which is not removable by matching the characters in the argument
#------------------------------------------------------------------------------------------
print("Hello".split("e"))
print("split is: ","hello".split())
# string.split(separator, maxsplit)
# both separator and max split is optional 
# it also searches from left to right
# max split is buy default -1 which means all occurences
# When maxsplit is specified, the list will contain the specified number of elements plus one.
txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split(", ", 1)
print("split is: ",x)
#-----------------------------------------------------------------------------
print("hello\t hello".splitlines())
# string.splitlines(keeplinebreaks)
# where keeplinebreaks is optional boolean value by default it is false
# false means not including '\n' component in list, true means including this component
print("splitlines is: ","hello\n hello".splitlines())
#----------------------------------------------------------------------------
print("starts with: ","hello".startswith('h'))
#string.startswith(value, start, end)
# value is required can be character, string or tuple
# start and end is optional
# returns boolean value
print("starts with: ","hello, welcome to new world!".startswith('we',7,10))
txt = "Hi, welcome to my world."
x = txt.startswith(("Hello", "Hi"))
print("starts with: ",x)
#---------------------------------------------------------------------------------------
print("strip is:"+"  Hell o   s-        ".strip()+"Shayan") #only removes the set of characters from any direction e.g( right or left )
#string.strip(characters) characters is optional, by default it is space
# we can enter more characters as well
# The strip() method removes any leading, and trailing whitespaces.
# Leading means at the beginning of the string, trailing means at the end.
print("strip is:"+"!?*(#$)&^$!#*(^hell os !#$^&*$#".strip('!?*(#$)&^$e')+"Shayan")
# it identifies the string which is not removable by matching the characters in the argument
#------------------------------------------------------------------------------------------
print("swapcase is: "+"Hello".swapcase())
# converts uppercase into lower case and vice versa
#---------------------------------------------------------------------------------------
print("title is: "+"hello welcome".title())
# converts first  alphabet letter to upper case, then with remaining with lower case
# If the word contains a number or a symbol, the first letter after that will be converted to upper case.
print("title is: ","Hello you are 1st in the class".title())
print("title is: ","hello b2b2b2 and 3g3g3g".title())
#-----------------------------------------------------------------------------------------
mydict = {83: 80}
txt = "HeSllo Sam!"
print(txt.translate(mydict))
# Syntax: string.translate(table)
# table is required either a dictionary or mapping table
# If a character is not specified in the dictionary/table, the character will not be replaced
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print("translate is: ",txt.translate(mytable))
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print("translate is: ",txt.translate(mytable))
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print("translate is: ",txt.translate(mytable))
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print("translate is: ",txt.translate(mydict))
#-----------------------------------------------------------------------------------------------
print("upper is: ","hello".upper())
#convert letter in to upper case
# numbers and symbols are ignored
#--------------------------------------------------------------------------------------
print("zfill is: ","hello".zfill(6))
# Syntax: string.zfill(len)
# where len is required, A number specifying the desired length of the string
#If the value of the len parameter is less than the length of the string, no filling is done.
# it always fill zeros with beginning
a = "hello"
b = "welcome to the jungle"
c = "10.000"
print("zfill is: ",a.zfill(10))
print("zfill is: ",b.zfill(10))
print("zfill is: ",c.zfill(10))
#--------------------------------------------------------------------
name : int = 2000
print(name) # print
print(type(name)) # type
print(id(name)) # physcial address
print([i for i in dir(name) if "__" not in i])
# ['as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 
# 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
print("as integer ratio is: ",0.3333333.as_integer_ratio())
print("as integer ratio is: ",0.0.as_integer_ratio())
print("as integer ratio is: ",2.5.as_integer_ratio())
a=8
print("as integer ratio is: ",a.as_integer_ratio())
#---------------------------------------------------------------------------------------
print("bit count is: ",a.bit_count())
# basically converts an integer number into binary , then counts no.of 1's
# only applicable on integers, not applicable on float
#---------------------------------------------------------------------------------------
print("bit length is: ",a.bit_length()) #total binary numbers
#--------------------------------------------------------------------------------------
print("Conjugate is: ",(3-4j).conjugate()) # converts one complex number into its oppsoite iota sign
#------------------------------------------------------------------------------------------
from fractions import Fraction
b=Fraction(11, 35)
print("Denominator is: ",b.denominator)
print ("Denominator is: ",Fraction(10, 18).denominator)
print ("Denominator is: ",Fraction().denominator) # it doesnot require square bracket when calling denominator
#-----------------------------------------------------------------------------------------
print("from_bytes is: ",int.from_bytes(b'\x00\x10', byteorder='big'))# 16
print("from_bytes is: ",int.from_bytes(b'\x00\x10', byteorder='little'))#4096
print("from_bytes is: ",int.from_bytes(b'\xfc\x00', byteorder='big', signed=True)) #-1024
print("from_bytes is: ",int.from_bytes(b'\xfc\x00', byteorder='big', signed=False))#64512
print("from_bytes is: ",int.from_bytes([255, 0, 0], byteorder='big'))#16711680
#-----------------------------------------------------------------------------------
print("imag is: ",(2-4j).imag)
print("imag is: ",0.0.imag) # no brackets in imag
z=3
print("imag is: ",z.imag)
#-----------------------------------------------------------------------------------
print("is_integer is: ",3.1.is_integer()) # false because it is float
print("is_integer is: ",4.0.is_integer())# true becaue it is integer
a=5
b=10.0
c=5.1
print("is_integer is: ",a.is_integer())
print("is_integer is: ",b.is_integer())
print("is_integer is: ",c.is_integer())
#---------------------------------------------------------------------------------
from fractions import Fraction
my_fraction = Fraction(3, 4)
numerator_value = my_fraction.numerator
print("The numerator is: ",numerator_value)
#------------------------------------------------------------------------
print("real is: ",(2-4j).real)
print("real is: ",0.0.real) # no brackets in real
z=3
print("real is: ",z.real)
#---------------------------------------------------------------------------
num = 10
byte_data = num.to_bytes(2, 'big')
print("to_bytes is: ",byte_data)
# Syntax
# int.to_bytes(length, byteorder, *, signed=False)
#  Parameters
# length: The number of bytes the integer should occupy.
# byteorder: The byte order used to represent the integer. It can be: 'big': Most significant byte first (big-endian). 'little': Least significant byte first (little-endian).
# signed: (Optional) If True, allows the representation of negative numbers. Default is False (unsigned).
num = 10
byte_rep = num.to_bytes(2, 'little')
print("to_bytes is: ",byte_rep)
num = -10
byte_rep = num.to_bytes(2, 'big', signed=True)
print("to_bytes is: ",byte_rep)
#----------------------------------------------------------------------------------
name : float = 7.0
print(name) # print
print(type(name)) # type
print(id(name)) # physcial address
print([i for i in dir(name) if "__" not in i]) # methods and attributes
# ['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
print("as_integer_ratio is: ",3.2.as_integer_ratio())
print("conjugate is: ",2.0.conjugate())
print("fromhex is: ",3.1.fromhex('0x1.ffffp10'))
print("fromhex is: ",3.0.fromhex('-0x1p-1074'))
hex_string = "48656c6c6f20576f726c64"  # Hex representation of "Hello World"
byte_data = bytes.fromhex(hex_string)
print("bytes_data is: ",byte_data)
print("bytes_data is: ",3.0.hex()) # hex()-> Return a hexadecimal representation of a floating-point number.
print("imag is: ",0.0.imag)
print("imag is: ",(3.1+4.3j).imag)
print("is_integer is: ",3.1.is_integer())# Return True if the float is an integer.
print("real is: ",0.0.real)
print("real is: ",(3.1+4.3j).real)
#------------------------------------------------------------------------------
name : bool = True
print(name) # print
print(type(name)) # type
print(id(name)) # physcial address
print([i for i in dir(name) if "__" not in i]) # methods and attributes
# ['as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 
# 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
print(True.as_integer_ratio())
print(False.as_integer_ratio())
print(True.bit_count()) # only count 1 's in binary number of the digit
print(False.bit_count())
print(True.bit_length()) # returns the number of bits required to represent the absolute value of the integer in binary, excluding the sign bit and leading zeros.
print(False.bit_length())# it gives zero since it dosnot count leading zeros
print(True.conjugate())
print(False.conjugate())
print(True.denominator)
print(False.denominator)
print(True.imag)
print(False.imag)
print(True.is_integer())
print(False.is_integer())
print(True.numerator)
print(False.numerator)
print(True.real)
print(False.real)
# Convert True to bytes
bool_value_true = True
bytes_value_true = bool_value_true.to_bytes(1, byteorder='big')
print(f"True as bytes: {bytes_value_true}")

# Convert False to bytes
bool_value_false = False
bytes_value_false = bool_value_false.to_bytes(1, byteorder='big')
print(f"False as bytes: {bytes_value_false}")
#---------------------------------------------------------------------------------
name : list[str] = ['a','b','c']
print(name) # print
print(type(name)) # type
print(id(name)) # physcial address
print([i for i in dir(name) if "__" not in i]) # methods and attributes
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop','remove',
#  'reverse', 'sort']
print(name.append(0))
print(type(name[3]))
# print(name.clear())
print(name.copy())
print(name.count('a'))
t:tuple=(1,2)
name.extend(t)
print(name) #extend with other data type values




