# plask
Plask is simple framework for practicing *Flask*


=== Example for hello world ===
    from plask import Plask
    
    app = Plask(__name__)
    
    @app.route('/')
    def index():
        return 'Hello index'
    
    @app.route('/hello')
    def say_hello():
        return 'Say Hello'
    
    if __name__ == '__main__':
        app.run()

