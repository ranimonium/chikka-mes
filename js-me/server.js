var http = require('http');

var server = http.createServer(function(req, res){
	res.writeHead(200);
	res.end('Hello http\n');
}).listen(8888);

console.log('Server ready.');