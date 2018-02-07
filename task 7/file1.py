import csv
with open("data.csv", "w") as fw:
    dataToBeSaved = [
        ["Name", "Email", "Mobile", "University", "Major"]
    ]
    fileobj = csv.writer(fw, delimiter=",")
    name = input("Enter Name or Stop to cancel : ")
    if name.lower() != "stop":
        Email = input("Enter Email: ")
        Mobile = input("Enter Mobile: ")
        University = input("Enter University: ")
        major = input("Enter Major: ")
        dataToBeSaved.append([name, Email, Mobile, University, major])
        while True:
            name = input("Enter Name or Stop to cancel: ")
            if name.lower() == "stop":
                break
            else:
                dataToBeSaved.append([name,input("Enter Email: "),input("Enter Mobile: "),input("Enter University: "),input("Enter Major: ")])
    fileobj.writerows(dataToBeSaved)
