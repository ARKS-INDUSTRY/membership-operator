list_of_lang = ['python', 'java', 'javascript', 'html', 'css', 'sass', 'swift', 'kotlin', 'r', 'c', 'c++']

add = str(input("enter the programimg lang: ")).lower()

if add in list_of_lang:
  print('Best lang for programming is '+ add )
else:
  print("opps! something went wrong, check your spelling")