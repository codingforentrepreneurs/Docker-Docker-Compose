const express = require("express")
const app = express()
const port = process.env.PORT || 3000
// function handleIndex (req, res) {
//     res.send("Hello world")
// }

app.get("/", (req, res)=>{
    res.send("Hello World")
})

app.get("/world", (req, res)=>{
    res.send("The World")
})


app.listen(port, ()=>{
    console.log(`Listening on http://localhost:${port}`)
})