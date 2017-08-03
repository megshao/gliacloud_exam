Models:

	Cafe:
		id
		name:varchar(20)
		address:varchar(50)
		rating:float
		commodities:[commodit_id]
		open_time:varchar(50)
		image_url:text

		funs:
			update_cafe_info(name:string, address:string, open_time:string, image_url:string)
			cal_rating()
			add_commodity(new_commodity:Commodity)
			remove_commofity(commofity_id:int)
	Rate:
		id
		rated_cafe:cafe_id
		rating:float
		time:timestamp
		message:text
		user:user_id

		funs:
			remove()
			update_rating(rateing:float)
			update_message(message:string)

	User:
		id
		token:char(20)
		name:varchar(20)
		password:varchar(10)
		gender:1 or 0
		rated_list:[rate_id]

		funs:
			login()
			logout()
			garenate_token()
			update(name:string, gender:boolean)
			add_rated_list(rating:Rate)
			remove_rated_list(rate_id:int)

	Commodity:
		id
		name:varchar(20)
		price:int
		description:text
		image_url:text
		cafe:cafe_id

		funs:
			update(name:string, price:int, image_url:string, description:string)

