from django.shortcuts import render

def churn_rate(request):
    l = float(request.POST.get('lost', '0'))
    i = float(request.POST.get('initial', '0'))

    churnrate = (l/i)*100 if request.method == 'POST' else 0

    print("Customerslost =", l)
    print("InitialCustomers =", i)
    print("ChurnRate =", churnrate)

    return render(
        request,
        'myapp/experiment3part3.html',
        {'l': l, 'i': i, 'churnrate': churnrate}
    )
