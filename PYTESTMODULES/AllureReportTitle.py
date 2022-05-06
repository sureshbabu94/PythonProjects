title = "EXPLEO"
'''
with open('C:\\PythonProjects\\allureresults\\widgets\\summary.json','r+') as report:
   x = report.read().replace("Allure Report", title)
with open('C:\\PythonProjects\\allureresults\\widgets\\summary.json','w+') as report:
    report.write(x)
'''