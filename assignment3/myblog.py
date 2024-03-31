#myblog.py
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

import ner


app = Flask(__name__)



app.config['SECRET_KEY'] = 'fc3bb2a43ff1103895a4ee315ee27740'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_users_posts.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def htmlnewline(s):
    if s is None:
        return ""
    return s.replace("\n", "<br>")

app.jinja_env.filters['nl2br'] = htmlnewline


#Three table was made, but User table doesn't contain any important information, it is reserved for potential future use.

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User(id={self.id} name={self.username} email={self.email} posts={self.posts})"

    def pp(self):
        posts = '\n    '.join([str(p) for p in self.posts])
        return f"User(id={self.id} name={self.username} email={self.email})\n    {posts})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_name = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Dep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dependencies = db.Column(db.String(255), nullable=True)
    post_name = db.Column(db.String(50), db.ForeignKey('post.entity_name'), nullable=False)
    


		
		


@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'GET':
            return render_template('form.html', input=open('input.txt').read())
        else:
            docs = request.form['text']
            #text = "Apple was founded by Steve Jobs and Steve Wozniak."
            doc = ner.SpacyDocument(docs)     
                        
            entities = doc.get_entities()
            print("Submitted Text:", docs)
            print("Detected Entities:", entities)
            entity_names = [entity[3] for entity in entities]

            #Enter new entites, if it already exist, give up
            try:

                for name in entity_names:
                    new_entity = Post(entity_name=name, user_id=1)
                    
                    db.session.add(new_entity)
                    
                
                db.session.commit()

            except IntegrityError:
                db.session.rollback()  

            #Intitalize dependency here
            dependencies = doc.get_dependency_parse()
            dependency_list = []

            # Check dependencies and match them with correponding entities.
            all_posts = Post.query.all()

            for post in all_posts:

                matched_dependencies = []

                for dependency_parse in dependencies:
                    text = dependency_parse['text']
                    if text in post.entity_name.split():
                        dependency_str = f"{dependency_parse['head_text']} {dependency_parse['dep']} {dependency_parse['text']}"
                        
                        matched_dependencies.append(dependency_str)
                        
                #Check whether it is Null
                if matched_dependencies:
                    dependency_list.append(matched_dependencies)

                dependencies_str = " \n ".join(matched_dependencies)  

                if dependencies_str:
                    try:
                        # Check if a Dep entry already exists for this post, else rollback
                        existing_dep = Dep.query.filter_by(post_name=post.entity_name).first()
                        if existing_dep:
                            existing_dep.dependencies = dependencies_str
                        else:
                            # Otherwise, create a new Dep entry
                            new_dep = Dep(dependencies=dependencies_str, post_name=post.entity_name)
                            db.session.add(new_dep)

                        db.session.commit()
                    except IntegrityError:
                        db.session.rollback() 
                
            
            return render_template('result.html', markup=entity_names, dependencies=dependency_list, text=docs)
    
#This for third page which show database
@app.route('/database')
def show_database():
    deps = Dep.query.all()
    posts = Post.query.all()
    return render_template('database.html', deps=deps, posts=posts)


#This for delete button
@app.route('/delete_all', methods=['POST'])
def delete_post_dep():
    try:
        # Deletes everything in database
        db.session.query(Dep).delete()
        db.session.query(Post).delete()
        db.session.commit()
        return jsonify({'message': 'All data deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error', 'error': str(e)}), 500






if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)


