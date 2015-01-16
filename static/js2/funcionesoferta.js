
function cargarOfertas(){
	
//	alert("CARGAR OFERTAS");
	var request=new XMLHttpRequest();
	
	request.open("GET","../xml/ofertas.xml", true);
	request.addEventListener("load", mostrarOfertas, false);
	request.send();
	
	}
	
function mostrarOfertas(response){
//	alert("mostrar");
	var docxml=response.target.responseXML;
	console.log(response);
	var ofertas=docxml.getElementsByTagName("oferta");
    
    var divLista=document.getElementById("OfferList");
    
    for(i=0; i<ofertas.length; i++){
    oferta=ofertas[i];
        nombre=oferta.getElementsByTagName("nombre")[0].innerHTML;
        dominio=oferta.getElementsByTagName("dominio")[0].innerHTML;
        descripcion=oferta.getElementsByTagName("descripcion")[0].innerHTML;
        urlimg=oferta.getElementsByTagName("img")[0].innerHTML;
        
        var divOferta=document.createElement("div");
        var divImg=document.createElement("img");
        var divNombre=document.createElement("p");
        var divDominio=document.createElement("p");
        var divDescripcion=document.createElement("p");
        var divDetalle=document.createElement("p");
        
        divNombre.innerText="Nombre: "+nombre;
        divDominio.innerText="Dominio: "+dominio;
        divDescripcion.innerText="Descripción: "+descripcion;
        divImg.setAttribute("src", urlimg);
        divDetalle.innerText="Ver Detalle";
        
        divNombre.setAttribute("class", "lat");
        divDominio.setAttribute("class", "lat");
        divDescripcion.setAttribute("class", "lat");
        divOferta.setAttribute("class", "offer");
        divImg.setAttribute("class", "logooffer");
        divDetalle.setAttribute("class", "detail");
        
        divOferta.appendChild(divImg);
        
        divOferta.appendChild(divNombre);
        divOferta.appendChild(divDominio);
        divOferta.appendChild(divDescripcion);
        divOferta.appendChild(divDetalle);
        divLista.appendChild(divOferta);
        
    }
    
	}


window.addEventListener("load", cargarOfertas, false);
