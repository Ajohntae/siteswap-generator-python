#BUILDING SITESWAP GENERATOR


#Check the number of inputs
#333 = 3
#And then it would check to see if  the numbers where divisible by the number of inputs
#333 = 9 = divisible by 3
#441 = 9 = divisible by 3
#So it would take the input i.e numbers i.e (441) as an example
#& reinterpret it as( 4,4,1) check to see how many inputs there are (3)
#Add the numbers  (4+4+1 = 9 )
#Check to see if that number is divisible by the number of inputs.
#(4+4+1 = 9 % 3)
#And if it is it would return it as a valid site swap.
#Otherwise, it would return it as invalid.)

ssinput = input("Enter your Siteswap! Please remember that only Numbers are valid here.")
ssinputint = (int(ssinput))

if ssinputint == str:
    print("This character is not supported, please enter a number & try again!")

ssinputstr = str(ssinputint)
#checks length of string
length_of_ssistr = len(ssinputstr)
length_of_ssi = int(length_of_ssistr)

if length_of_ssi % ssinputint :
    print('This Siteswap ' + ssinput, ' is valid!')
else:
    print('This Siteswap ' + ssinput + 'is not valid!')
