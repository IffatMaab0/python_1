x=int(input("enter a number: " ))
match x:
      case 1:
           print("its monday")
      case 2:
           print("its tuesday")  
      case 3:
           print("its wednesday")
      case 4:
           print("its thurday")
      case 5:
           print("its friday")
      case 6:
           print("its saturday")
      case 7:
           print("its sunday")
      case _ if(x<1 and x >7): 
           print("Enter a Valid Number!")