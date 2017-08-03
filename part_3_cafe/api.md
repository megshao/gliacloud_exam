APIs:

	All http request need to add Query user_token to check user

	GET /cafes/list
		get cafe list

	GET /cafes/{id}
		get cafe detail by cafe_id

	POST /cafes
		create new cafe

		field:
			name:string
			address:string
			open_time:string

	PUT /cafes/{id}
		update cafe detail by cafe_id

		field:
			name:string
			address:string
			open_time:string

	DELETE /cafes/{id}
		delete cafe by cafe_id

	GET /cafes/{id}/rates
		get rating list for cafe

	POST /cafes/{id}/rates
		create new rate for cafe

		field:
			rating:float
			message:string

	GET /rates/{id}
		get rate by rate_id

	PUT /rates/{id}
		update rate bt rate_id

		field:
			message:string

	DELETE /rates/{id}
		delete rate by rate_id

	GET /cafes/{id}/commodities
		get commodities list in cafe

	POST /cafes/{id}/commodities
		create commodity in cafe

		field:
			name:string
			price:int
			description:string

	PUT /commodities/{id}
		update commodity by commodity_id

		field:
			name:string
			price:int
			description:string

	DELETE /commodities/{id}
		delete commodity by commodity_id

	POST /users
		create user

	GET /users/{id}
		get user detail by user_id

	PUT /users/{id}
		update user detail by user_id

		field:
			name:string
			gender:boolean

	DELETE /users/{id}
		delete user by user_id

	POST /users/login
		user login

		field:
			name:string
			password:string

	POST /users/logout
		user logout
