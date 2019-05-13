var createError = require('http-errors');

var express = require('express');

const sqlite3 = require('sqlite3')
var path = require('path');

var cookieParser = require('cookie-parser');

var logger = require('morgan');


var indexRouter = require('./routes/index');

var usersRouter = require('./routes/users');


bodyParser = require('body-parser');
var app = express();
app.use(express.static('public'))
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
var urlencodedParser = bodyParser.urlencoded({ extended: true})
app.use(bodyParser.urlencoded({ extended: true }))
var jsonParser = bodyParser.json()

var students = []

let db = new sqlite3.Database('../Face-DataBase.db', (err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Connected to the in-memory SQlite database.');});

db.serialize(() => {
  db.each("SELECT * from Student", (err, row) => {
    if (err) {
      console.error(err.message);
    }
    students.push(row.Id);
  });
});

app.get('/', function (req, res) {
  res.render('index',
	      {students : students}
	     );
});

app.post('/getAttendance', urlencodedParser, function (req, res) {
  console.log(req.body);
  var date = req.body.date;
  var date_vals = date.split("-");
  date = date_vals[2] + "-" +date_vals[1] + "-" + date_vals[0];
  var present_students = [];
  var absent_students = [];
  var seen_rols = [], i = 0;
  var attendance = {};
  var subject = req.body.subject;

  db.serialize(() => {
    db.each("SELECT * from Attendance5 where date = '" + date + "' and subject = '" + subject + "'" , (err, row) => {
      if (err) {
        console.error(err.message);
        res.send("Error in processing. Please try again.");
      } else {
        present_students[i] = row;
        seen_rols[i] = row.Roll;
        console.log(row);
        i++;
      }
      console.log(present_students.length)
    });

    db.serialize(() => {
      i = 0;
      db.each("SELECT * from Student", (err, row) => {
      if (err) {
         console.error(err.message);
      }
      if(!(seen_rols.includes(row.Id))) {
      	  absent_students[i++] = row;
        }
      });
     });
    
  db.serialize(() => {
   db.get("SELECT * from Student", (err, row) => {
    console.log(absent_students);
    attendance["subject"] = subject;
    attendance["date"] = date;
    res.render("aReport",
		{ attendance : attendance,
		  present_students : present_students,
                  absent_students : absent_students
		});
    });
    });
  });
});

app.post('/getReports', urlencodedParser, function (req, res) {
  console.log(req.body);
  var roll_no = req.body.id;
  var subject = req.body.subject;
  var present_days = [];
  i = 0;
  var name = "";
  var student = {};

  db.serialize(() => {
    db.each("SELECT DISTINCT Date from Attendance5", (err, row) =>{
      if (err) {
        console.error(err.message);
      }
      present_days[row.Date] = "Absent";
    });
  });

  db.serialize(() => {
    i = 0;
    db.each("SELECT * from Attendance5 where Roll = '" + roll_no + "' AND Subject = '" + subject + "'", (err, row) => {
       if(err){
         console.log(err.message);
       }
       present_days[row.Date] = "Present";
    });
  });
  
   db.serialize(() => {
    i = 0;
    db.get("SELECT Name from Student where Id = '" + roll_no + "'", (err, row) => {
       if(err){
         console.log(err.message);
       }
       name = row.Name;
    });
  });

  db.serialize(() => {
   db.get("SELECT * from Student", (err, row) => {
    student["name"] = name;
    student["roll"] = roll_no;
    student["subject"] = subject;
    res.render("wReport",
		{ student: student,
		  present_days : present_days
		});
    });
  });      
});

module.exports = app;
