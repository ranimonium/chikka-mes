chikka_mes
==========

#### curl client command for GET
`curl localhost:60007/aux/dummyfile.html`
*`telnet localhost 80`
 * `GET \ HTTP/1.0`
#### curl client command for POST
`curl -X POST --header "File:hello.html" localhost:60007 -v`
`curl -X POST --header "File:aux/hello.html" localhost:60007 -v`


#### curl client command for OPTIONS
* `telnet localhost 80`
 * `OPTIONS\ HTTP/1.0`

#### NodeJS 
* sudo apt-get install node
* sudo apt-get install nodejs
* sudo apt-get install npm
* npm config set registry http://registry.npmjs.org/
* npm install web

#### js-me directory
* `todo.html`
 * simple todo list that you can push to and pop from
* `helloworld.js`
 * simple helloworld javascript program that you execute through nodejs (displays only "Hello world!") when executed
 * why am I even including this here
 * of course this is for learning log
* `server.js`
 * the me that I'm really supposed to be showing.
 * still in progress; so far it successfully sends "Hello World" to curl client
 * should mimic apache too. :3
