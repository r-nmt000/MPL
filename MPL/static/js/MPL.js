(function(){
    $('#submit').on('click', function(){
        code = $('#input').val();
        $.get("/mpl/api", {code: code}, function(data){
            $('#output').val(data['output']);
        });
    });
})();