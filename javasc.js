var Message;
Message = function (arg) {
    this.text = arg.text, this.message_side = arg.message_side;
    this.draw = function (_this) {
        return function () {
            var $message;
            $message = $($('.message_template').clone().html());
            $message.addClass(_this.message_side).find('.text').html(_this.text);
            $('.messages').append($message);
            return setTimeout(function () {
                return $message.addClass('appeared');
            }, 0);
        };
    }(this);
    return this;
};

var getMessageText, message_side, sendMessage;
message_side = 'right';
/*getMessageText = function () {
    var $message_input;
    $message_input = $('.message_input');
    return $message_input.val();
};*/
sendMessage = function (text) {
    var $messages, message;
    if (text === '') {
        return;
    }
    $('.message_input').val('');
    $messages = $('.messages');
    message_side = message_side === 'left' ? 'right' : 'left';
    message = new Message({
        text: text,
        message_side: message_side
    });
    message.draw();
    return $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
};




 $(function() {
     $('#send_message').bind('click', function() {
        t = $('input[name= "message_input"]').val();
       $.getJSON('/get_message', {

         message_input : $('input[name= "message_input"]').val()


       }, function(data) {

            if(t != "")
             sendMessage(t);
             setTimeout(1000);
            if(data != "")
             sendMessage(data)

        });
       return false;
    });
});



 $(function() {
     $('#speechRecog').bind('click', function() {
       $.getJSON('/speechRecog', {
    
            }, function(data) {
               // data = data.split(',');
             //alert(data[0]+"   "+data[1]);
             if(data[0]!="")
              sendMessage(data[0]);
              setTimeout(1000);
             if(data[1]!="")
              sendMessage(data[1]); 
            
        });
       return false;
    });
});
    


