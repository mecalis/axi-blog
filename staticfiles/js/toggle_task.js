$(document).ready(function(){

    $(".task_done").click(function(){
        $.ajax({
            url: '',
            type: 'post',
            data: {
                task_id = $(this).attr('id')
                console.log(task_id)
             },


        });

    });




});