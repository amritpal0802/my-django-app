from reportlab.pdfgen import canvas
from django.http import HttpResponse
def getpdf(request): 
    response=HttpResponse(content_type='applpication/pdf')
    response['content-disposition']='attachment; filename="file.pdg"'
    p=canvas.Canvas(response)
    p.setFont("times-Roman",55)
    p.drawString(100,70,"hello,javatpoint")
    p.showPage()
    p.save()
    return response
