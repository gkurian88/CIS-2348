#Githin Kurian
# ID: 1580561
HW # 4

def get_age(): 
    age=int(input())
    if age<18 or age >75: 
    	raise ValueError("Invalid age.") 
    return age 
  

def fat_burning_heart_rate(age): 
  
    hr=220-age 
    hr*=0.7
    return hr

if __name__=="__main__":
    try: 
        age=get_age()
        r=fat_burning_heart_rate(age)
        print("Fat burning heart rate for a",age,"year-old:",r,'bpm')
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.\n")
