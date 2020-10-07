#Githin Kurian
#1580561

month={ "january":"1","february":"2", "march":"3","april":"4", "may":"5", "june":"6","july":"7", "august":"8", "september":"9","october":"10", "november":"11", "december":"12"}
x=open('C:\\Users\\yassn\\OneDrive\\Desktop\\a.txt', 'r')
y=open('C:\\Users\\yassn\\OneDrive\\Desktop\\b.txt','w')
for each in x:
    if each!="-1":
        lis=each.split()
        if len (lis) >=3:
            mon=lis [0]
            day=lis[1]
            year=lis [2]
            if mon.lower() in month:
                comma=day[-1]
                if comma==',':
                    day=day[:len (day)-1]
                    number=month[mon.lower()]
                    ans=number+"/"+day+"/"+year

                    y.write (ans)
                    y.write("\n")
y.close()
x.close()
