#!/usr/bin/env python
# -*- coding: utf-8 -*-

fichier = open("data.txt", "r")
readl = fichier.readlines()
tab=[]
bool = True
admis = ajourn = dette = max = 0
min=20
for line in readl: #allignement
    tab.append(line.split("\t"))
del tab[len(readl)-1] #line zyada te3 iman
#methode 2
#line.append("mention")

for line in tab: #ajoute la colonne mention
    if bool==True:
        line.append("Mention")
        bool = False
    elif float(line[3]) >= 10.00 and float(line[4]) >= 10.00:
        line.append("admis")
        admis += 1
    elif float(line[6]) + float(line[7]) >= 45:
        line.append("admis avec dette")
        dette += 1
    else:
        line.append("ajourné")
        ajourn += 1
        #s=1
        #for line in tab:
        #if s==1:
        #s++
        #elif comme elleest

bool = True
for line in tab:
    if bool:
        bool=False
    elif float(line[5])>max:
        max=float(line[5])
bool = True
for line in tab:
    if bool:
        bool = False
    elif float(line[5])<min:
        min=float(line[5])
for line in tab:
    print(line)
#prsen=(admis*100)/(len(tab)-1)
print("\nle nombre des étudiants admis",admis,"=====>",round(admis*100/(len(tab)-1),2),"%")

print("\nle nombre des étudiants admis avec dette",dette,"=====>",round(dette*100/(len(tab)-1),2),"%")
print("\nle nombre des étudiants ajourné",ajourn,"=====>",round(ajourn*100/(len(tab)-1),2),"%")
print("\nla meilleur moyenne est",max)
print("\nla mauvaise moyenne est",min)

#####********************* html **********************************************************#####

fichhtml = open("html.html","w")
fichhtml.write("<html>\n \t <head>\n \t <title>  First TP </title>\n </head> <body>")
fichhtml.write("<H2><Center><I>P.V.de Deleberation final </I></Center></H2><BR> <B> <center> <table border= 1px solid black;>\n ")
for line in tab:
    fichhtml.write('<tr>')
    for i in range(len(line)):
        fichhtml.write("<th>\n")
        fichhtml.write("%s" %line[i])
        fichhtml.write("</th>\n")
    fichhtml.write('</tr>')
fichhtml.write('</table>\n</center>\n')
fichhtml.write("<h1><center><I> Les statistiques </I> </h1></center> ")
fichhtml.write('<P> le nombre des étudiants admis :   ' +str (admis)+" ( "+str (round(admis*100/(len(tab)-1),2))+"% )" +'</P>')
fichhtml.write('<P> le nombre des étudiants admis avec dette :   ' +str (dette)+" ( "+str (round(dette*100/(len(tab)-1),2))+"% )" +'</P>')
fichhtml.write('<P> le nombre des étudiants ajourné :   ' +str (ajourn)+" ( "+str (round(ajourn*100/(len(tab)-1),2))+"% )" +'</P>')
fichhtml.write('<P> la meilleur moyenne est :   '+str(max)+'</P>')
fichhtml.write('<P> la mauvaise moyenne est :   '+str(min)+'</P>')
fichhtml.write("</body></html>")
