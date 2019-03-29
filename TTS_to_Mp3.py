# import the necessary packages
from gtts import gTTS
import os


print("\n")


print("[INFO]: Loading Translator......")
print("Make sure you have an internet connection")
print("\n")
# Load a txt file or type along at the terminal
choice = input("would you like to load a .txt file or you prefer typing it out?. press 'y' for file and 'n' to type")
# convert user input to lower case laters
choice = choice.lower()
if choice == 'y':
    print("\n")
    print("Please parse the name or directory of the file. eg. demo.txt")
    filename = input("Please parse the name or directory of the file. eg. demo.txt  ")
    f = open(filename, "r")
    mytext = f.read()
else:
    mytext = input("Enter your Text  ")

print("[INFO]: loading languages......")
# We list out the Languages that are compatible
LANGUAGES= """
    'af':'Afrikaans',
    'sq':'Albanian',
    'ar':'Arabic',
    'hy':'Armenian',
    'bn':'Bengali',
    'ca':'Catalan',
    'zh':'Chinese',
    'zh-cn':'Chinese (Mandarin/China)',
    'zh-tw':'Chinese (Mandarin/Taiwan)',
    'zh-yue':'Chinese (Cantonese)',
    'hr':'Croatian',
    'cs':'Czech',
    'da':'Danish',
    'nl':'Dutch',
    'en':'English',
    'en-au':'English (Australia)',
    'en-uk':'English (United Kingdom)',
    'en-us':'English (United States)',
    'eo':'Esperanto',
    'fi':'Finnish',
    'fr':'French',
    'de':'German',
    'el':'Greek',
    'hi':'Hindi',
    'hu':'Hungarian',
    'is':'Icelandic',
    'id':'Indonesian',
    'it':'Italian',
    'ja':'Japanese',
    'ko':'Korean',
    'la':'Latin',
    'lv':'Latvian',
    'mk':'Macedonian',
    'no':'Norwegian',
    'pl':'Polish',
    'pt':'Portuguese',
    'pt-br':'Portuguese (Brazil)',
    'ro':'Romanian',
    'ru':'Russian',
    'sr':'Serbian',
    'sk':'Slovak',
    'es':'Spanish',
    'es-es':'Spanish (Spain)',
    'es-us':'Spanish (United States)',
    'sw':'Swahili',
    'sv':'Swedish',
    'ta':'Tamil',
    'th':'Thai',
    'tr':'Turkish',
    'vi':'Vietnamese',
    'cy':'Welsh'
"""

print(LANGUAGES)


language = input("please select ony of the abbreviations of the Languages above to translate   ")

# save to the disk
saveAs = input('SAVE AS ==  ')
print("\n")
print("[INFO]: Saving file.....")

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("%s.mp3" %saveAs)

print("\n")
print("Check the folder were you load this .py file from")
print("\n")

os.system('mpg321 ' + '%s.mp3' %saveAs )


