import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column , Integer, String, ForeignKey
from sqlalchemy import select 

from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base() 

class User(Base):
    __tablename__='user'
    user_id = Column(Integer,autoincrement=True,primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    
class Article(Base):
    __tablename__='article'
    article_id = Column(Integer,autoincrement=True,primary_key=True)
    title = Column(String)
    content = Column(String)
    authors = relationship("User", secondary="article_authors")
    
class ArticleAuthors(Base):
    __tablename__='article_authors'
    user_id = Column(Integer,ForeignKey("user.user_id"),primary_key=True,nullable=False)
    article_id = Column(Integer,ForeignKey("article.article_id"),primary_key=True,nullable=False)
    
engine=create_engine("sqlite:///./testdb.sqlite3")

if __name__=='__main__':
    with Session(engine,autoflush=False) as session:
        session.begin()
        try:
            author=session.query(User).filter(User.username=="vignesh").one()
            
            article = Article(title="Using relationship", content = "User relationship for Insert")
            
            article.authors.append(author)
            
            session.add(article)
        




#            article=Article(title="my new application",content="Python ORM")
#            session.add(article)
#            session.flush()
#            print("--- Get Article Id ---")
#            print(article.article_id)
            #raise Exception("Dummy Error")
#            article_authors= ArticleAuthors(user_id=1,article_id=article.article_id)
#            session.add(article_authors)
        except:
            print("Rolling back")
            session.rollback()
            raise
        else:
            print("No exception . Hence Commit")
            session.commit()
           
           











#    with Session(engine) as session:
#        articles = session.query(Article).filter(Article.article_id==1).all()
#        for article in articles:
#            print("Article : {}".format(article.title))
#            for author in article.authors:
#                print("Author : {}".format(author.username))



#    stmt = select(User)
#    print("---------------Query--------------")
#    print(stmt)
#    with engine.connect() as conn:
#        print("---------------Result--------------")
#        for row in conn.execute(stmt):
#            print(row)