from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id':1, 
    'title':'Data Analyst', 
    'location':'Bengaluru , India', 
    'salary':'Rs.10,00,000',
  },
  {
    'id':2, 
    'title':'Data Scientist', 
    'location':'Pune, India', 
    'salary':'RS.17,00,000',
  },
{
  'id':3, 
  'title':'Data Engineer', 
  'location':'Pune, India', 
  'salary':'Rs.16,00,000',
},
  {
    'id':4, 
    'title':'Data Engineer', 
    'location':'San Fransisco, USA', 
    'salary':'$150k',
  },

]

@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs= JOBS,  
                         company_name='Jovian')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
