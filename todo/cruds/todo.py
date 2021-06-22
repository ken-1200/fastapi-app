from sqlalchemy.orm import Session

from todo.models import Todo
from todo.schemas import TodoCreate, TodoUpdate

# id指定
def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

# 全取得
def get_todos(db: Session, limit: int = 100):
    return db.query(Todo).limit(limit).all()

# 作成
def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(title=todo.title, text=todo.text)

    # データの追加
    db.add(db_todo)

    # データの登録
    db.commit()

    # 一時データのリフレッシュ
    db.refresh(db_todo)
    return db_todo

# 更新
def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db_todo.title = todo.title
    db_todo.text = todo.text
    db.commit()
    return db_todo

# 削除
def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.delete(db_todo)
    db.commit()
