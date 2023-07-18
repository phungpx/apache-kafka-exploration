# Environment Setup

## 1. Create virtual environment

- Direct to your target directory

```
cd <your-project-folder>
```

- Create a virtual enviroment (with a compatible python version)

```

python -m venv <environment-name>
```

- Activate virtual environemtn

```
source <environment-name>/bin/activate
```

- Install all dependencies

```
pip install -r requirements.txt
```

- In case, you don't have a effient requirement file, you need to install all necessary dependencies to this environment, and then export all dependencies to a requirement file.

```
pip freeze > requirements.txt
```
