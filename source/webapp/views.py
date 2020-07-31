from django.shortcuts import render


# def index_view(request):
#     print(request.GET.get('answer/'))
#     return render(request, )

def answer_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        context = {
            'first_num': request.POST.get('first_num'),
            'second_num': request.POST.get('second_num'),
            'calc': request.POST.get('calc'),
            'answer': 0
            }
        if context['calc'] == 'add':
            context['calc'] ='+'
            context['answer'] =int(context['first_num']) + int(context['second_num'])
        elif context['calc'] == 'subtract':
            context['calc'] = '-'
            context['answer'] = int(context['first_num']) - int(context['second_num'])
        elif context['calc'] == 'multiply':
            context['calc'] = '*'
            context['answer'] = int(context['first_num']) * int(context['second_num'])
        elif context['calc'] == 'divide':
            context['calc'] = '/'
            context['answer'] = int(context['first_num']) / int(context['second_num'])

        print(context)
        return render(request, 'answer.html', context)



# Create your views here.
