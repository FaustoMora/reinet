	function go(ind) {
        if(ind==0){
        var elemento = document.getElementById("informacionEmpresa");
         elemento.style.display = 'block';
         elemento = document.getElementById("informacionAdministrador");
         elemento.style.display = 'none';
         elemento = document.getElementById("informacionContacto");
         elemento.style.display = 'none';
         elemento = document.getElementById("listaItem1");
         elemento.setAttribute("class", "seleccionado");
         elemento = document.getElementById("listaItem2");
         elemento.setAttribute("class", "");
         elemento = document.getElementById("listaItem3");
         elemento.setAttribute("class", "");
       
        }
	    if(ind==1){
        var elemento = document.getElementById("informacionEmpresa");
         elemento.style.display = 'none';
         elemento = document.getElementById("informacionAdministrador");
         elemento.style.display = 'block';
         elemento = document.getElementById("informacionContacto");
         elemento.style.display = 'none';
         elemento = document.getElementById("listaItem1");
         elemento.setAttribute("class", "");
         elemento = document.getElementById("listaItem2");
         elemento.setAttribute("class", "seleccionado");
         elemento = document.getElementById("listaItem3");
         elemento.setAttribute("class", "");
       
        }
        if(ind==2){
        var elemento = document.getElementById("informacionEmpresa");
         elemento.style.display = 'none';
         elemento = document.getElementById("informacionAdministrador");
         elemento.style.display = 'none';
         elemento = document.getElementById("informacionContacto");
         elemento.style.display = 'block';
         elemento = document.getElementById("listaItem1");
         elemento.setAttribute("class", "");
         elemento = document.getElementById("listaItem2");
         elemento.setAttribute("class", "");
         elemento = document.getElementById("listaItem3");
         elemento.setAttribute("class", "seleccionado");
       
        }
   	
 	}

 
