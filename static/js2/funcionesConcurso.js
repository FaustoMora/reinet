function cargarConcurso(){
	var request=new XMLHttpRequest();
	request.open("GET","../xml/concursos.xml", true);
	request.addEventListener("load", mostrarConcurso, false);
	request.send();
}
	
function mostrarConcurso(response){
	var docxml=response.target.responseXML;
	console.log(response);
	var concursos=docxml.getElementsByTagName("concurso");
    
    var divLista=document.getElementById("lstConcursos");
    
    for(i=0; i<concursos.length; i++){
    concurso=concursos[i];
        nombre=concurso.getElementsByTagName("nombre")[0].innerHTML;
        descripcion=concurso.getElementsByTagName("descripcion")[0].innerHTML;
        participantes = concurso.getElementsByTagName("participantes")[0].innerHTML;
        ranking = concurso.getElementsByTagName("ranking")[0].innerHTML;

        urlimg="../images/sidLogo.png";
        urlestrella= "../images/estrella.jpg" 
        urlestrellaNegra= "../images/estrellanegra.jpg" 
        var divConcurso=document.createElement("div");

        var divImg=document.createElement("img");
        var divNombre=document.createElement("p");
        var divDescripcion=document.createElement("article");
        var anchor = document.createElement("a");
        var part = document.createElement("p");//parrafo donde se visualizara el num de participantes
        var rank = document.createElement("div");//div donde se colocaran las estrellas de ranking
        

        divNombre.innerText="Nombre: "+nombre;
        divDescripcion.innerText="Descripción: "+descripcion;
        divImg.setAttribute("src", urlimg);
        anchor.innerText = "Acceder";
        part.innerText = "Num. Participantes: " + participantes;
        for (j = 0; j < ranking;j++){
            var divEst = document.createElement("img");
            divEst.setAttribute("class", "estrella");
            divEst.setAttribute("src", urlestrella);
            divEst.setAttribute("alt", "estrella");
            rank.appendChild(divEst);    
        }
        for (k = 0; k < 5 - ranking;k++){
            var divEst = document.createElement("img");
            divEst.setAttribute("class", "estrella");
            divEst.setAttribute("src", urlestrellaNegra);
            divEst.setAttribute("alt", "estrella sin puntuar");
            rank.appendChild(divEst); 
        }

        divDescripcion.setAttribute("class","desc")
        divNombre.setAttribute("class", "lateral");
        divConcurso.setAttribute("class", "concurso");
        divImg.setAttribute("class", "logoconc");
        anchor.setAttribute("class","acceder color");
        anchor.setAttribute("href", "Concurso_Inicio.html");
        part.setAttribute("class", "participantes");
        rank.setAttribute("class", "ranking");

         

       
        divConcurso.appendChild(divImg);
        divDescripcion.appendChild(anchor);
        divConcurso.appendChild(divNombre);
        divConcurso.appendChild(divDescripcion);
        divConcurso.appendChild(rank);
        divConcurso.appendChild(part);
        divLista.appendChild(divConcurso);
       
         var url = document.URL;
        var res = url.split("=");
        var id= res[res.length-1];
        console.log(id);

        var links=document.getElementsByClassName("acceder");

     for (l = 0; l < links.length; l++) {
             links[l].setAttribute("href",links[l].getAttribute("href")+"? id="+id);
        
     }
        
    }
    
}


window.addEventListener("load", cargarConcurso, false);