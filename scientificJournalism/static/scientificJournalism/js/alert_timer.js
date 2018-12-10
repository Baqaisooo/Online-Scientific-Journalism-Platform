setTimeout( function ( ) { $('#alert').remove() }, 10000 ); //displays alert for 10 seconds

    
    $(".close").click(function(){
        $("#alert").remove();
    });