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


@app.route('/jackets/')
def jackets():
    context = {'title': 'Куртки'}
    jackets_list = [
        {
            'name': 'Куртка_1',
            'image': 'jacket_1.jpg',
            'description': 'Женский пуховик, цвет: белый, размер S, сезон: зима'
        },
        {
            'name': 'Куртка_2',
            'image': 'jacket_2.jpg',
            'description': 'Женский пуховик-пальто, цвет: розовый, размер М, сезон: весна, осень'
        },
        {
            'name': 'Куртка_3',
            'image': 'jacket_3.jpg',
            'description': 'Мужская курта, цвет: серо-бежевый, размер М, сезон: весна, осень'
        },
        {
            'name': 'Куртка_4',
            'image': 'jacket_4.jpg',
            'description': 'Мужской пуховик, цвет: бежевый, размер М, сезон: зима'
        }
    ]
    return render_template('jackets.html', **context, jackets=jackets_list)


@app.route('/dresses/')
def dresses():
    context = {'title': 'Платья'}
    dresses_list = [
        {
            'name': 'Платье_1',
            'image': 'dress_1.jpg',
            'description': 'Платье черное, трикотаж, размер М'
        },
        {
            'name': 'Платье_2',
            'image': 'dress_2.jpg',
            'description': 'Платье коктейльное в черный горох, размер S'
        },
        {
            'name': 'Платье_3',
            'image': 'dress_3.jpg',
            'description': 'Платье с принтом Хризантемы, размер М'
        },
        {
            'name': 'Платье_4',
            'image': 'dress_4.jpeg',
            'description': 'Платье летнее шифоновое с голубым принтом, размер S'
        }
    ]
    return render_template('dresses.html', **context, dresses=dresses_list)


@app.route('/jeans/')
def jeans():
    context = {'title': 'Джинсы'}
    jeans_list = [
        {
            'name': 'Джинсы_1',
            'image': 'jeans_1.jpg',
            'description': 'Прямые женские джинсы, размер М'
        },
        {
            'name': 'Джинсы_2',
            'image': 'jeans_2.jpg',
            'description': 'Молодежные джинсы, размер М'
        },
        {
            'name': 'Джинсы_3',
            'image': 'jeans_3.jpg',
            'description': 'Женские черные джинсы, размер S'
        },
        {
            'name': 'Джинсы_4',
            'image': 'jeans_4.jpeg',
            'description': 'Джинсы для девочки, рост 134-146 см'
        }
    ]
    return render_template('jeans.html', **context, jeans=jeans_list)


@app.route('/skirts/')
def skirts():
    context = {'title': 'Юбки'}
    skirts_list = [
        {
            'name': 'Юбка_1',
            'image': 'skirt_1.jpg',
            'description': 'Юбка для девочки, рост 134-140'
        },
        {
            'name': 'Юбка_2',
            'image': 'skirt_2.jpeg',
            'description': 'Юбка школьная для девочки-подростка, рост 140-146'
        },
        {
            'name': 'Юбка_3',
            'image': 'skirt_3.jpg',
            'description': 'Длинная черная юбка, размер S'
        },
        {
            'name': 'Юбка_4',
            'image': 'skirt_4.jpg',
            'description': 'Длинная шифоновая черная юбка, размер М'
        }
    ]
    return render_template('skirts.html', **context, skirts=skirts_list)


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
