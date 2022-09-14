import sqlite3



def data_base_start():
	global db,cur

	db = sqlite3.connect('data_user.db')
	cur = db.cursor()

	if db:
		print('data_base on')

	cur.execute('''

		CREATE TABLE data_user (photo TEXT, name TEXT, description TEXT, data TEXT)

		''')

	db.commit()



async def db_add(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO data_user VALUES (?,?,?,?)', tuple(data.values()))
		db.commit()




