var pagina_atual;


function setPage(pagina){
    pagina_atual = pagina;
    var xmlHttp;
    try {
        xmlHttp=new XMLHttpRequest(); // Firefox, Opera 8.0+, Safari
    }
    catch (e) {
        try {
            xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");// Internet Explorer
        }
        catch (e){
            try {
                xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
            }
            catch (e) {
                alert("Seu navegador nao suporta AJAX. Atualize-o em www.getfirefox.com");
                return false;
            }
        }
    }
    xmlHttp.onreadystatechange=function() {
        if(xmlHttp.readyState == 1) {
            document.getElementById("content").innerHTML = "Carregando...<img src='./images/loading.gif'></img>";
        }
        if(xmlHttp.readyState == 4) {
            document.getElementById("content").innerHTML = xmlHttp.responseText;
        }
    }
    xmlHttp.open("GET",pagina,true);
    xmlHttp.send(null);
}


function getPage(){
    
	this.pagina_atual;
    var xmlHttp;
    try {
        xmlHttp=new XMLHttpRequest(); // Firefox, Opera 8.0+, Safari
    }
    catch (e) {
        try {
            xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");// Internet Explorer
        }
        catch (e){
            try {
                xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
            }
            catch (e) {
                alert("Seu navegador nao suporta AJAX. Atualize-o em www.getfirefox.com");
                return false;
            }
        }
    }
    xmlHttp.onreadystatechange=function() {
        if(xmlHttp.readyState == 1) {
            document.getElementById("content").innerHTML = "Carregando...<img src='./images/loading.gif'></img>";
        }
        if(xmlHttp.readyState == 4) {
            document.getElementById("content").innerHTML = xmlHttp.responseText;
        }
    }
	if(pagina_atual == null){
	    pagina_atual = "home.html";	
	}

    xmlHttp.open("GET",pagina_atual,true);
    xmlHttp.send(null);
}
