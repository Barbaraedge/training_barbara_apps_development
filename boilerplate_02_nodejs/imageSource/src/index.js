var fs = require("fs");

var appconfigLocal;
var appconfigGlobal;

setInterval(() => {
  appconfigLocal = JSON.parse(
    fs.readFileSync("/appconfig/appconfig.json", "utf8")
  );
  appconfigGlobal = JSON.parse(
    fs.readFileSync("/appconfig/global.json", "utf8")
  );

  console.log("===================");
  console.log("");
  console.log("Reading Secrets...");
  if (process.env.SECRET1) {
    console.log(process.env.SECRET1);
  }
  if (process.env.SECRET2) {
    console.log(process.env.SECRET2);
  }
  console.log("");
  console.log("Reading Global Config...");
  console.log(JSON.stringify(appconfigGlobal));

  console.log("");
  console.log("Reading Local Config...");
  console.log(JSON.stringify(appconfigLocal));
}, 5000);
