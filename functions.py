from django.shortcuts import render


def my_view(request):
    breadcrumbs = [
        {'url': '/', 'name': 'Home'},
        {'url': '/products/', 'name': 'Products', 'children': [
            {'url': '/products/category1/', 'name': 'Category 1'},
            {'url': '/products/category2/', 'name': 'Category 2', 'children': [
                {'url': '/products/category2/subcategory1/', 'name': 'Subcategory 1'},
                {'url': '/products/category2/subcategory2/', 'name': 'Subcategory 2'}
            ]}
        ]},
        {'url': request.path_info, 'name': 'Current Page'}
    ]
    context = {'breadcrumbs': breadcrumbs}
    return render(request, 'my_template.html', context)
