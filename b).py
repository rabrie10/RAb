# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 09:06:28 2021

@author: Eier
"""
class Flerevalgspørsmål:
     def __init__(self, que, ans, alt):
          self.question = que
          self.answer = ans
          self.alternative = alt
    
     def __str__(self):
        text = self.question + "\n"
        for alternativnummer, alternativsvar, in enumerate(self.alternative):
            text += f"  {alternativnummer+1}: {alternativsvar} \n"
        return text
        
     def sjekk_svar (self, sjekk: int):
        return sjekk == self.answer

quiz = []

quiz.append(Flerevalgspørsmål("Hva er hovestad i Japan?", 2, ["Oslo", "Tokyo","Tronto", "Beijing"] ))
quiz.append(Flerevalgspørsmål("\nHvor ligger Japan", 3, ["Europa", "Nord-amerika", "Asia", "Afrika"]))
for spm in quiz:
    print(spm)
    
    valg = int(input("skriv svar:"))
    
    if spm.sjekk_svar(valg):
        print ("Riktig svar")
        
    else:
        print("feil svar")

