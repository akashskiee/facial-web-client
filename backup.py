  if(conf < 100):
              if(id==1):
                id=1
                if((str(id)) not in dict):
                    dict[str(id)]=str(id)
             
                ts = time.time()
                conn = sqlite3.connect('Face-DataBase.db')
                c = conn.cursor()  
                timeStamp = cmb2.get()    
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                roll = id
                sub = cmb.get()
                query2 = ("SELECT Name FROM Student WHERE Id='1'")
                data2 = c.execute(query2)
                row = c.fetchone()[0]
                query = ("INSERT INTO Attendance5(Roll,Name, Date, Time, Subject) VALUES (?,?,?,?,?)")
                data = c.execute(query, (roll,row,date,timeStamp,sub))
                conn.commit()
                c.close()
                conn.close()   
                if((str(id)) not in dict):
                    dict[str(id)]=str(id)
                break
           
              elif(id==2):
                

                  id=2
                  if((str(id)) not in dict):
                     dict[str(id)]=str(id)
             
                  ts = time.time()
                  conn = sqlite3.connect('Face-DataBase.db')
                  c = conn.cursor()  
                  timeStamp = cmb2.get()    
                  date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                  roll = id
                  sub = cmb.get()
                  query2 = ("SELECT Name FROM Student WHERE Id='2'")
                  data2 = c.execute(query2)
                  row = c.fetchone()[0]
                  
                  query = ("INSERT INTO Attendance5(Roll,Name, Date, Time, Subject) VALUES (?,?,?,?,?)")
                  data = c.execute(query, (roll,row,date,timeStamp,sub))
                  conn.commit()
                  c.close()
                  conn.close()
              elif(id==3):
                  
                  id=3
                  if((str(id)) not in dict):
                     dict[str(id)]=str(id)
             
                  ts = time.time()
                  conn = sqlite3.connect('Face-DataBase.db')
                  c = conn.cursor()  
                  timeStamp = cmb2.get()    
                  date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                  roll = id
                  sub = cmb.get()
                  query2 = ("SELECT Name FROM Student WHERE Id='3'")
                  data2 = c.execute(query2)
                  row = c.fetchone()[0]
                  query = ("INSERT INTO Attendance5(Roll,Name, Date, Time, Subject) VALUES (?,?,?,?,?)")
                  data = c.execute(query, (roll,row,date,timeStamp,sub))
                  conn.commit()
                  c.close()
                  conn.close()
              elif(id==4):
                  
                
                  id=4
                  if((str(id)) not in dict):
                     dict[str(id)]=str(id)
             
                  ts = time.time()
                  conn = sqlite3.connect('Face-DataBase.db')
                  c = conn.cursor()  
                  timeStamp = cmb2.get()    
                  date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                  roll = id
                  sub = cmb.get()
                  query2 = ("SELECT Name FROM Student WHERE Id='4'")
                  data2 = c.execute(query2)
                  row = c.fetchone()[0]
                  query = ("INSERT INTO Attendance5(Roll,Name, Date, Time, Subject) VALUES (?,?,?,?,?)")
                  data = c.execute(query, (roll,row,date,timeStamp,sub))
                  conn.commit()
                  c.close()
                  conn.close()
              elif(id==5):
                  
                
                  id=5
                  if((str(id)) not in dict):
                     dict[str(id)]=str(id)
             
                  ts = time.time()
                  conn = sqlite3.connect('Face-DataBase.db')
                  c = conn.cursor()  
                  timeStamp = cmb2.get()    
                  date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                  roll = id
                  sub = cmb.get()
                  query_select = ("SELECT * FROM Attendance5 WHERE Roll='5' AND Date = '?' AND Time = '?' AND Subject = '?'")
                  data_select = c.execute(query_select, (roll, date, timestamp, sub))
                  if data_select is 'None' :
                      query2 = ("SELECT Name FROM Student WHERE Id='5'")
                      data2 = c.execute(query2)
                      row = c.fetchone()[0]
                      query = ("INSERT INTO Attendance5(Roll,Name, Date, Time, Subject) VALUES (?,?,?,?,?)")
                      data = c.execute(query, (roll,row,date,timeStamp,sub))
                      conn.commit()
                  else:
                      print("Entry exists")
                  c.close()
                  conn.close()
              elif(id==6):
                  
                
                  id=6
                  if((str(id)) not in dict):
                     dict[str(id)]=str(id)
             
                  ts = time.time()
                  conn = sqlite3.connect('Face-DataBase.db')
                  c = conn.cursor()  
                  timeStamp = cmb2.get()    
                  date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                  roll = id
                  sub = cmb.get()
                  query2 = ("SELECT Name FROM Student WHERE Id='6'")
                  data2 = c.execute(query2)
                  row = c.fetchone()[0]
                  query = ("INSERT INTO Attendance5(Roll,Name, Date, Time, Subject) VALUES (?,?,?,?,?)")
                  data = c.execute(query, (roll,row,date,timeStamp,sub))
                  conn.commit()
                  c.close()
                  conn.close()
              elif(id==7):
                                  
                  id=7
                  if((str(id)) not in dict):
                     dict[str(id)]=str(id)
             
                  ts = time.time()
                  conn = sqlite3.connect('Face-DataBase.db')
                  c = conn.cursor()  
                  timeStamp = cmb2.get()    
                  date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                  roll = id
                  sub = cmb.get()
                  query_select = ("SELECT * FROM Attendance5 WHERE Roll='7' AND Date = ? AND Time = ? AND Subject = ?")
                  data_select = c.execute(query_select, (date, timeStamp, sub))
                  has_entries = 1
                  for row in data_select:
                      has_entries = 0
                      break
                  if has_entries:
                      query2 = ("SELECT Name FROM Student WHERE Id='7'")
                      data2 = c.execute(query2)
                      row = c.fetchone()[0]
                      query = ("INSERT INTO Attendance5(Roll,Name, Date, Time, Subject) VALUES (?,?,?,?,?)")
                      data = c.execute(query, (roll,row,date,timeStamp,sub))
                      conn.commit()
                      break
                  conn.commit()
                  c.close()
                  conn.close()
              elif(id==8):
                
                  id=8
                  if((str(id)) not in dict):
                     dict[str(id)]=str(id)
             
                  ts = time.time()
                  conn = sqlite3.connect('Face-DataBase.db')
                  c = conn.cursor()  
                  timeStamp = cmb2.get()    
                  date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                  roll = id
                  sub = cmb.get()
                  query2 = ("SELECT Name FROM Student WHERE Id='8'")
                  data2 = c.execute(query2)
                  row = c.fetchone()[0]
                  query = ("INSERT INTO Attendance5(Roll,Name, Date, Time, Subject) VALUES (?,?,?,?,?)")
                  data = c.execute(query, (roll,row,date,timeStamp,sub))
                  conn.commit()
                  c.close()
                  conn.close()
              elif(id==9):
                
                  id=9
                  if((str(id)) not in dict):
                     dict[str(id)]=str(id)
             
                  ts = time.time()
                  conn = sqlite3.connect('Face-DataBase.db')
                  c = conn.cursor()  
                  timeStamp = cmb2.get()    
                  date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                  roll = id
                  sub = cmb.get()
                  query2 = ("SELECT Name FROM Student WHERE Id='9'")
                  data2 = c.execute(query2)
                  row = c.fetchone()[0]
                  query = ("INSERT INTO Attendance5(Roll,Name, Date, Time, Subject) VALUES (?,?,?,?,?)")
                  data = c.execute(query, (roll,row,date,timeStamp,sub))
                  conn.commit()
                  c.close()
                  conn.close()
              elif(id==10):
                
                  id=10
                  if((str(id)) not in dict):
                     dict[str(id)]=str(id)
             
                  ts = time.time()
                  conn = sqlite3.connect('Face-DataBase.db')
                  c = conn.cursor()  
                  timeStamp = cmb2.get()    
                  date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                  roll = id
                  sub = cmb.get()
                  query2 = ("SELECT Name FROM Student WHERE Id='10'")
                  data2 = c.execute(query2)
                  row = c.fetchone()[0]
                  query = ("INSERT INTO Attendance5(Roll,Name, Date, Time, Subject) VALUES (?,?,?,?,?)")
                  data = c.execute(query, (roll,row,date,timeStamp,sub))
                  conn.commit()
                  c.close()
                  conn.close()