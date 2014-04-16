chikka_mes
==========

#### curl client command for GET
curl localhost:60007/aux/dummyfile.html

#### curl client command for POST
curl -X POST --header "File:hello.html" localhost:60007 -v
curl -X POST --header "File:aux/hello.html" localhost:60007 -v

#### curl client command for OPTIONS