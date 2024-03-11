from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

import ner

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc3bb2a43ff1103895a4ee315ee27740'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_users_posts.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User(id={self.id} name={self.username} email={self.email} posts={self.posts})"

    def pp(self):
        posts = '\n    '.join([str(p) for p in self.posts])
        return f"User(id={self.id} name={self.username} email={self.email})\n    {posts})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



		
		


@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'GET':
            return render_template('form.html', input=open('input.txt').read())
        else:
            text = request.form['text']
            doc = ner.SpacyDocument(text)
            
            markup = doc.get_entities()
            

            #dependecies added here, check the dependency_parse function under ner.py
            dependencies = doc.get_dependency_parse()
            dependency_str = ""
            for dep in dependencies:
                dependency_str += f"{dep['head_text']} {dep['dep']} {dep['text']} <br>\n"

            entities = doc.get_entities()

            

            entity_names = [entity[3] for entity in entities]

            for name in entity_names:
                new_entity = Post(entity_name=name, user_id=1)
                db.session.add(new_entity)
            
            db.session.commit()
    

            

            

            return render_template('result.html', markup=entity_names, dependencies=dependency_str, text=text )
    

@app.route('/database')
def show_database():
    posts = Post.query.all()
    return render_template('database.html', posts=posts)




if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(debug=True)


"""

curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/john
curl -X POST http://127.0.0.1:5000/john/john@example.com
curl -X POST http://127.0.0.1:5000/john/hello/world
curl -X POST http://127.0.0.1:5000/john/byebye/country

"""
