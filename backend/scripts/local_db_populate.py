from database.db import engine, Base, print_success
from database.models.Projects import Project, WorkTime
# from database.models.Study_stats import Study_Time

Base.metadata.create_all(bind=engine)

# print(WorkTime, Project)
print(Base.registry.mappers)

# print('what')

# for mapper in Base.registry.mappers:
#     print(mapper.class_.__name__)
#     print('Boom')