
function cargarIncubacion(){
	
//	alert("CARGAR OFERTAS");
	var request=new XMLHttpRequest();
	
	request.open("GET","../xml/incubaciones.xml", true);
	request.addEventListener("load", mostrarIncubacion, false);
	request.send();
	
	}
	
function mostrarIncubacion(response){
//	alert("mostrar");
    
	var docxml=response.target.responseXML;
	console.log(response);
	var incubaciones=docxml.getElementsByTagName("incubacion");
    
    var divLista=document.getElementById("IncList");
    
    for(i=0; i<incubaciones.length; i++){
    incubacion=incubaciones[i];
        nombre=incubacion.getElementsByTagName("nombre")[0].innerHTML;
        tipo=incubacion.getElementsByTagName("tipo")[0].innerHTML;
        descripcion=incubacion.getElementsByTagName("descripcion")[0].innerHTML;
     //   urlimg=incubacion.getElementsByTagName("img")[0].innerHTML;
       urlimg="../images/sidLogo.png"; 
        var divIncubacion=document.createElement("div");
        var divImg=document.createElement("img");
        var divNombre=document.createElement("p");
        var divTipo=document.createElement("p");
        var divDescripcion=document.createElement("p");
        var divDetalle=document.createElement("p");
        
        divNombre.innerText="Nombre: "+nombre;
        divTipo.innerText="Tipo: "+tipo;
        divDescripcion.innerText="Descripción: "+descripcion;
        divImg.setAttribute("src", urlimg);
        divDetalle.innerText="Ver Detalle";
        
        divNombre.setAttribute("class", "lat");
        divTipo.setAttribute("class", "lat");
        divDescripcion.setAttribute("class", "lat");
        divIncubacion.setAttribute("class", "offer");
        divImg.setAttribute("class", "logooffer");
        divDetalle.setAttribute("class", "detail");
        
        divIncubacion.appendChild(divImg);
        
        divIncubacion.appendChild(divNombre);
        divIncubacion.appendChild(divTipo);
        divIncubacion.appendChild(divDescripcion);
        divIncubacion.appendChild(divDetalle);
        divLista.appendChild(divIncubacion);
        
    }
    
	}

    

window.addEventListener("load", cargarIncubacion, false);