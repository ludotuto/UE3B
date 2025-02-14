# Copyright 2024-2025 Ludovic Rousseau, TSSU 
# Distribuée sous licence CC BY-NC-ND 4.0 
# Attribution-NonCommercial-NoDerivatives 4.0 International  
# https://creativecommons.org/licenses/by-nc-nd/4.0/

from math import *
h=0
x=0
y=0
ahtf=0
atf=0

print("DE2 en mEq/L/upH")
print("DE2(PCO2i,pHi,PCO2f,pHf)")
print("DE2(,,,)")
print("S=[Atf-]+[AHtf]=cte!!! en mmol/L")
print("S(DE,phi,phf)")
print("S(,,)")


print("d[af] (différent de 0):")
print("d_af(pHi,PCO2i,pHf,PCO2f,Ctotal,pKa)")
print("d_af(,,,,,)")


print("(-PT=) DE en mEq/L/upH")
print("DE1(Dhco3,phi,phf)")
print("DE1(,,)")
print("[Atf-] et [AHtf] en mmol/l avec Ctot tf: ")
print("Ctf(Ctotal,pH,pKa)")
print("Ctf(,,)")

print("HCO3- en mmol/l: ")
print("f(PCO2,pH)")
print("f(,)")
print("PCO2 en mm Hg ")
print("g(HCO3-,pH)")
print("g(,)")
print("DNE !!! en mEq/L/upH")
print("DNE(PCO2f,pHf)")
print("DNE(,)")


def f(p,ph):
  h=0.03*p*10**(ph-6.1)
  return h

def DNE(pf,phf):
  x=(-24+f(pf,phf))/(-7.4+phf)
  return x

def DE2(pi,phi,pf,phf):
  x=(-f(pi,phi)+f(pf,phf))/(-phi+phf)
  return x

def Ctf(ct,pH,pka):
  atf=ct*(1-(1/(1+(10**(pH-pka)))))
  ahtf=ct-atf
  print("[Atf-]=",atf)
  print("[AHtf]=",ahtf)
  return atf

def d_af(phi,pi,phf,pf,ct,pka):
  print('etat initial :')
  KK=Ctf(ct,phi,pka)
  print('etat final :')
  LL=Ctf(ct,phf,pka)
  y=-(((f(pf,phf))-(f(pi,phi)))-KK+LL)
  print("en mmol/L  d[af] =")
  return y

def DE1(Dhco3,phi,phf):
  x=(Dhco3)/(-phi+phf)
  return x


def S(DE, pH_i, pH_f):
  z = (-DE * (pH_f - pH_i)) / ((1 + 10**(6.8 - pH_f)) - (1 + 10**(6.8 - pH_i)))
  return z


def g(h,ph):
  pco2=(h*10**(-ph+6.1))/0.03
  return pco2
