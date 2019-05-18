require('lighthouse');

var exec = require('child_process').exec;

const args = process.argv.slice(2)
var url = args[0]

// output-path pasar una variable
child = exec("lighthouse " + url + " --output=csv --output-path=./report.csv", function (error, stdout, stderr) {
    console.log(stdout)
    console.log(stderr);
    if (error !== null) {
      console.log('exec error: ' + error);
    }                                                                                                         
  });
//https://github.com/GoogleChrome/lighthouse/blob/master/docs/understanding-results.md