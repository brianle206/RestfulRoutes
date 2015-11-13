"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Restfuls(Controller):
    def __init__(self, action):
        super(Restfuls, self).__init__(action)
        self.load_model('Restful')

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        product = self.models['Restful'].get_all()
        print product
        return self.load_view('index.html', product=product)

    def show(self, id):
        show = self.models['Restful'].get_product_by_id(id)
        return self.load_view('show.html', show=show)

    def edit(self,id):
        edit = self.models['Restful'].get_product_by_id(id)
        return self.load_view('show.html', edit=edit)

    def update(self,id):
        print id
        update = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price'],
            'id': id
        }
        self.models['Restful'].update(update)
        return redirect('/')
    def new(self):
        return self.load_view('add.html')
    def add(self):
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        new = {
            'name': name,
            'description': description,
            'price': price
        }
        self.models['Restful'].add(new)
        return redirect('/')

    def destroy(self, id):
        self.models['Restful'].destroy(id)
        return redirect('/')


