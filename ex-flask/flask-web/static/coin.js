$(document).ready(function(){
    $(document).on('click','tr',function(){
        alert($(this).find('td').eq(2).text());
        let code =$(this).find('td').eq(2).text();
        let subUrl ="http://192.168.0.19:5000/coin";
        $.ajax({
            url :subUrl
            ,type:'POST'
            ,data:JSON.stringify({'market':code})
            ,dataType :'json'
            ,success:function(res){
            console.log(res);
            }
            ,error(e){
            console.log(e);
            }
        })
    });
});