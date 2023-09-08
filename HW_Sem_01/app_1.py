# Задание № 9
# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/about/')
def about():
    context = {'title': 'О нас'}
    return render_template('about.html', **context)


@app.route('/catalog/')
def catalog():
    context = {'title': 'Каталог'}
    catalog_list = [
        {
            'name': 'Одежда',
            'image': 'clothes.png',
            'page': 'cloth',
            'description': 'Широкий ассортимент одежды как на каждый день, так и в праздничные дни. Юбки, куртки, '
                           'платья, джинсы и многое другое...'
        },
        {
            'name': 'Обувь',
            'image': 'shoes.jpg',
            'page': 'shoes',
            'description': 'Широкий ассортимент обуви как на каждый день, так и в праздничные дни. Сапоги, ботинки, '
                           'туфли, кроссовки и многое другое...'
        }
    ]
    return render_template('catalog.html', **context, catalogs=catalog_list)


@app.route('/cloth/')
def cloth():
    context = {'title': 'Одежда'}
    cloth_list = [
        {
            'name': 'Куртки',
            'image': 'jackets.jpg',
            'page': 'jackets',
            'description': 'Широкий ассортимент курток'
        },
        {
            'name': 'Платья',
            'image': 'dresses.jpg',
            'page': 'dresses',
            'description': 'Широкий ассортимент платьев'
        },
        {
            'name': 'Джинсы',
            'image': 'jeans.jpg',
            'page': 'jeans',
            'description': 'Широкий ассортимент джинсов'
        },
        {
            'name': 'Юбки',
            'image': 'skirts.jpg',
            'page': 'skirts',
            'description': 'Широкий ассортимент юбок'
        }
    ]
    return render_template('cloth.html', **context, cloths=cloth_list)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    shoes_list = [
        {
            'name': 'Сапоги',
            'image': 'boots.jpg',
            'page': 'boots',
            'description': 'Широкий ассортимент сапог'
        },
        {
            'name': 'Ботинки',
            'image': 'little_boots.jpeg',
            'page': 'little_boots',
            'description': 'Широкий ассортимент ботинок'
        },
        {
            'name': 'Туфли',
            'image': 'shoes_0.jpg',
            'page': 'shoe',
            'description': 'Широкий ассортимент туфель'
        },
        {
            'name': 'Кроссовки',
            'image': 'sneakers.jpg',
            'page': 'sneakers',
            'description': 'Широкий ассортимент кроссовок'
        }

    ]
    return render_template('shoes.html', **context, shoes=shoes_list)


if __name__ == '__main__':
    app.run(debug=True)
