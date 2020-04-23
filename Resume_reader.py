import pandas as pd
import re
def reader(x):
    
    df = pd.read_excel('Resume Headings & Subheadings.xlsx')
    headings=df['headings']
    headings=headings.dropna()

    #Atiya's code
    resume=x.split("\n")
    resume_len=len(resume)
    for i in range(resume_len):
        resume[i]=resume[i]+"\n"
    copy_headings=[]
    for i in headings:
        copy_headings.append(i)

    keys=[]
    dic={}
    value=""

    for i in range(resume_len):
        for j in headings:
            to=re.findall(r'[A-Za-z0-9-:()&.@/, \t |]+[A-Za-z0-9-:()&.@/,\t |]',resume[i])
            if len(to)!=0:
                if j == to[0].lower():
                    keys.append([to[0],i,"a"])

    key_len=len(keys)

    #Mansi's Code
    def func1():
                  

        count=-1
        head,list=[],[]

        # hd=headings.iloc[:,:-1].values.tolist()
        # for i in hd:
        #     list.append(i[0])

        
        for i in resume:
       
            count+=1
            if "\t" in i:
                r=re.findall(r'[\w\s]*?[\w]+\t',i)
                if len(r)!=0:
                    r[0]=r[0].replace('\t','')
                    if r[0].lower() in copy_headings:
                        if ([r[0],count,'a'] not in keys) or ([r[0],count,'m'] not in keys):
                            keys.append([r[0],count,"m"])
    func1()

    def func2():
        list,head=[],[]
        count=-1

        for i in resume:
            count+=1
            if ":" in i or "\t" in i or "-" in i:
#                 r=re.findall(r'[\w\s\t\n]?[\w]+[:\t-]+?[\w\n]?',i)
                r=re.findall(r'[\w\s\t\n]?[\w\s]+[:\t-\n\s]+?',i)
                if len(r)!=0:
                    for j in range(len(r)):
                        r[j]=r[j].replace(':','')
                        r[j]=r[j].replace('\t','')
                        r[j]=r[j].replace('-','')
                        if r[j].lower() in copy_headings:
                            if ([r[0],count,'a'] not in keys) and ([r[0],count,'m'] not in keys):
                                keys.append([r[0],count,"m"])

                                
    func2()

    x=[]
    for i in keys:
        x.append(i[1])
    x.sort()

    final_head=[]
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] == keys[j][1]:
                final_head.append(keys[j])
    keys=final_head


    #Atiya's Code
    dic={}
    resume_len=len(resume)
    key_len=len(keys)
    for key in range(len(keys)-1):
        if keys[key][2]=='a':
            for i in range(keys[key][1]+1,keys[key+1][1]):
                value+=resume[i]
            dic[keys[key][0]]=value
            value=""

        elif keys[key][2]=='m':
            value=""
            resume_len=len(resume)
            for i in range(keys[key][1],keys[key+1][1]):
                if i==keys[key][1]:
                    value+=resume[i].replace(keys[key][0],"")
                else:
                    value+=resume[i]
            dic[keys[key][0]]=value
            value=""
    print(keys)
    if keys[-1][2]=='a':
        for i in range(keys[key_len-1][1]+1,resume_len):
            value+=resume[i]
        dic[keys[key_len-1][0]]=value
    elif keys[-1][2]=='m':
        for i in range(keys[key_len-1][1],resume_len):
            value+=resume[i].replace(keys[key_len-1][0],"")

        dic[keys[key_len-1][0]]=value
    temp=resume[:keys[0][1]]
    about_cont=[]
    for i in temp:
        if i not in ['\n',' \n','\n ',' \n ']:
            about_cont.append(i)
    dic["about"]=''.join(about_cont)
    return dic

# x='''AKALILI BAZILAH BINTI MOHD POAT 

# NRIC 9210017-14-5592   AGE: 25     MARITAL STATUS  Single 

 

 

 

 

 

# EDUCATION 

# 2011 - 2014 Bachelor in Business Management (Hons) in Human Resource 
# Management 
# Universiti Teknologi MARA (UiTM) Seri Iskandar, Perak 
# CGPA : 3.16 
 

# 2010 – 2011 Matriculation Certificate in Accountancy 
# Perlis Matriculation College 
# CGPA: 3.26 
 

# 2008 – 2009 Sijil Pelajaran Malaysia (SPM) 
# Sekolah Menengah Teknik Setapak, Kuala Lumpur 
# SPM: 4A 3B 3D 
 

 

# PROFFESIONAL SKILLS     

#  Average Good Skilled 

# Word ● ● ● ● ● ● ● ● ●  

# Excel ● ● ● ● ● ● ● ● ○ 

# PowerPoint ● ● ● ● ● ● ● ● ○ 

# Outlook ● ● ● ● ● ○ ○ ○ ○ 

# Photoshop ● ● ● ○ ○ ○ ○ ○ ○  

# Bahasa Melayu ● ● ● ● ● ● ● ● ● 

# English ● ● ● ● ● ● ○ ○ ○ 

 



# EMPLOYMENT  

# Jun 2015 - Branch Service Operations – Adecco Staffing and Outsourcing 
# Sep 2017 Administrative Assistant – Contract Staff 

#  Perform master debit card stocks and stationaries monitoring. 
#  Download reports 
#  Perform card issuance 
#  Check statement address and reprint mailer. 
#  Perform change of address and customer’s contact details for CBOL  
#  Monitoring delivery failure as perform enrolment for undelivered 

# statements. 
#  Responsible for daily system maintenance: 

#  Activate customer’s account 
#  Delink customer’s account for housekeeping purpose 
#  Amendment of defect information 

#  Update customer deceased and staff termination 
# information status 

#  Perform chequebook maintenance as prepare chequebook order, 
# send out as per request and change of address 

 

#   Citibank Berhad (Banking) – Adecco Staffing and Outsourcing 
#   Service Admin – Contract Staff 

#  Scan new/existing AOFs/FATCA/PADD into documentum 
#  Signature scanning into Eclipse and review customer’s signature to 

# match against AOF letter forms 
#  Returned statements maker; time stamp and key in information 

# into database 
#  Responsible for system maintenance: 

#  Activate customer’s account 
#  Amendment of defect information 
#  Update Know-Your-Customer (KYC) 

#  Update customer deceased and staff termination 
# information 

#  Perform chequebook maintenance as arrange chequebook order, 
# send out as per request and change of address. 

 

# REFERENCES 
  
# How Mei Cheng +6012 201 0123 
# Assistant Manager of Branch Service Department, Citibank 
 
# Noor Zahirah Binti Mohd Zaidon +6012 677 2728 
# Assistant Manager of Branch Service Department, Citibank'''

# z=reader(x)