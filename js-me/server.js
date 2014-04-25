var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');
var redis = require('redis'),
 redis_client = redis.createClient();

//check for redis errors
redis_client.on("error", function (err) {
    console.log("Error " + err);
});

var server = http.createServer(function(req, res){

	if(req.method == "POST") {
		var reqBody = '';

		req.on('data', function(data){
			reqBody += data;
			var formData = qs.parse(reqBody);
			
			if(formData.task != undefined && formData.task.length > 0){
				redis_client.rpush('todolist', formData.task);
			}
			if(formData.removeLast != undefined && formData.removeLast){
				redis_client.rpop('todolist');
			}
			updateToDoList(res);
		});
	} else {
			updateToDoList(res);
	}

}).listen(8888);

console.log('Server ready.');

function updateToDoList(res){
	var todoHTMLFile = fs.readFileSync('./todo.html', 'utf8');
	var todolist_result = '';
	redis_client.lrange('todolist', 0, -1, function(err, result) {
		for ( todoitem in result ) {
			todolist_result += "<li>" + result[todoitem] + "</li>";
		}

		var todolistendindex = todoHTMLFile.search('<ul id="todolist">') + '<ul id="todolist">'.length;
		todoHTMLFile = (todoHTMLFile.substring(0, todolistendindex) + todolist_result + todoHTMLFile.substring(todolistendindex));
		res.writeHead(200, {"Content-Type": "text/html"});
		res.end(todoHTMLFile);
	});
}