from django.http import HttpResponse
from django.core.exceptions import EmptyResultSet
from django.db import Error
from wsgiref.util import FileWrapper

from .models import QueryFromUser
from .utils import create_video


def send_video(request):
    # getting the request parameter "text"
    text = request.GET.get('text', None)
    if text is None:
        raise EmptyResultSet('Отсутствует параметр запроса "text"') 

    # create and save video
    filename = create_video(text=text)

    # add query to database
    query = QueryFromUser(query_text=text)
    try:
        query.save()
    except Error:
        raise Error('Не удалось сохранить запрос в базу данных')

    # open the video and send it
    try:
        file = FileWrapper(open(filename, 'rb'))
    except FileNotFoundError:
        raise FileNotFoundError('Файл не найден')
    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = f'attachment; filename={filename}'

    return response
