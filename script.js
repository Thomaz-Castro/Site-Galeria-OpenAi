function abrirImagem(src) {
    // cria o elemento de imagem grande
    var imgGrande = document.createElement("img");
    imgGrande.setAttribute("src", src);
    imgGrande.setAttribute("id", "imgGrande");
    
    // adiciona o elemento de imagem grande ao corpo da página
    document.body.appendChild(imgGrande);
    
    // adiciona um evento de clique ao elemento de imagem grande para fechá-lo
    imgGrande.onclick = function() {
      document.body.removeChild(imgGrande);
    }
  }
  