name=input("ingrese su nombre: ")
age=int(input("ingrese su edad: "))
if(age>=18):
    id=input("ingrese su cedula: ")
    civilstatus=input("ingrese su estado civil: ")
    exdata=input("Tiene trabajo? SI/NO: ")
    if(exdata=="SI"):
        print("\nNombre:  "+name+"\n"+"edad: "+str(age)+"\n"+"id: "+id+"\n"+"estado civil"+civilstatus+"\n"+"estado laboral: empleado")
    elif(exdata=="NO"):
        print("\nNombre:  "+name+"\n"+"edad: "+str(age)+"\n"+"id: "+id+"\n"+"estado civil"+civilstatus+"\n"+"estado laboral: desempleado")
else:
    Family=input("con quien vive?: ")
    print("\nno es mayor de edad"+"\nvive con su: "+Family)