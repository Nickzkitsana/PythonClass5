from pracLibrary import line50

wantedskill = {"C#" , "Python" , "Java" ,"PHP" , "SQL" , "Go"}
applicant1skill = {"VB","C","Ruby","Java","HTML"}
applicant2skill = {"C#","HTML","R","PHP","SQL","Swift","PHP"}
applicant3skill = {"Java","C++","Ruby","JavaScript","Objective-C","Go"}
applicant4skill = {"Java","Python","Go","SQL","Swift"}
applicant5skill = {"C++","C","C#","Objective-C","JavaScript","SQL"}

compareapp1 = (len(applicant1skill & wantedskill)/len(wantedskill))*100
compareapp2 = (len(applicant2skill & wantedskill)/len(wantedskill))*100
compareapp3 = (len(applicant3skill & wantedskill)/len(wantedskill))*100
compareapp4 = (len(applicant4skill & wantedskill)/len(wantedskill))*100
compareapp5 = (len(applicant5skill & wantedskill)/len(wantedskill))*100

notmatchapp1 = (len(applicant1skill - wantedskill)/len(wantedskill))*100
notmatchapp2 = (len(applicant2skill - wantedskill)/len(wantedskill))*100
notmatchapp3 = (len(applicant3skill - wantedskill)/len(wantedskill))*100
notmatchapp4 = (len(applicant4skill - wantedskill)/len(wantedskill))*100
notmatchapp5 = (len(applicant5skill - wantedskill)/len(wantedskill))*100

print("Applicant 1 skill match : {0:,.2f}%".format(compareapp1))
print("Applicant 2 skill match : {0:,.2f}%".format(compareapp2))
print("Applicant 3 skill match : {0:,.2f}%".format(compareapp3))
print("Applicant 4 skill match : {0:,.2f}%".format(compareapp4))
print("Applicant 5 skill match : {0:,.2f}%".format(compareapp5))
line50()
print("Applicant 1 skill not match : {0:,.2f}%".format(notmatchapp1))
print("Applicant 2 skill not match : {0:,.2f}%".format(notmatchapp2))
print("Applicant 3 skill not match : {0:,.2f}%".format(notmatchapp3))
print("Applicant 4 skill not match : {0:,.2f}%".format(notmatchapp4))
print("Applicant 5 skill not match : {0:,.2f}%".format(notmatchapp5))
