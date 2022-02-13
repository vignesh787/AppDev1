import csv
import sys
import matplotlib.pyplot as plt

f = open('data.csv','r')
c = csv.reader(f)

type = sys.argv[1]
value = sys.argv[2]

print("type",type)
print("value",value)

s=""

htm=""
html1=""

sid=[]
cid=[]
marks=[]

if type=='-s':
        for row in c:
            if value==row[0]:
                sid.append(row[0])
                cid.append(row[1])
                marks.append(int(row[2]))

        for i in range(len(sid)):
         s = s + "<tr>" + "<td>" + sid[i] + "</td>" + "<td>" + cid[i] + "</td>" + "<td>" + str(marks[i])+ "</td>" + "</tr>"


        htm = """
    <!DOCTYPE html>
    <html>
    <style>
    table, th, td {
    border:1px solid black;
    }
    </style>
    <title>Student Data</title>
    <body>
    <h1>Student Details</h1>
    <table>
    <tr>
    <th>Student id</th>
    <th>Course id</th>
    <th>Marks</th>
    </tr>
    """+s+"""
    <tr>
    <td style="text-align:center" colspan = "2" >
    Total Marks
    </td>
    <td>
    """+str(sum(marks))+"""
    </td>
    </table>
    </body>
    </html>
    """

elif type=='-c':
    for row in c:
     #   print(int(value))
      #  print("--"+row[1].strip())
        if "Course" not in row[1].strip():
        #    print(int(value)==int(row[1].strip()))
            if (int(value)==int(row[1].strip())):
            #    sid.append(row[0])
            #    cid.append(row[1])
                marks.append(int(row[2]))

    plt.hist(marks)
    plt.xlabel("Frequency")
    plt.ylabel("Marks")
    plt.savefig('my_plot.png')

    htm1 ="""
    <!DOCTYPE html>
    <html>
    <style>
    table, th, td {
    border:1px solid black;
    }
    </style>
    <title>Course Data</title>
    <body>
    <h1>Course Details</h1>
    <table>
    <tr>
    <th>Average Marks</th>
    <th>Maximum Marks</th>
    </tr>
    <tr>
    <td align="center">
    """+str(sum(marks)/len(marks))+"""
    </td>
    <td align="center">
    """+str(max(marks))+"""
    </td>
    </table>
     <img src='my_plot.png'/>
    </body>
    </html>
    """

# print("sid",sid)
# print("cid",cid)
# print("marks:",marks)
if type=='-s':
    f = open("studentoutput.html", 'w')
    f.write(htm)
if type=='-c':
    f = open("courseoutput.html", 'w')
    f.write(htm1)
else:
    htm = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Something Went Wrong</title>
    </head>
    <body>
    <h1>Wrong Inputs</h1>
    <p>Something went wrong</p>
    </body>
    </html>
    """

    f = open("output.html", 'w')
    f.write(htm)