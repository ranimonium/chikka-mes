var http = require('http');
var fs = require('fs'); //file system
var url = require('url');
var redis = require('redis'),
	redis_client = redis.createClient();

redis_client.on("error", function (err) {
    console.log("Error " + err);
});

var newtodo = {'content' : '' };

updateToDoList(todoHTMLFile);

var server = http.createServer(function(req, res){

	// console.log(req);

	var todoHTMLFile = fs.readFileSync('./todo.html', 'utf8');
	
	if(req.method == "GET"){

		res.writeHead(200, {"Content-Type": "text/html"});
		var url_parts = url.parse(req.url, true);
		var query = url_parts.query;

		//push data to redis list "todolist"
		if(query.task != undefined && query.task.length > 0) {
			redis_client.rpush('todolist', query.task);

		}
		if(newtodo == ''){
			// console.log('\n\n\n\n todoHTMLFile \n\n\n\n' + todoHTMLFile);
			// res.end(todoHTMLFile);
		}
	}

	updateToDoList(todoHTMLFile);

	res.write(newtodo.content);

	console.log('\n\n\n\n newtodo \n\n\n\n' + newtodo);
	res.end();
}).listen(8888);

function updateToDoList(todoHTMLFile){
	redis_client.lrange('todolist', 0, -1, function(err, result){

		var todolistendindex = todoHTMLFile.search('<ul id="todolist">') + '<ul id="todolist">'.length;

		var todolist_result = "";
		for ( todoitem in result ) {
			todolist_result += "<li>" + result[todoitem] + "</li>";
		}

		newtodo.content = (todoHTMLFile.substring(0, todolistendindex) + todolist_result + todoHTMLFile.substring(todolistendindex));

	});

}


console.log('Server ready.');