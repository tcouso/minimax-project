//Based on the following Geeks for Geeks tutorial: https://www.geeksforgeeks.org/run-python-script-using-pythonshell-from-node-js/

//Import express.js module.

const express = require('express');
const app = express();

//Import PythonShell module.

const  {PythonShell} = require('python-shell');

//Router to handle the incoming event.

app.get("/", (req, res, next)=>{
    //Option object.
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], //get print results in real time
        args: ['thisisanargument']
    };

    PythonShell.run('python_test.py', options, function (err, result) {
        if (err) throw err;
        console.log('result: ', result.toString());
        res.send(result.toString())
    });
});

//Create server on the default port

const port=8000;
app.listen(port, ()=>console.log(`Server connected to ${port}`));
