Set Shell = CreateObject("WScript.Shell")
Shell.CurrentDirectory = "C:\Users\Manuel\Documents\Projects\DailyRecap" 
Shell.Run "npm run start", 0, False