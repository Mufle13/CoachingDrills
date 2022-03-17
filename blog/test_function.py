def filter_pagination(page=2, dico_parameters={'page': 1, 'categories': [1,2], 'tags': [1,2,6]}):

    dico_parameters.pop('page', None)
    dico_parameters['page']= page
    return print(dico_parameters)


filter_pagination()

    
