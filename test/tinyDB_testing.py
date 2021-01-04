from tinydb import TinyDB, Query
from pprint import pprint
db = TinyDB('./resources/db.json')

setup1 = {'Ca':30, 'Na':100}
setup2 = {'Ca':100, 'O2':2} 
setup3 = {"Na":100, "fps":10}
parser = lambda setup: "_".join([key+'_'+str(setup[key]) for key in setup.keys()])

db.insert({'date': '01/01/2021', 'setup': setup1, 'file_dir': parser(setup1)} )
db.insert({'date': '01/02/2021', 'setup': setup2, 'file_dir': parser(setup2)} )
db.insert({'date': '01/03/2021', 'setup': setup3, 'file_dir': parser(setup3)} )

# pprint(db.all())

Trails = Query()
# condition = ( (Trails.setup.Ca > 10) | (Trails.setup.Na > 10) ) & ( (Trails.setup.Na >= 100) | (Trails.setup.fps == 10) ) 
condition = ( (Trails.setup.Ca > 10) ) & ( (Trails.setup.Na >= 100) | (Trails.setup.fps == 10) ) 

pprint(db.search(condition))

db.update({'setup':{'Ca': 10}}, condition)

pprint(db.search(condition))