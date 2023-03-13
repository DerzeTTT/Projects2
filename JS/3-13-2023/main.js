const exec = require("child_process").exec

exec("echo Halo", (error, stdout) => {

    console.log(error, stdout)

})