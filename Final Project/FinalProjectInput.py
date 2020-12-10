#Githin Kurian
#1580561
#Final Project

import csv

while True:
      inp=input('...............\n1. if you want to enter details of the product. \n2. for searching an element.\n3.q or Q for exit \n............ \nplease type an input:')
      if inp=='1':
            class details:
                  idm=int(input('enter id of the product:'))
                  nmm=input('Mnufacturer name: ')
                  tpm=input('enter type of the product')
                  dmm=input('damage if any : (leave blank if nop. indicate yes in case of damage!)')
                  pmp=int(input('enter price of the product: '))
                  sd=input('enter service date - (format (mm/dd/yyyy)) :')
            d=details()
            mn=[d.idm,d.nmm,d.tpm,d.dmm]
            pr=[d.idm,d.pmp]
            sr=[d.idm,d.sd]

            with open('ManufacturerList.csv', 'a' ,newline='') as m:
                  wm = csv.writer(m)
                  wm.writerow(mn)

            with open('PriceList.csv', 'a' ,newline='') as n:
                  wm = csv.writer(n)
                  wm.writerow(pr)

            with open('ServiceDatesList.csv', 'a' ,newline='') as o:
                  wm = csv.writer(o)
                  wm.writerow(sr)

            from operator import itemgetter

            with open('FullInventory.csv', 'r') as f:
                data = [line for line in csv.reader(f)]

            nr = [d.idm,d.nmm,d.tpm,d.pmp,d.sd,d.dmm]
            data.append(nr)

            data.sort(key=itemgetter(1))  #itemgetter(csv colmn number)

            with open('FullInventory.csv', 'w' ,newline='') as l:
                csv.writer(l).writerows(data)

            if d.tpm==('laptop' or 'Laptop' or 'LAPTOP'):

                  lap = [d.idm,d.nmm,d.pmp,d.sd,d.dmm]
                  with open('LaptopInventory.csv', 'a' ,newline='') as o:
                        wm = csv.writer(o)
                        wm.writerow(lap)

            if d.dmm==('damage' or 'DAMAGE' or 'Damage'):
                  dmin = [d.idm,d.nmm,d.tpm,d.pmp,d.sd,]
                  with open('DamagedInventory.csv', 'a' ,newline='') as o:
                        wm = csv.writer(o)
                        wm.writerow(dmin)

      elif inp=='2':
            m=input('enter manufacturer :')
            t=input('item type:')
            x=[]
            y=[]
            dp='damage\n'
            with open('FullInventory.csv', 'r') as f:
                  
                  for i in f:
                        if (m in i):
                              y.append(i)
                              ch=''.join(y)
                              if (t in i):
                                    x.append(i)
                                    z=''.join(x)
                                    if dp in z:
                                          print('No such item in inventory')
                                    else:
                                          print('Your item is:',z)
                              elif(dp in ch):
                                    print('No such item in inventory')
                              else:
                                    print('You may, also, consider:',ch)
            
                                                                                                      
      elif (inp=='q' or 'Q'):
            print('\n\n...exiting. Thankyou...\n\n')
            break
      else:
            print('\n\n...please provide a valid input...\n\n')
