from sqlalchemy.orm import Session

from todo.models import Todo
from todo.schemas import TodoCreate, TodoUpdate


def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def get_todos(db: Session, limit: int = 100):
    return db.query(Todo).limit(limit).all()


def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(title=todo.title, text=todo.text)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db_todo.title = todo.title
    db_todo.text = todo.text
    db.commit()
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.delete(db_todo)
    db.commit()
