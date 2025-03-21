import dotenv
import os
from os.path import join, dirname

# print(env.SB_DB_Password)
print(__file__,'\n', dirname(__file__))

env_path = join(dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path=env_path)

print(os.environ, os.environ.get('SB_DB_Password'))

for k in os.environ:
    print(f"{k} -:- {1}\n")