function cargarNoticias(){

	var request=new XMLHttpRequest();
	
	request.open("GET","../xml/noticias.xml", true);
	request.addEventListener("load", mostrarNoticias, false);
	request.send();
	
	}
	
function mostrarNoticias(response){

	var docxml=response.target.responseXML;
	console.log(response);
	var noticias=docxml.getElementsByTagName("noticia");
    
    var divNotificaciones=document.getElementById("notificaciones");
    
    for(i=0; i<noticias.length; i++){
    noticia=noticias[i];
        nombre=noticia.getElementsByTagName("usuario")[0].innerHTML;
        fecha=noticia.getElementsByTagName("fecha")[0].innerHTML;
        descripcion=noticia.getElementsByTagName("descripcion")[0].innerHTML;
        
        var article=document.createElement("article");
        var usuario=document.createElement("h3");
        var descpnoti=document.createElement("p");


        usuario.innerHTML = nombre;
        descpnoti.innerHTML=descripcion+"</br>"+fecha;
        
        article.setAttribute("class", "noticias");
        article.appendChild(usuario);
        article.appendChild(descpnoti);
        
        divNotificaciones.appendChild(article);
        
        
    }
    
	}


window.addEventListener("load", cargarNoticias, false);
