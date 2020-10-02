function chooseLang(self){
if(self.classList.contains("unchosen-lang")){
    document.querySelectorAll(".lang-button").forEach((element) => {
        if(element.id !== self.id){
            element.classList.add("unchosen-lang")
        }
    })
    self.classList.remove("unchosen-lang")
}
}
