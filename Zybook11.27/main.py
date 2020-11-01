#Githin Kurian
#1580561

def roster():
   keys = list(ply.keys())

   keys.sort()

   print("ROSTER")
   for i in keys:
       print("Jersey number: %d, Rating: %d" %(i,ply[i]))

ply = {}

for i in range(5):
 
   jno = int(input("Enter player %d's jersey number:\n" %(i+1)))
  
   ply[jno] = int(input("Enter player %d's rating:\n" %(i+1)))
  
   print("")
  


roster()

while True:

   
   print('\nMENU\na - Add player')
   print('d - Remove player')
   print('u - Update player rating')
   print('r - Output players above a rating')
   print('o - Output roster')
   print('q - Quit\n')
  
   op = input("Choose an option:\n")  
  
   if op == 'o':
       roster()
    
   elif op == 'a':

       jno = int(input("Enter a new player's jersey number: \n"))
      
       rating = int(input("Enter the player's rating:\n"))
      

       ply[jno] = rating
  
   elif op == 'd':
      
       jno = int(input("Enter a player's jersey number: \n"))
      

       if jno in list(ply.keys()):
       
           del ply[jno]
  

   elif op == 'u':

       jno = int(input("Enter a player's jersey number: \n"))
      
       
       rating = int(input("Enter a new rating for player:\n"))
      
       ply[jno] = rating
      
   elif op == 'r':
      
       rating = int(input("Enter a rating:\n"))
      
      
       keys = list(ply.keys())

   
       keys.sort()

       print("\nABOVE %d" %(rating))
      
       c = 0
       for i in keys:
          
           if(ply[i]>rating):
               print("Jersey number: %d, Rating: %d" %(i,ply[i]))
              
               c +=1
      
       if(c == 0):
           print("No players found above %d rating" %(rating))
      

   if op == "q":
       break

   
  
