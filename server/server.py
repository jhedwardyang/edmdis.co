import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
		user_data = web.input(input_song="no data")
		user_data.input
		return user_data.input_song

if __name__ == "__main__":
    app.run()
