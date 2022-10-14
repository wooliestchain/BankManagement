import  mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database="bank")

def OpenAcc():
    n=input("Entrer le nom: ")
    ac=input("Entrer le numéro de compte: ")
    db=input("Entrer la date de naissance: ")
    add=input("Entrer l'adresse: ")
    cn=input("Entrer le numero de telephone: ")
    ob=int(input("Entrer le montant de départ: "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1=('insert into compte values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into montant values (%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Les données ont bien été enregistrées.")
    main()

def DepoAmo():
    amount=int(input("Entrer le montant à déposer: "))
    ac = input("Entrer le numéro de compte: ")
    a='select Solde from montant where Num_Compt=%s  '
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+amount
    sql=('update montant set Solde=%s where Num_Compt=%s ')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def WithdrawAmount():
    amount = int(input("Entrer le montant à virer: "))
    ac = input("Entrer le numéro de compte: ")
    a = 'select Solde from montant where Num_Compt=%s  '
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = ('update montant set Solde=%s where Num_Compt=%s ')
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()

def BalEnq():
    ac=input("Entrer le numéro de compte: ")
    a='select * from montant where Num_Compt=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Solde du compte:",ac,"est",int(result[-1]))
    main()

def DisDetails():
    ac = input("Entrer le numéro de compte: ")
    a = 'select * from compte where Num_Compt=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i,end=" ")


def CloseAcc():
    ac = input("Entrer le numéro de compte: ")
    sql1='delete from compte where Num_Compt=%s'
    sql2='delete from montant where Num_Compt=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    main()










def main():
    print('''
    1.Ouvrir un compte
    2.Deposer de l'argent
    3.Retirer de l'argent
    4.Consulter le solde
    5.Afficher les informations du compte
    6.Fermer un compte
    7.Quitter''')
    choice = input("Entrer une tache à executer: ")
    if (choice=='1'):
        OpenAcc()
    elif (choice=='2'):
        DepoAmo()
    elif (choice=='3'):
        WithdrawAmount()
    elif (choice=='4'):
        BalEnq()
    elif (choice=='5'):
        DisDetails()
    elif (choice=='6'):
        CloseAcc()
    while (choice == '7'):
        print("Au revoir.")
        break
    else:
        print("Choix Incorect")
        main()


main()