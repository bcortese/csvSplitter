#!/usr/bin/python

from Tkinter import *
root =Tk()
root.title("CSV_Splitter")
root.geometry("360x260+0+0")
fields = 'File Path:', 'Header Key:', 'Footer Key:', 'File Count:'

#get the file path
labelFilePath = Label(root, text="File Path:").place(x=50, y=40) 
filePath = StringVar()
entry_box_FilePath = Entry(root, textvariable=filePath, width=25, bg="white").place(x=150, y=40) 

#get the hdr key
labelHDRKey = Label(root, text="Header Key:").place(x=50, y=60) 
strHDR = StringVar()
entry_box_HDR = Entry(root, textvariable=strHDR, width=25, bg="white").place(x=150, y=60)

#get the ftr key
labelFTRKey = Label(root, text="Footer Key:").place(x=50, y=80) 
strFTR = StringVar()
entry_box_FTR = Entry(root, textvariable=strFTR, width=25, bg="white").place(x=150, y=80)

#get the amount of files user wants to split file into
labelFileCount = Label(root, text="File Amount:").place(x=50, y=100) 
intFileAmt = IntVar()
entry_box_FileAmt = Entry(root, textvariable=intFileAmt, width=25, bg="white").place(x=150, y=100)


#get the data delimiter
labelFileCount = Label(root, text="Delimiter:").place(x=50, y=120) 
strDelim = StringVar()
entry_box_Delim = Entry(root, textvariable=strDelim, width=25, bg="white").place(x=150, y=120)




def splitCSV():
	#!/usr/bin/env python
	# -*- coding: cp1252 -*-
	import csv
	
	
	i=1
	globalx = 0
	ftrCount = 0 
	ftrString = strFTR.get().split()
	
	#count the amount of bills within data file.
	with open(filePath.get()) as f:
		     
		for lineStr in f:              
			if any(s in lineStr for s in ftrString):
				ftrCount+=1
				print("Amount of Footers:%i" %ftrCount)
				print(ftrString)
	
	
	
	with open(filePath.get()) as csvfile:
		
	
		count = 0
		mylist = []
		outputList = []
		readCSV = csv.reader(csvfile, delimiter=strDelim.get())
		docCount=0
		ftrAmount = 0
		ftrCounter=0
	
	
		recordsPerFile = ftrCount/intFileAmt.get()
		print("records per file %s" %str(recordsPerFile))
	
		while(docCount<=intFileAmt.get()):
		
			docCount+=1
			#print("break and making a new file. %s" %str(docCount))
			if(docCount<=intFileAmt.get()):
				with open(filePath.get()+"%x.csv" %docCount, "wb") as file:
					print("RELOOP")
		
					for line, row in enumerate(readCSV):
			
							writer = csv.writer(file)
							mylist.append(row)
		
							if(row[0]==strFTR.get()):																
								if(count>=recordsPerFile):		
									count=0
									break				
								else:										
									if(ftrCounter!=ftrCount):
										writer.writerows(mylist)
										count+=1
										ftrCounter+=1
										#print("found a footer the count is %s" %str(count))
										#print("found a doccount the count is %s" %str(docCount))							
										del mylist[:]
										
							globalx+=1

			       	
		        
		        		
	file.close()	
# create button to call split file
splitBtn = Button(root, text="Split", command=lambda: splitCSV())
splitBtn.pack()

root.mainloop()
