import math as m
import pracLibrary as prac

def show_final_result():
    prac.line50()
    print("             Total score !")
    prac.line50()
    for i in range(len(premier_league_2017_2018)):
        for j in range(len(premier_league_2017_2018)):
            sum = (premier_league_2017_2018[i][1][0] * 3) + (premier_league_2017_2018[i][1][1] * 1)
        print("{0:5} {1:25} {2}".format(i+1,premier_league_2017_2018[i][0],sum))
        if i == 3:
            prac.line40()
        if i == 16:
            prac.line40()
        if i == 20:
            prac.line40()

def lose_morethan_draw():
    prac.line50()
    print("           Team lose more than draw")
    prac.line50()
    for i in range(len(premier_league_2017_2018)):
        if premier_league_2017_2018[i][1][2] > premier_league_2017_2018[i][1][1]:
            sum = premier_league_2017_2018[i][1][2] - premier_league_2017_2018[i][1][1]
            print("{0:20} {1:5}".format(premier_league_2017_2018[i][0],sum))


premier_league_2017_2018 = [["ManchesterCity",(32,4,2)],["Manchester United",(25,6,7)],
                            ["Tottenham",(23,8,7)],["Liverpool",(21,12,5)],
                            ["Chelsea",(21,7,10)],["Arsenal",(19,6,13)]
                            ,["Burnley",(14,12,12)],["Everton",(13,10,15)],
                            ["Leicester",(12,11,15)],["Newcastle",(12,8,18)],
                            ["Crystal Palace",(11,11,16)],["Bournemouth",(11,11,16)],
                            ["WestHam",(10,12,16)],["Watford",(11,8,19)],["Brighton",(9,13,16)],
                            ["Huddersfield",(9,10,19)],["Southampton",(7,15,16)],["Swansea",(8,9,21)],
                            ["Stoke",(7,12,19)],["West Bromwich",(6,13,19)]]
#(win,draw,lose)

show_final_result()
lose_morethan_draw()
