from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
company1 = Company(name='Company A', founding_year=1990)
company2 = Company(name='Company B', founding_year=2000)
dev1 = Dev(name='Dev 1')
dev2 = Dev(name='Dev 2')
session.add_all([company1, company2, dev1, dev2])
session.commit()

# Create sample freebies
freebie1 = Freebie(dev=dev1, company=company1, item_name='Item 1', value=10)
freebie2 = Freebie(dev=dev1, company=company2, item_name='Item 2', value=15)
freebie3 = Freebie(dev=dev2, company=company1, item_name='Item 3', value=20)
freebie4 = Freebie(dev=dev2, company=company2, item_name='Item 4', value=25)
session.add_all([freebie1, freebie2, freebie3, freebie4])
session.commit()
