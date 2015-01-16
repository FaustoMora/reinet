function cargarPerfil() {
	var request=new XMLHttpRequest();
	request.open("GET","../xml/usuarios.xml", true);
	request.addEventListener("load", mostrarPerfil, false);
	request.send();
}

	
function mostrarPerfil(response){
	var docxml=response.target.responseXML;
	console.log(response);
	var perfiles=docxml.getElementsByTagName("usuario");
	var url = document.URL;
    var res = url.split("=");
    var id= res[res.length-1];
    console.log(id);

    var links=document.getElementsByClassName("link");

    for (i = 0; i < links.length; i++) {
         links[i].setAttribute("href",links[i].getAttribute("href")+"? id="+id);
        
    }

	var infogeneralTbody=document.getElementById("infogeneral");
	var infocontactoTbody=document.getElementById("infocontacto");
	
	var a_avatar=document.getElementById("a_avatar");
	var principlNombre=document.getElementById("principalNombre");
	
	var fotitoMensaje=document.getElementById("mensajeFoto");
	var tituloMensaje=document.getElementById("mensajeTitulo");
	
    for(i=0; i<perfiles.length; i++){
         perfil=perfiles[i];
         var idPerfil = perfil.getElementsByTagName("id")[0].innerHTML;
         console.log(idPerfil);
         if(idPerfil==id){
         var nombre=perfil.getElementsByTagName("nombre")[0].innerHTML;
        var fechaNac=perfil.getElementsByTagName("nacimiento")[0].innerHTML;
        var institucion=perfil.getElementsByTagName("institucion")[0].innerHTML;
        var cargo=perfil.getElementsByTagName("cargo")[0].innerHTML;
        var actividad=perfil.getElementsByTagName("actividad")[0].innerHTML;
        var pais=perfil.getElementsByTagName("pais")[0].innerHTML;
        var ciudad=perfil.getElementsByTagName("ciudad")[0].innerHTML;
        var fotourl=perfil.getElementsByTagName("foto")[0].innerHTML;
        var intereses=perfil.getElementsByTagName("areasinteres")[0].innerHTML;
        
        
        var sitioweb=perfil.getElementsByTagName("sitioweb")[0].innerHTML;
        var telefono=perfil.getElementsByTagName("telefono")[0].innerHTML;
        var correo=perfil.getElementsByTagName("correo")[0].innerHTML;
    
    /*nombre principal*/
    principalNombre.innerHTML=nombre+" <br><small>"+institucion+"</small>"
    
    
	/*imagen avatar principal*/
	
	a_avatar.removeChild(a_avatar.firstChild);
		a_avatar.innerHTML="  <img src="+"\""+fotourl+"\""+" alt=\"fotoperfil\">"	
			   
			   /*datos*/
        
			var tr1=document.createElement("tr");
			var td1a=document.createElement("td");
			var td1b=document.createElement("td");
			        

			var tr2=document.createElement("tr");
			var td2a=document.createElement("td");
			var td2b=document.createElement("td");
			        
			var tr3=document.createElement("tr");
			var td3a=document.createElement("td");
			var td3b=document.createElement("td");
			        
			var tr4=document.createElement("tr");
			var td4a=document.createElement("td");
			var td4b=document.createElement("td");
			        
			var tr5=document.createElement("tr");
			var td5a=document.createElement("td");
			var td5b=document.createElement("td");
			        
			var tr6=document.createElement("tr");
			var td6a=document.createElement("td");
			var td6b=document.createElement("td");
			        
			var tr7=document.createElement("tr");
			var td7a=document.createElement("td");
			var td7b=document.createElement("td");
			       
			        
			var tr8=document.createElement("tr");
			var td8a=document.createElement("td");
			var td8b=document.createElement("td");
			        
 
			var tr9=document.createElement("tr");
			var td9a=document.createElement("td");
			var td9b=document.createElement("td");
			        
			var tr10=document.createElement("tr");
			var td10a=document.createElement("td");
			var td10b=document.createElement("td");
			        
			var tr11=document.createElement("tr");
			var td11a=document.createElement("td");
			var td11b=document.createElement("td");
			        
			var tr12=document.createElement("tr");
			var td12a=document.createElement("td");
			var td12b=document.createElement("td");
			       
			       
			 td1a.innerText="Nombre";
			 td1b.innerText=nombre;
			 
			 td2a.innerText="Institucion";
			 td2b.innerText=institucion;
			 
			 td3a.innerText="Fecha de Nacimiento";
			 td3b.innerText=fechaNac;
			 
			 td4a.innerText="Cargo";
			 td4b.innerText=cargo;
			 
			 td5a.innerText="Actividad";
			 td5b.innerText=actividad;
			 
			 td6a.innerText="Pais";
			 td6b.innerText=pais;
			 
			 td7a.innerText="Ciudad";
			 td7b.innerText=ciudad;
			 
			 td8a.innerText="Intereses";
			 td8b.innerText=intereses;
			 
			 /*contacto*/
			 td9a.innerText="Sitio Web";
			 td9b.innerText=sitioweb;
			 
			 td10a.innerText="Teléfono";
			 td10b.innerText=telefono;
			 
			 td11a.innerText="Correo";
			 td11b.innerText=correo;
			   
			   /*aniadir clases*/
			   td1a.setAttribute("class", "text-muted");
			   td2a.setAttribute("class", "text-muted");
			   td3a.setAttribute("class", "text-muted");
			   td4a.setAttribute("class", "text-muted");
			   td5a.setAttribute("class", "text-muted");
			   td6a.setAttribute("class", "text-muted");
			   td7a.setAttribute("class", "text-muted");
			   td8a.setAttribute("class", "text-muted");
			   td9a.setAttribute("class", "text-muted");
			   td10a.setAttribute("class", "text-muted");
			   td11a.setAttribute("class", "text-muted");
			   
			   
			   /*appenchild*/
			   
			   tr1.appendChild(td1a);
			   tr1.appendChild(td1b);
			   
			   tr2.appendChild(td2a);
			   tr2.appendChild(td2b);
			   		   
			   tr3.appendChild(td3a);
			   tr3.appendChild(td3b);
			   		   
			   tr4.appendChild(td4a);
			   tr4.appendChild(td4b);
			   		   
			   tr5.appendChild(td5a);
			   tr5.appendChild(td5b);
			   		   
			   tr6.appendChild(td6a);
			   tr6.appendChild(td6b);
			   		   
			   tr7.appendChild(td7a);
			   tr7.appendChild(td7b);
			   		   
			   tr8.appendChild(td8a);
			   tr8.appendChild(td8b);
			   /*contacto*/		   
			   tr9.appendChild(td9a);
			   tr9.appendChild(td9b);
			   		   
			   tr10.appendChild(td10a);
			   tr10.appendChild(td10b);
			   		   
			   tr11.appendChild(td11a);
			   tr11.appendChild(td11b);		   
			   
			   
			   
			   
			   
			   infogeneralTbody.appendChild(tr1);
			   infogeneralTbody.appendChild(tr2);
			   infogeneralTbody.appendChild(tr3);
			   infogeneralTbody.appendChild(tr4);
			   infogeneralTbody.appendChild(tr5);
			   infogeneralTbody.appendChild(tr6);
			   infogeneralTbody.appendChild(tr7);
			   infogeneralTbody.appendChild(tr8);
			   
			   infocontactoTbody.appendChild(tr9);
			   infocontactoTbody.appendChild(tr10);
			   infocontactoTbody.appendChild(tr11);
			   
	/*foto y titulo del modal mensaje*/
	 fotitoMensaje.setAttribute("src", fotourl);
	 tituloMensaje.innerText=nombre+"  -  "+institucion;
	
        }
    }
    
    
}


window.addEventListener("load", cargarPerfil, false);
	
