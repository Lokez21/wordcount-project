from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    # return HttpResponse('<h1>Home page</h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordslist = fulltext.split()
    count = len(wordslist)

    words_count_dict = {}
    max_count = 0
    min_count = 1
    max_items = []
    min_items = []
    for each in wordslist:
        if each in words_count_dict:
            words_count_dict[each] += 1

        else:
            words_count_dict[each] = 1

    for k,v in words_count_dict.items():
        if v==1:
            min_items.append(k)
        if v >= max_count:
            max_count = v

    for k,v in words_count_dict.items():
        if v==max_count:
            max_items.append(k)


    words_count_list = words_count_dict.items()
    sorted_words_list = sorted(words_count_list, key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', { 'fulltext':fulltext, 'count':count, 'words_count':sorted_words_list, 'min_items': min_items } )
