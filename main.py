from fastapi import FastAPI, Request, Form
import uvicorn, sklearn, joblib
from fastapi.templating import Jinja2Templates

app=FastAPI()
templates=Jinja2Templates(directory="templates/")

#async def hello():
#@app.get('/')
#    return('Air temperature prediction')

model=joblib.load('model.pkl')

@app.get('/')
async def form_post(request:Request):
    result='Waiting for you to enter details'
    return templates.TemplateResponse('form.html', context={'request':request, 'result':result})

@app.post('/')
async def form_post(request:Request, num_1:float=Form(...),num_2:float=Form(...),num_3:float=Form(...),num_4:float=Form(...),num_5:float=Form(...),num_6:float=Form(...),num_7:float=Form(...),num_8:float=Form(...)):
#    result=num_1+num_2+num_3+num_4+num_5+num_6+num_7+num_8
#predict([[308.9,1508,92,0,0,0,0,0]])[0]
#ouput= 298.68
    result=round(model.predict([[num_1, num_2,num_3,num_4,num_5,num_6,num_7,num_8]])[0],2)

    return  templates.TemplateResponse('form.html', context={'request':request,'result':result})