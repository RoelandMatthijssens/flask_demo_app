What is flask:
Flask is a python micro framework for web request.
Its a lightweight modular framework build for speed and extendability.
It doesn't have a strict standard for project structure.

It doesn't come with it's own ORM like many other frameworks do 
rails -> active record
django -> object relational mapper
symphony -> doctrine

It uses jinja templates for rendering HTML

Why flask instead of other frameworks:
The fact that is super lightweight, and doesn't try to do everything is appealing to me. You get what you ask for and nothing more. You get a fast small web framework without too many bells and whistles.

Setup a simple flask app.
create simple app
    demonstrate adding routes (lists, products)
    Show splitting the app into modules
        move each route to module
    Templating
        create new product form
    create post request
        create new product

Connect to simple database.
    Create db schema
    create db file
        get_db
        close_db
        init_db
        create_command
    run command
        check sqlite for table
            .tables
    run query


Handle parameterized requests.


General python remarks:
Python uses indentation for scope structuring. No brackets/braces
package manager = pip.
    pip install flask
