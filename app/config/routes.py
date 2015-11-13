
from system.core.router import routes

routes['default_controller'] = 'Restfuls'
routes['GET']['/products/show/<id>'] = 'Restfuls#show'
routes['GET']['/products/edit/<id>'] = 'Restfuls#edit'
routes['POST']['/update/<id>'] = 'Restfuls#update'
routes['GET']['/products/new'] = 'Restfuls#new'
routes['POST']['/products/new/add'] = 'Restfuls#add'
routes['POST']['/products/destroy/<id>'] = 'Restfuls#destroy'
