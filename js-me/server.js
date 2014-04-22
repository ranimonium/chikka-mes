var http = require("http");

http.createServer(function(request, response) {
	
	response.writeHead(200, {"Content-Type": "text/sagf"});
	response.write("Hello World\n");
	// console.log(request['url'])
	response.end();
}).listen(8888);

console.log("Server has started.");

