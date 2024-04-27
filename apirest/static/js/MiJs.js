
    function getFecha(){
        const d = new Date();
        let text = d.toString();
        return text;
    }

    function Ir(cual){
        document.forms['mio'].action="/niveles/"+cual
        document.forms['mio'].submit();
     
     
       }function Ir1(cual){
        location.href=cual
       }
        function Confirmar(que,donde){
            if (confirm(que))
              location.href=donde
        }
       function Va(tipo){
        
        if(tipo=="i")
        document.forms['mio'].action="/niveles/i"
        if(tipo=="u"){
         
         document.forms['mio'].action="/niveles/u"   
        }
        
        document.forms['mio'].submit();    
     
       }
       $('#tree').tree({
        dataSource: [ 
          { 
            text: 'Planta 1', 
            children: [ 
              { text: 'Área 1', 
               children: [
                 { text: 'Equipo 1',
                   children: [
                     { text: 'Punto 1' },
                     { text: 'Punto 2' },
                     { text: 'Punto 3' }
                   ]
                 }
               ] 
              } 
            ] 
          }
        ]
      });
      
