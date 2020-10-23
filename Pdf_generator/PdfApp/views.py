from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import HttpResponse
from .models import Blog
# Create your views here.
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils.timezone import datetime
from django.views.generic import ListView
from .Forms import PdfForm

def index(request):
    blog=Blog.objects.all()
    return render(request,'index.html',{'blogs':blog})
# class Customer(ListView):
#     model = Blog
#     template_name = 'home.html'

def render_pdf(request,pk):

    blog =get_object_or_404(Blog,pk=pk)
    template_path = 'pdf.html'
    date=datetime.now()
    context = {
        'blog': blog
    }
    response = HttpResponse(content_type='application/pdf')
    filename = f'{blog.name}-{date}.pdf'
    response['content-Disposition'] = 'attachment; filename=%s' % filename
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('page not found')
    return response

def pdf_generator(request,pk):
    # pk=kwargs.get('pk')
    blog =get_object_or_404(Blog,pk=pk)
    template_path = 'pdf.html'
    date = datetime.now()
    context = {
        'blog': blog,

    }
    response = HttpResponse(content_type='application/pdf')
    filename = f'{blog.name}-{date}.pdf'
    response['content-Disposition'] = 'filename=%s' % filename
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('page not found')
    return response


def create(request):
    form = PdfForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'create.html')
    else:
        form = PdfForm()
        return render(request, 'create.html', {'forms': form})




# def pdf_file(request):
#     template_path='pdf.html'
#     context={
#         'myvar':'hello this is pdf format'
#     }
#     response=HttpResponse(content_type='application/pdf')
#     # if download:
#     # response['content-Disposition'] = 'attachment; filename="report.pdf"'
#     #if display:
#     response['content-Disposition'] = ' filename="report.pdf"'
#     template=get_template(template_path)
#     html=template.render(context)
#
#     pisa_status=pisa.CreatePDF(
#         html,dest=response)
#     if pisa_status.err:
#         return HttpResponse('we had some error <pre>'+html + '</pre>')
#     return response