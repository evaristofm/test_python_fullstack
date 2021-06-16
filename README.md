
# Tutorial test_python_fullstack com Django

# Como rodar o projeto

- No terminal, execute o comando
```
docker-compose up --build
```

- Não esqueça de rodar as migrations:
```
docker-compose exec web python manage.py migrate
```

- Não esqueça de criar um superuser para acessar a interface de admin:
```
docker-compose exec web python manage.py createsuperuser
```

- Uma outra opção interessante é executar esse comando para acessar o container:
```
docker-compose exec web bash
```

E a partir daí rodar os comandos normalmente, sem acrescentar `docker-compose exec web` na frente.

- Não esqueça de derrubar o container quando acabar
```
docker-compose down
```

Por fim, acesse o site neste link: [http://localhost:8000/](http://localhost:8000/)


