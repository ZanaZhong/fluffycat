$(document).ready(function() {
    $(".rmValue").click(function(){
        var petIDs = [];
        $.each($("input[name='petId']:checked"), function(){
            petIDs.push($(this).val().toString());
        });
        // console.log(petIDs);
        // $.each(petIDs, function( i, j){
        //     $("#u"+j).closest(".adopt-list"+j).remove();
        // });
        
        // alert("Make sure you want to delete pet: " + petIDs.join(", "));
        if(petIDs.length != 0){
            // alert(typeof petIDs+petIDs[1]);
            if(confirm("Make sure you want to delete pet: " + petIDs)) {
                $.ajax({
                    headers: { "X-CSRFToken": "{{ csrf_token }}" },
                    type: "POST",
                    url: 'del/',
                    data: {
                        'id': petIDs,
                        // 'csrfmiddlewaretoken': '{% csrf_token %}'
                    },
                    dataType: 'json',
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader("X-CSRFToken", '{% csrf_token %}');
                    },
                    success: function (data) {

                        $.each(petIDs, function( i, j){
                            $("#u"+j).closest(".adopt-list"+j).remove();
                        });
                        alert("刪除成功");
                    }
                });
            } else {
                alert("good");
            }
        } else {
            alert("checked one or more pet(s) first")
        }
    });

});