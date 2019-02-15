import csv
def getfile(request):
    response=HttpResponse(content_type='text/csv')
    response['content-disposition']='attachment;filename="file.csv"'
    writer=csv.writeer(response)
    writer.writerow(['12','amrit','pal','CA'])
    writer.writerow(['23','taran','jeet','US'])
    return response
