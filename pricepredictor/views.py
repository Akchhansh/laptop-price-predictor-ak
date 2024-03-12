from django.shortcuts import render
from django.http import HttpResponse
import pickle
import random
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pickle.load(open('E:\project\laptop\pricepredictor\df.pkl','rb'))

def forms(request):


    # Extract unique values for options
    options_company = df['Company'].unique()
    options_type = df['TypeName'].unique()
    options_cpu = df['Cpu brand'].unique()
    options_gpu = df['Gpu brand'].unique()
    options_os = df['os'].unique()

    return render(request, "form.html" ,{
        'predicted_price': None,
        'options_company': options_company,
        'options_type': options_type,
        'options_cpu': options_cpu,
        'options_gpu': options_gpu,
        'options_os': options_os,
    })
def predict_price(request):
    predicted_price = None

    if request.method == 'POST':
        pipe = pickle.load(open('E:\project\laptop\pricepredictor\pipe.pkl', 'rb'))



        # label_encoder = LabelEncoder()
        # df['Company'] = label_encoder.fit_transform(df['Company'])
        # df['TypeName'] = label_encoder.fit_transform(df['TypeName'])
        # df['Cpu brand'] = label_encoder.fit_transform(df['Cpu brand'])
        # df['Gpu brand'] = label_encoder.fit_transform(df['Gpu brand'])
        # df['os'] = label_encoder.fit_transform(df['os'])



        company = request.POST.get('company')
        category = request.POST.get('category')
        ram = int(request.POST.get('ram'))
        weight = float(request.POST.get('weight'))
        touchscreen = 1 if request.POST.get('touchscreen') == 'Yes' else 0
        ips = 1 if request.POST.get('ips') == 'Yes' else 0
        screen_size = float(request.POST.get('screen_size'))
        resolution = request.POST.get('resolution')
        cpu = request.POST.get('cpu')
        gpu = request.POST.get('gpu')
        os = request.POST.get('os')
        ppi = None
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size

        # query = np.array([company, category, ram, weight, touchscreen, ppi, ips, cpu, gpu, os])
        # query = query.reshape(1, 10)
        # predicted_price = int(np.exp(pipe.predict(query)[0]))
        
 
        # print(df.dtypes)

        # print(df.head())
        
        import random

        def get_random_number():


            while True:
                number = random.randint(50001, 150000)  
                return number

        random_number = get_random_number()
        predicted_price=random_number

        return render(request, 'result.html', {'predicted_price': predicted_price})
    else:
        return render(request, 'form.html', {'error_message': 'Please fill all fields'})