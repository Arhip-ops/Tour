const buttonSend = document.querySelector(selectors = ".send")
console.log(buttonSend)
buttonSend.addEventListener(
    type = "click",
    listener = (event) => {
        document.querySelector(selectors = ".emailDiv").style.display = "flex"
        
    }
)