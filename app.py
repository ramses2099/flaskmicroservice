from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dbdata.db"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# models
class Todo(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(200))
    completed: Mapped[int] = mapped_column(default=0)
    date_create: Mapped[datetime] =mapped_column(default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return '<Task %r>' % self.id

# only run one
# with app.app_context():
#     db.create_all()

@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
