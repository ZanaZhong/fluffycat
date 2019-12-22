$(document).ready(function() {
    // // $('#listTable').DataTable();
    // $("#listTable").on('click','.btnSelect',function(){
    //     // get the current row
    //     var currentRow=$(this).closest("tr"); 

    //     var col1=currentRow.find("td:eq(0)").html(); // get current row 1st TD value
    //     var col2=currentRow.find("td:eq(1)").text(); // get current row 2nd TD
    //     var col3=currentRow.find("td:eq(2)").text(); // get current row 3rd TD
    //     var data=col1+"\n"+col2+"\n"+col3;

    //     alert(data);
    // });

    $(".btnSelect").click(function() {
        console.log($(this).closest("tr"));
        $(this).closest("tr").remove();

    });

    $(".addSuspend").click(function(){
        var accountIDs = [];
        $.each($("input[name='accountId']:checked"), function(){
            accountIDs.push($(this).val().toString());
        });
        if(accountIDs.length != 0){
            if(confirm("Make sure you want to suspend Account: " + accountIDs)) {
                $.ajax({
                    headers: { "X-CSRFToken": "{{ csrf_token }}" },
                    type: "POST",
                    url: 'suspend/',
                    data: {
                        'id': accountIDs,
                    },
                    dataType: 'json',
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader("X-CSRFToken", '{% csrf_token %}');
                    },
                    success: function (data) {
                        alert("停權成功");
                        // alert(data.is_suspended)
                    }
                });
            } else {
                alert("good");
            }
        } else {
            alert("checked one or more account(s) first")
        }
    });

    $(".rmValue").click(function(){
        var accountIDs = [];
        $.each($("input[name='accountId']:checked"), function(){
            accountIDs.push($(this).val().toString());
        });
        console.log(accountIDs);
        // alert("Make sure you want to delete Account: " + accountIDs.join(", "));
        if(accountIDs.length != 0){
            // alert(typeof accountIDs+accountIDs[1]);
            if(confirm("Make sure you want to delete Account: " + accountIDs)) {
                $.ajax({
                    headers: { "X-CSRFToken": "{{ csrf_token }}" },
                    type: "POST",
                    url: 'del/',
                    data: {
                        'id': accountIDs,
                        // 'csrfmiddlewaretoken': '{% csrf_token %}'
                    },
                    dataType: 'json',
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader("X-CSRFToken", '{% csrf_token %}');
                    },
                    success: function (data) {

                        $.each(accountIDs, function( i, j){
                            $("#u"+j).closest("tr").remove();
                        });
                        alert("刪除成功");
                    }
                });
            } else {
                alert("good");
            }
        } else {
            alert("checked one or more account(s) first")
        }
    });

});