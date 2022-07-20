from demo import db, User
# from demo import engine


# query_result = engine.execute("SELECT * FROM table;").fetchall()
# print(pd.DataFrame(query_result))

# itemtodelete = User.query.filter_by(username="test2").first()
# db.session.delete(itemtodelete)
# db.session.commit()

print(User.query.all())
print(User.query.filter_by(username="jlfrencher").first())