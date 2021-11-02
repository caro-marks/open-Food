<h1 > Python Challenge 20200228 </h1>
<h2 > API que baixa dados da Open Food Facts e popula no Atlas MongoDB </h2>

## Construída com Django, como challenge by Coodesh.

<h4> 
	 🚀 Primeira versão concluída...
</h4>

## Para reproduzir este projeto, é necessário ter Python e Pip atualizados, e uma conta no database Atlas do MONGODB.

### Clone este repositório

```
git clone <https://github.com/caro-marks/open-Food.git>
```

### Acesse a pasta do projeto no terminal/cmd

```
cd open-Food
```

### Crie um ambiente virtual e ative-o

```
python3 -m venv env
source ./env/bin/activate
```

### Instale as dependências

```
python -m pip install -r requirements.txt
```

### Crie um arquivo para configurações de ambiente, e insira suas credenciais devidamente, como exemplificado no arquivo .env-dist

### Rode os testes localmente

```
cd foodData
python manage.py test
```

### Execute a aplicação em modo de desenvolvimento

```
python manage.py runserver
```

#### O servidor inciará na porta:8000 - acesse <http://127.0.0.1:8000/>

## Alternativamente, os passos acima podem resumidos em 2 utilizando Docker-Compose

### Clone este repositório e acesse a pasta do projeto

```
git clone <https://github.com/caro-marks/open-Food.git>
cd open-Food
```

### Build Containers e Run com MAKEFILE

```
make build
```

### 🛠 Tecnologias

As ferramentas usadas na construção do projeto foi:

- [Django](https://www.djangoproject.com/)
- [DJango Rest Framwork](https://www.django-rest-framework.org/)
- [Atlas - MongoDB]()

Os arquivos CSV gerados foram criados utilizando os dados da API da Open Food Facts

- [Open Food Facts](https://br.openfoodfacts.org/data)

### <a>🚀Feito por</a>

<a href="https://www.linkedin.com/in/caro-marks">
   <b>Marcos Nolasco</b> 👋🏽
</a>

---
