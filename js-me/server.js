var http = require('http');
var url = require('url');
var fs = require('fs');
var redis = require('redis'),
 redis_client = redis.createClient();

//check for redis errors
redis_client.on("error", function (err) {
    console.log("Error " + err);
});

var server = http.createServer(function(req, res){
	var path = url.parse(req.url).pathname;
	// console.log(req.url);
	
	if(path.search("add") != -1){
		query = url.parse(req.url, true).query;
		// console.log(query);

		if(query.task != undefined && query.task.length > 0){
			redis_client.rpush('todolist', query.task);
		}

		//updatetodo
		getToDoList(res);
	} else if(path.search("remove")!= -1){
		redis_client.rpop('todolist');		

		//updatetodo
		getToDoList(res);
	}	else if(path.search("refresh") != -1){
		getToDoList(res);
	} else {
		fs.readFile('./todo.html', function(err, file){
			if(err){
				console.log("Error: " + err);
				return;
			}
			
			//updatetodo
			getToDoList(res, file+"");
		});
	}
}).listen(8888);

console.log('Server ready.');

function getToDoList(res, file){

	var todolist_result = '';
	redis_client.lrange('todolist', 0, -1, function(err, result) {

		for ( todoitem in result ) {
			todolist_result += "<li>" + result[todoitem] + "</li>";
		}

		if(file){
			var insert_i = file.search('<ul id="todolist">') + '<ul id="todolist">'.length;
			todolist_result = (file.substring(0, insert_i) + todolist_result + file.substring(insert_i));
		}
				
		// console.log(todolist_result)
		res.writeHead(200, {'Content-Type':'text/html'});
		res.end(todolist_result, 'utf-8');
	});
}