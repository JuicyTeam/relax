import tornado.ioloop
import tornado.web
import model_factory

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def post(self):
        args = self.request
        try:
            model_factory.diagnosis(args)
            self.write("Execute successfully...")
        except Exception:
            self.write(Exception)

def make_app():
    return tornado.web.Application([
        (r"/application/diagosis", MainHandler),
        (r"/application/test", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()