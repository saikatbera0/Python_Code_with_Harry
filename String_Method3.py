# **Strings are immutable**
Name="Saikat"

#Get String Lenght
print("Lenght is:=>",len(Name))

# Transfer to uppercase
print("After convert Uppercase:=>",Name.upper()) #Output=>SAIKAT

# Transfer to lowercase
print("After convert Lowercase:=>",Name.lower()) #Output=>saikat

#Strip Telling Cherecter
a="Hello!!!! !!!!!!"
print("After Striping:=>",a.strip("!")) #Output=>Hello

#Replace Cherecter using replace() method
print("After replacing :=>",a.replace("Hello","Hii").strip("!"))

# Split separate string as list items
print("After spliting:=>",a.split(" "))

# Captilize() Method captilize the first letter of a blog
b="Sagar Bera"
print("After Captilize:=>",b.capitalize())

# Center() Method Align to string at center 
print("After Center:=>",b.center(50))

# Count() Method count any cherecter how many time have in this word it is also apply at word
print("After Count:=>",b.count("a")) #Output:=> 2

# endswitch() methods cheaks if the string end with a given value.If yes then return True Otherwize Return False
print("a is the end letter of 'b'variable?:=>",b.endswith("a"))
print("r is the end letter of 'b'variable?:=>",b.endswith("r",0,5))

# Find() Method search first Occurance of the given value and return the index no where it is present
print("In sagar 'a' is on index no:=>",b.find("a")) #Output:=>1
print("In sagar 'f' is on index no:=>",b.find("f")) #Output:=>-1

# index() method help us to get index no of given value 
print("In sagar 'r' is on index no:=>",b.index("r")) #Output:=>4

# isalnum() cheak string is alphanumaric or not 
print("Is veriable b string is alphanumaric?:=>",b.isalnum())

# isalpha() cheak if string in A-Z or a-z
print("Is veriable b string is alpha?:=>",b.isalpha())

# islower() method cheak whether string is lowercase or not
print("Is veriable b string is lowercase?:=>",b.islower())

# isprintable() this method is cheak is any content is printeble or not if printable then return True otherwise return False
print("Is veriable b string is Printable?:=>",b.isprintable())
print("Is veriable b string is Printable?:=>","\n".isprintable())

# istitle() This method cheak when a string first letter is capital or not 
print("Is veriable b string first letter is capitel?:=>",b.istitle())

# swapcase() this method convart a string lower to uppercase and upper to lowercase
print("After Using Swapcase() method:=>",b.swapcase())

# title() this method convert the string to titlecase
print("After Convert Titlecase:=>","hello world".title())