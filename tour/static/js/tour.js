const urls = document.querySelectorAll(".tourUrl")

for (let count = 0; count < urls.length; count ++){
    let url = urls[count]
    url.addEventListener(
        type = "click",
        listener = function (
            event
        ){
           document.cookie = `tour=${url.id}; path = /`
        }
    )
}