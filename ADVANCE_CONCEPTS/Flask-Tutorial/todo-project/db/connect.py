from sqlalchemy import create_engine , text

#engine = create_engine('sqlite:///sample.db')

engine = create_engine("mysql+mysqldb://juneuser:JuneDB12@localhost:3306/rocketcars",echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "hello"'))
    print(result.all())
