import os,subprocess,tkinter,time,mysql.connector
from tkinter import messagebox
#Obtenemos la información fecha
log=time.strftime("%H%M-%Y-%m-%d")
msg="'Backup Listo '+log"
#print(log)
#Var conexión
HOST='67.227.144.116'
#HOST='teechiapas.gob.mx'
PORT='3306'
USER='tribuna7_declaracionp'
PASS='@T33ch2022*_*'
BD='tribuna7_bd_declarachiapas'

#mydb = mysql.connector.connect(host=HOST,user=USER,passwd=PASS,db=BD)
#cur=mydb.cursor()
#if mydb:
  #print("Conexión Establecida")
#subprocess.run("mysqldump -u 'tribuna7_declaracionp' -p '@T33ch2022*_*' -h 67.227.144.116 'tribuna7_bd_declarachiapas' > ${log}.sql")
#os.popen("mysqldump -h %s -P %s -u %s -p%s %s > %s.sql" % (HOST,PORT,USER,PASS,BD,BD+"_"+log))
subprocess.call("mysqldump -h %s -P %s -u %s -p%s %s> %s.sql" % (HOST,PORT,USER,PASS,BD,log+"_"+BD),shell=True)
messagebox.showinfo(message=msg, title="Respaldo BD terminado")
  #subprocess.call("mysqldump -u%s-p%s-h%s %s>%s" %(USER,PASS,HOST,BD,BD),shell=True)
  #if os.path.isfile('${log}${bd}.sql'):
  #subprocess.call("rm ${log}${bd}.sql",shell=True)

#else:
#  print("Conexión Fallida")
#mydb.close()