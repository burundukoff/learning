
server {
    listen 80;
    
    root /var/www/html;
    
    location /new {
        root /tmp;
    }
}
Директива root может быть указана как в server block, так и в нужном location
Если не проваливаемся в location то берем root+хвост без домена (/var/www/html+хвост без домена) Хвост без домена подразумевается это location + сам файл

Если проваливаесся в location , то /tmp/+location+файл (/tmp/new+файл)
Если необходимо, чтобы location выкидывался , то используем alias
server {
    listen 80;
    
    root /var/www/html;
    
    location /new {
        alias /tmp;
    }
}
тогда /tmp/+файл и мы выкинули из пути location

Именованные location
location могут быть именованные, т.е. мы делаем направления в location по особым правилам
если получаем error pages то улдетаем в location not_faund
server {
    listen 80;
    
    root /var/www/html;
    
    error_page 404 = @not_found;
    
    location @not_found {
        rewrite ^(.*)$ /hello.txt break;
        root /tmp;
    }
}

Директива index
Директива index задает файлы, которые nginx будет искать, если пользователь не указал их в своем запросе
server {
    listen 80;
    
    root /tmp;
    
    index hello.txt;
}

Если пользователь будет запрашивать страницы без указания файла (например, http://example.org/ или http://example.org/path/to/directory/), то nginx добавит в конце файл hello.txt и будет его искать. Указать можно несколько файлов, например, index index.html index.php, тогда nginx будет пытаться обработать сначала index.html, а если не найдет его, то будет пытаться обработать index.php.

Директива try_files

Самая удобная (и самая часто встречающаяся) директива из всех, которые используются для обработки статики. Позволяет проверять несколько файлов, изменяя их пути, а также перекидывать запросы на именованные location
server {
    index index.php;
    root /var/www/blog;
    
    location / {
        try_files $uri $uri/ /index.php?$args;
    }
    
    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_intercept_errors on;
        fastcgi_pass php;
        fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }
}

try_files берет путь из root и пробует там искать файл по значению из локейшена. не находит? значит пробует взять путь из root, значение из локейшена и варианты из директивы index. если и их не находит, то пробует 3й вариант.


В данном случае при обработке / сначала проверяется существование файла в системе, если он есть — то он возвращается пользователю. Дальше к запросу добавляется / и проверяется наличие директории, внутри которой лежит index.php (index index.php). Если ни первый, ни второй варианты не сработали — запрос идет на /index.php файл с передачей аргументов."
каждая итерация, по сути, новый запрос. то есть на третий раз запрос из / улетит в локейшен где конец строки запроса оканчивается на .php

как пример:

    /index.jpg - если в root есть такой файл - отдаем. иначе...
    /index.jpg - пробуем так $root/index.jpg/index.php если и такого файла нет, то пробуем последний вариант


Опрашивем разные бакеты s3 , елси находим файл в тесте отдаем его, если не находим , то отдаем их бакета prod
server {
    listen 80;
    
    location / {
        try_files @dev @prod;
    }
    
    location @dev {
        proxy_http_version     1.1;
        proxy_set_header       Connection "";
        proxy_set_header       Authorization '';
        proxy_set_header       Host rebrain.dev.s3.amazonaws.com;
        add_header             Cache-Control max-age=31536000;
        proxy_pass             http://rebrain.dev.s3.amazonaws.com;
    }
    
    location @prod {
        proxy_http_version     1.1;
        proxy_set_header       Connection "";
        proxy_set_header       Authorization '';
        proxy_set_header       Host rebrain.prod.s3.amazonaws.com;
        add_header             Cache-Control max-age=31536000;
        proxy_pass             http://rebrain.prod.s3.amazonaws.com;
    }
}