#Script para hacer respaldos de base de datos MySql
import os,subprocess,tkinter,time,mysql.connector
from tkinter import messagebox
#Obtenemos la fecha y hora
log=time.strftime("%H%M-%Y-%m-%d")
msg="'Backup Listo "
HOST='dominio o IP'
PORT='3306'
USER='usuario_bd'
PASS='pass_bd'
BD='nombre_de_la_bd'
subprocess.call("mysqldump -h %s -P %s -u %s -p%s %s> %s.sql" % (HOST,PORT,USER,PASS,BD,log+"_"+BD),shell=True)
messagebox.showinfo(message=msg+BD+' '+log, title="Proceso terminado")
