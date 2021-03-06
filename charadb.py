import pymysql
import config

def get_all_characters():

	connector = pymysql.connect(
		host = config.host,
		user = config.user,
		passwd = config.passwd,
		db = config.db,
		charset = config.charset,
		cursorclass = pymysql.cursors.DictCursor)

	with connector.cursor() as cursor:
		sql = "select * from characters;"
		cursor.execute(sql)
		result = cursor.fetchall()

		response_list = []

		for i in range(len(result)):
			response_list.append(result[i])

		json_response = { "character_data" : response_list }			
		
		return json_response


def get_specified_color_characters(color):

	connector = pymysql.connect(
		host = config.host,
		user = config.user,
		passwd = config.passwd,
		db = config.db,
		charset = config.charset,
		cursorclass = pymysql.cursors.DictCursor)

	with connector.cursor() as cursor:
		sql = 'select * from characters where color = "%s";'% (color)
		cursor.execute(sql)
		result = cursor.fetchall()

		response_list = []

		for i in range(len(result)):
			response_list.append(result[i])

		json_response = { "character_data" : response_list }

		return json_response


def get_skill_characters(type, cut):

	connector = pymysql.connect(
		host = config.host,
		user = config.user,
		passwd = config.passwd,
		db = config.db,
		charset = config.charset,
		cursorclass = pymysql.cursors.DictCursor)

	with connector.cursor() as cursor:
		sql = 'select * from characters where id IN (select skill_id from skills where type = "%s" and cut = %s);'% (type, cut)
		cursor.execute(sql)
		result = cursor.fetchall()

		response_list = []

		for i in range(len(result)):
			response_list.append(result[i])

		json_response = { "character_data" : response_list }

		return json_response


	
			

