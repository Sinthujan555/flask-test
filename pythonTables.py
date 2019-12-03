user1 = Users(email='chester.gardner@qa.com',password='password')
db.session.add(user1)
db.session.commit()
Users.query.first()
