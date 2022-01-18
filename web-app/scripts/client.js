// Hello world client

const zmq = require('zeromq');

//socket to talk to the python server
console.log("Connection to python hello world server");
var requester = zmq.socket('req');

var reply_count = 0;
requester.on("message", function(reply) {
    console.log("Received reply", reply_count, ": [", reply.toString(), ']');
    reply_count += 1;
    if (reply_count === 10) {
        requester.close();
        process.exit(0);
    }
});

requester.connect("tcp://localhost:5555")

for (var i = 1; i < 10; i++) {
    console.log(`Sending request ${i}...`);
    requester.send("Hello");
}

process.on('SIGINT', function() {
    requester.close();
});
