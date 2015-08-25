/*$(".rotate_table").each(function() {
    var table = $(this);
    var newrows = [];

    table.find("tr").each(function(){
        var i = 0;

        $(this).find("td").each(function(){
            i++;
            if(newrows[i] === undefined) { newrows[i] = $(""); }
            newrows[i].append($(this));
        });
    });

    table.find("tr").remove();
    $.each(newrows, function(){
        table.append(this);
    });
});*/
