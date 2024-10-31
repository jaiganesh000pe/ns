from flask import Flask, render_template ,request, redirect,flash,url_for,session
from datetime import datetime
now = datetime.now()
print(now)  # Output: 2024-10-24 14:30:00.123456 (format varies depending on system settings)
from datetime import datetime
dt = datetime.now()
formatted_date = dt.strftime("%d/%m/%Y")  # Output: 2024-10-24 14:30:00 %H:%M
formatted_time = dt.strftime("%H:%M")

import sqlite3 as sql
app = Flask(__name__)







@app.route("/", methods=['GET', 'POST'])
def home():

    return render_template('index.html')


@app.route("/home", methods=['GET', 'POST'])
def homepay():
    
    name12 = ''
    name1 = ''
    pass12 = ''
    if request.method == 'POST':
        ns12 = request.form['ns1']
        name12 = request.form['nsemail']
        pass12 = request.form['nspass']
        

        if name12 == 'nscdm96@gmail.com' and pass12 == "Nscdm@96":
            return redirect('/loingcorrect/'+ns12)
        else:
            return redirect('/Incorrect/'+ns12)

    return render_template('index.html', nsname=name12 ,name1 =name1)


@app.route("/s", methods=['GET', 'POST'])
def s():
    
        
    name12pay = ''
    name1pay = ''
    pass12pay = ''
    
    if request.method == 'POST':
       
        name12pay = request.form['nsemailpay']
        pass12pay = request.form['nspasspay']
        
        if name12pay == 'nscdm96@gmail.com' and pass12pay == "Nscdm@96":  
            return redirect('/all')
        else:
            return redirect('/Incorrect1')
        
        
    return render_template('index.html', nsnamepay=name12pay ,name1pay =name1pay )


@app.route("/loingcorrect/<ns12>" , methods=['GET', 'POST'])
def loing1(ns12):
    current_date = formatted_date
    current_time = formatted_time
    
    return render_template('page1.html',ns12 = ns12 ,date=current_date, time=current_time )





#sume page ster

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']

         city = formatted_date
         pin = formatted_time

         ef = request.form['esaf']
         ef1 = request.form['esaf1']
         gs1 = request.form['gs']
         jp1 = request.form['jp']
         vs1 = request.form['vs']
         ss1 = request.form['ss']
         sa1 = request.form['sa']
         su1 = request.form['su']
         no1 = request.form['no']


         hp1 = request.form['hp']
         eb1 = request.form['eb']
         mk1 = request.form['mk']
         pt1 = request.form['pt']
         mo1 = request.form['mo']
         fe1 = request.form['fe']
         tr1 = request.form['tr']
         gy1 = request.form['gy']
         fo1 = request.form['fo']
         fr1 = request.form['fr']

         el1 = request.form['el']


#lone totel
         eft = int(ef)
         ef1t = int(ef1)
         gs1t = int(gs1)
         jp1t = int(jp1)
         vs1t = int(vs1)
         ss1t = int(ss1)
         sa1t = int(sa1)
         su1t = int(su1)
         no1t = int(no1)
         el1t = int(el1)


         lone = eft+ef1t+gs1t+jp1t+vs1t+ss1t+sa1t+su1t+no1t+el1t
#lone totel end
         hp1 = int(hp1)
         eb1 = int(eb1)
         mk1 = int(mk1)
         pt1 = int(pt1)
         mo1 = int(mo1)
         fe1 = int(fe1)
         tr1 = int(tr1)
         gy1 = int(gy1)
         fo1 = int(fo1)
         fr1 = int(fr1)
         
         home_totel =  hp1 +eb1 +mk1 +pt1 +mo1 +fe1 +tr1 +gy1 +fo1 +fr1 


         totel = home_totel+lone

#salary
         addr1 = int(addr)
         balas =addr1 - totel  
         m = "This Month's Your Salary Is Low,So You Need This Amount : "


         if balas < 0:
             the_need =m + str(balas)
             the_balas =  "Sorry This Month No Savings And No Balance"
         else:
             the_need =" This Is Your Savings and Balance : " + str(balas)
             the_balas ="Happy -_- , This Month You Have Savings And Balance "

         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin,esaf,esaf1,home,ebbill,milk,petrol,gramiya,jaya,valar,sur,sama,suth,non,mob,fes,tra,gym,food,frd1,elone,to_lone,to_home,all_totel,to_) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(nm,addr,city,pin,ef,ef1,hp1,eb1,mk1,pt1,gs1,jp1,vs1,ss1,sa1,su1,no1,mo1,fe1,tr1,gy1,fo1,fr1,el1,lone,home_totel,totel,balas) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         
         return render_template("add.html",msg = msg ,lone =lone, home_to = home_totel ,totel = totel ,salary=the_balas , the_need = the_need,nm=nm)
         con.close()               

#sume page end


@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   data = cur.fetchall(); 
   con.close()
   return render_template("add.html",data = data)


@app.route("/Incorrect/<ns12>" , methods=['GET', 'POST'])
def eroor(ns12):
    return render_template('erorr.html',ns12 = ns12)

@app.route("/Incorrect1" , methods=['GET', 'POST'])
def eroor1():
    return render_template('erorr1.html')



@app.route('/all')
def all():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   data = cur.fetchall(); 
   con.close()
   
   return render_template("allbillig.html",data = data)


@app.route("/updata_record/<string:id>", methods=[ 'POST','GET'])
def updata_record(id):
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from students where pid=?",[id])
    
    data = cur.fetchone(); 
    con.close()

    return render_template('updata_record.html' ,data=data,id=id)

@app.route("/delete_record/<string:id>", methods=[ 'POST','GET'])
def delete_record(id):
    try:
            con =  sql.connect("database.db") 
           
            cur = con.cursor()
            cur.execute("DELETE FROM students where pid=?",[id])
            con.commit()
            msg = "Record successfully added"
    except:
        con.rollback()
        msg = "error in insert operation"
      
    finally:
        return render_template('index.html',msg=msg )
        con.close

   


if __name__ == '__mani__': 
    app.run(debug=True, host='0.0.0.0') 