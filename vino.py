from flask import Flask ,render_template,request
#import mysql.connector as db
app = Flask(__name__)
@app.route('/')
def student():
   return render_template('student.html')
 vino
if __name__=="__main__":
   app.run()
