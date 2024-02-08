open = document.getElementById("btn")
let span = document.getElementsByClassName("close")[0]

open.addEventListener("click", function(){
    document.getElementById("modalwd").style.display='block'
})

span.addEventListener("click", function(){
    document.getElementById("modalwd").style.display='none'
})

