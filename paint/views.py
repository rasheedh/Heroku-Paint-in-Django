from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import sqlite3
import pickle

def draw(request,filename):
        wholedata=[]
    	fname=[]
    	db=sqlite3.connect('image.db')
    	cur=db.cursor().execute('select * from entries')
     	for row in cur.fetchall():
       		fname.append(row[0])
      		if filename==row[0]:
      			wholedata=pickle.loads(str(row[1]))
        t = get_template('paint.html')
    	html = t.render(Context({'lis':fname,'imagedata':wholedata})) 
        return HttpResponse(html)

def h(request):
     if request.method=='POST':
	fname=request.POST.get('f')
        imagedata=request.POST.get('parameter')
        
	imagedata=pickle.dumps(imagedata)
        
	db=sqlite3.connect('image.db')	
        
	db.cursor().execute('insert into entries (filename,imagedata) values (?,?)',[fname,imagedata])
	db.commit()
	db.close()
        
        t = get_template('paint.html')
    	html = t.render(Context({'list':fname})) 
        return HttpResponse(html)
        
	
def hello(request):
        
	filename=[]
	wholedata=[]
	db=sqlite3.connect('image.db')
	cur=db.cursor().execute('select * from entries')
	for row in cur.fetchall():
		filename.append(row[0])
        t = get_template('paint.html')
    	html = t.render(Context({'lis':filename,'imagedata':wholedata})) 
        return HttpResponse(html)

