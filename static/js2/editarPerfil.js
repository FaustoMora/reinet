function cargarEditarPerfil() {
	var request=new XMLHttpRequest();
	request.open("GET","../xml/usuarios.xml", true);
	request.addEventListener("load", mostrarEditarPerfil, false);
	request.send();
	
}
	
	
	
	
function mostrarEditarPerfil(response){
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

	var inputNombre=document.getElementById("editNombre");
	//var inputApellido=document.getElementById("editApellido");
	var inputIdentificacion=document.getElementById("editIdentificacion");
	var inputInstitucion=document.getElementById("editInstitucion");
	var inputCargo=document.getElementById("editCargo");
	var inputEmail=document.getElementById("editEmail");
	
	var inputPais=document.getElementById("editPais");
	var inputCiudad=document.getElementById("editCiudad");
	var inputFecha=document.getElementById("editFecha");
	
	

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
        var identificacion=perfil.getElementsByTagName("ci")[0].innerHTML;
        
        
        var sitioweb=perfil.getElementsByTagName("sitioweb")[0].innerHTML;
        var telefono=perfil.getElementsByTagName("telefono")[0].innerHTML;
        var correo=perfil.getElementsByTagName("correo")[0].innerHTML;

	
		
		inputNombre.value=nombre;
        //inputApellido.value=
        inputIdentificacion.value=identificacion;
        //inputInstitucion.value=institucion;
        inputCargo.value=cargo;
         inputEmail.value=correo;
        // inputPais.value=pais;
        inputCiudad.value=ciudad;
        // inputFecha.value=fecha;
    
    
    /*titulo Nombre*/
    
    var titulo=document.getElementById("tituloNombre");
    console.log(titulo.innerHTML);
    titulo.innerHTML="Editar Perfil <small>"+nombre+"</small>";  
    console.log(titulo.innerHTML, nombre);
    }   
}      
  }  
window.addEventListener("load", cargarEditarPerfil, false);
	   

	
