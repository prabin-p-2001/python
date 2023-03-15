import os
class file:
    def Create(self):
        fname=input("\nEnter file name: ")
        if os.path.exists(fname):
            print(fname,"exist")
        else:
            f=open(fname,"x")
            print("\t\t\tfile created")


    def Write(self):
        while True:
        
            print("\n1.append \t2.write \t3.exit")
            n=int(input("\nEnter your choice: "))
            if n==1:
                fname=input("\nEnter file name: ")
                f=open(fname,"a")
                x=input("\nEnter the content: ")
                f.write(x)
                f.close()
                print("\t\t\tsuccess")

            elif n==2:
                fname=input("\nEnter file name: ")
                f=open(fname,"w")
                x=input("\nEnter the content: ")
                f.write(x)
                f.close()
                print("\t\t\tsuccess")
            elif n==3:
                print("Exited")
                break
            else:
                print("Invalid choice")

            

    def Read(self):
        fname=input("\nEnter file name: ")
        if os.path.exists(fname):
            f=open(fname,"r")
            print(f.read())
        else:
            f=open(fname,"x")
            print("\t\t\tfile does not exsit")
                    


    def delete(self):
        fname=input("\nEnter file name: ")
        if os.path.exists(fname):
            os.remove(fname)
            print("file removed")
        else:
            print("file does not exist")



obj=file()

while True:

    print("\n1.create \t2.write \t3.read \t 4.delete \t5.exit")
    ch=int(input("\nEnter your choice: "))
    if ch==1:
        obj.Create()

    elif ch==2:
        obj.Write()
    
    elif ch==3:
        obj.Read()

    elif ch==4:
        obj.delete()

    elif ch==5:
        print("Exited")
        exit()
    else:
        print("invalid choice")
