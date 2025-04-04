from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
  {
    'id':1, 
    'title':'Data Analyst', 
    'location':'Bengaluru , India', 
    'salary':'Rs.10,00,000'
  },
  {
    'id':2, 
    'title':'Data Scientist', 
    'location':'Pune, India', 
    'salary':'RS.17,00,000'
  },
{
  'id':3, 
  'title':'Data Engineer', 
  'location':'Hyderabad, India', 
  
},
  {
    'id':4, 
    'title':'Data Engineer', 
    'location':'San Fransisco, USA', 
    'salary':'$150k'
  },

]

@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs= JOBS,  
                         company_name='Jovian')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
