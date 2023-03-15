import pandas as pd
import numpy as np
import re
import os
import csv
import sys
data = (['QuestionNumber','Question','Answer', 'valm', 'valf'])
def  ifqQuit(arg): #quit argument for the first name input, gender, and continue function
    if arg == 'q':
        sys.exit()
quitter = ifqQuit    
pattern = re.compile(r'[^a-zA-Z0-9]') # pattern that only allows letters ad number with no special characters
while True: # while true loop function for name asks for a name with no special characters if one is input it will error and restart the 
#question
    name = input('Ok please enter your first name without any special characters. (or q to quit)')
    if " " in name:
        print("error: your name cannot contain special characters")
    elif name == "":
        print("error: your name was not entered")
    elif pattern.search(name):
        print('error: your name contains a special character. Please enter your name only with numbers and letters')
    else:
        break
quitter(name) #exit statement
print('your name is: ', name)
gender = 'n'
while True: #while true statenebt for gender for m and f and quit if either m,f, or q is not entered it will print an error message and loop
    gender = input('Please enter your sex as "m" for male or "f" for female. or (q to quit)')
    gender = gender.lower()
    if gender not in ['m', 'f', 'q']:
        print('Error: Please enter your sex as "m" for male or "f" for female. or (q to quit')
    else:
        break
quitter(gender)
namefile = name+ ".csv" #makes your name the csv file name
hasfile = 0 #allows for file input to be characterized has 0 being does not have a file
if os.path.isfile(namefile):
    hasfile = 1 #assigned to show that the user has a file
    
continueyorn = 'n'
def newfile(hasfile, name, namefile,data):
    while hasfile == 0:  #while loop if a person does not have a csv file in the name input will create the csv file
        with open(name +'.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
            hasfile = 1
#enters in the first row headers for m and female
    else:
        print('Your CSV file has been created / already exists:')
newfile(hasfile,name,namefile,data)
while hasfile == 1: #if the person has a file it will ask if the want to continue the test or clear their results and start a new test errors out if a non y, n or q is not entered
    continueyorn = input('We found a file with your name do you want to continue taking the test?: Answer "y" for yes, or Answer "N" for no to start a new test. (or q to quit:')
    if continueyorn not in ['y', 'n', 'q']:
        print(' error: please Answer "y" for Yes or "n" for No:')
    else:
        break
quitter(continueyorn) #quits function
if hasfile == 1 and continueyorn == 'n': #this starts writing a new document if n is entered into the last equation it will rewrite the csv file
    print('read from: ' +namefile)
    with open(namefile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['QuestionNumber','Question','Answer', 'valm', 'valf']) #first row values
else: 
    



    with open(namefile, 'r') as file:  #opens and reads the first row of the csv file
        reader = csv.reader(file)
        for row in reader:
            print(row)

file = name + '.csv' #writes the first name file as a cssv file
columns = ['Qno', 'Q', 'Atext', 'Btext', 'Ctext'] # columns of the csv mfile mbti


mbti = "mbti.csv"  
sex = gender
file = name + '.csv'
columns = ['Qno', 'Q', 'Atext', 'Btext', 'Ctext']

def export_rows(mbti, file, columns, sex): #main function that calls the variables mbti, file , columns and sex variable into the function
    print(gender)
    while True:   #while true loop if they enter a wrong input it will loop back and recieve an error message
        last_row = get_last_row(file)  # Get the last row processed from the output file
        print('Welcome to the MBTI test!')
        print('please answer the following quesitons with the letter a,b, or c. or enter "q" to save and quit:')
        if last_row is not None:  #checks if there is a valid file to look up
            df = pd.read_csv(mbti)  #loads the csv file into pandas
        if last_row >= 2:   #makes it so the last row function starts at row 1 of the mbti csv file even tho there is already a row 1
            df = df.iloc[last_row + 1:] #loops through all the mbti rows
       
        if last_row >= 20: #stops at the last row and loads the brain to loading the personality test
            lastrow(last_row,file, sex)
            break
                    
        invalid_input_counts = 0    
        for index, row in df.iterrows(): #prints current question you are on
            print("Row", index + 1)
            for col in columns:
                print(col, ";", row[col]) #prints specific columns for the input
            export = input("Answer a, b, or c with the answer that you agree with more: (q to quit): ")
            if export.lower() == 'a':
                new_columns = ['Qno', 'Q', 'Atext', 'Avalm', 'Avalf']
            elif export.lower() == 'b':
                new_columns = ['Qno', 'Q','Btext', 'Bvalm', 'Bvalf']

            elif export.lower() == 'c':
                new_columns = ['Qno', 'Q','Ctext', 'Cvalm', 'Cvalf']

            elif export.lower() == 'q':
                return
            else:
                invalid_input_counts += 1
                if invalid_input_counts >= 1:
                    break
                    print('Please enter a valid answer of a, b or c. (q for quit)') #error loop
                    continue #continues to the append write to change rows
            with open(file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([row[col] for col in new_columns])
            
             # Update the last row processed in the output file

def get_last_row(file): # operates by finding last row you left off from you you can stop and take the test a different time
    # Get the last row processed from the output file
    try:
        with open(file, 'r') as f:
            last_row = sum(1 for _ in f)
            if last_row == 0:
                return None
            else:
                return last_row - 1
    except FileNotFoundError: #file not found error stop
        return None

def update_last_row(file, last_row): #updates the last row if you answer a question
    # Update the last row processed in the output file
    with open(file, 'r', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([last_row])
def lastrow(last_row,file, sex): #This is  the brain function of the pesonality test
    df = pd.read_csv(file)# it checks for what gender you are before going into the question to access the either valm or valf column
    if sex == 'm':
        df['letter'] = df['valm'].str.extract(r'([a-zA-Z]+)', expand=False)
        df['number'] = df['valm'].str.extract(r'(\d+)', expand=False).astype(int)
        result = df.groupby('letter')['number'].sum()
        df['valm'] = df['valm'].fillna(0)
        file == df.to_csv('updated_example.csv', index=False)
    if sex == 'f':
        df['letter'] = df['valf'].str.extract(r'([a-zA-Z]+)', expand=False)
        df['number'] = df['valf'].str.extract(r'(\d+)', expand=False).astype(int)
        result = df.groupby('letter')['number'].sum()
        df['valf'] = df['valf'].fillna(0)
        file == df.to_csv('updated_example.csv', index=False)
    print(result) #gives me the tally of each letter of the personality test
    E = result[0]

    I = result[2]
    J = result[3]
    N = result[4]
    P = result[5]
    S = result[6]
    T = result[7]
    F = result[1]
    if I >= E: #Checks to see which letter has the higher number of score and compares them and assigns the higher letter to A1 being the number of points
# A11 being the letter itself etc
        A1 = I
        A11 =result.index[2]
    else:
        A1 = E
        A11 = result.index[0]
    if N >= S:
        A2 = N
        A21 = result.index[4]
    else:
        A2 = S
        A21 = result.index[6]
    if F >= P:
        A3 = F
        A31 = result.index[7]
    else:
        A3 = P
        A31 = result.index[1]
    if P >= J:
        A4 = P
        A41 = result.index[3]
    else:
        A4 = J
        A41 = result.index[5]
    print("your dominant trait letters are: ", A11, A1, A21, A2, A31, A3, A41, A4) #prints your highest letter and number of points per letter
    print("your personality is:",A11,A21,A31,A41) #personality trait 4 letter
    final = A11+A21+A31+A41+ ('.txt')#sets it as a txt file to open the adjacent 4 letter memo about your personality type
    print(final)
    print('this is what your personality trait says about you', final)
    with open(final, 'r') as file: #opens the 4 letter text file to describe your personality trait
        file_contents = file.read()
        print(file_contents)


    

export_rows(mbti, file, columns, sex)









            
            

                
    
            
        
            
    

    
    
    
