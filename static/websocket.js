var ws = new WebSocket( "ws://" + document.location.hostname + ":9000");

function connect(pageName){
    ws = new WebSocket( "ws://" + document.location.hostname + ":9000");

    ws.onmessage = function(e)
    {
        incomingData = JSON.parse( e.data );
        console.log(incomingData)

    }

    ws.onopen = function(e)
    {
        console.log( "ws open " + pageName);
        var start = 
        {
            Command: "Start",
            Data:
            {
                "pageName" : pageName
            }
            
        }
        ws.send( JSON.stringify( start ) )
    }

    ws.onclose = function(e)
    {
        console.log('Socket is closed. Reconnect will be attempted in 1 second.', e.reason);
        setTimeout(function() {
            connect();
          }, 1000);
    
    }

    ws.onerror = function( e )
    {
        console.log( "ws error" );
    };

}
