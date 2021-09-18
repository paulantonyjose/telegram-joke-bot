
// Function to simply format the text in the right way. May end up being more complicated when you have MCQs, etc.
function generate_formatted_chat_message(data){
	 	if ('joke' in data){
			joke =data['joke']

			message_text = '<span class="message-text">' +joke['text']+ '</span>'
		 }
		else{
			message_text = '<span class="message-text">' +'Initiated'+ '</span>'
		}

		return message_text;

}
// Function that adds a message to the chat window
function add_message_to_chat(data, formatted_div){
	var chat = $('#messages-container');
	var new_source = data["source"];


		var child = $('<div class="msg-row">');
		$(child).append('<div class="row"><div class="col-xs-10 col-sm-10 col-md-10 col-lg-10  pull-right no-sides-padding msg-animate"><div class="panel message-panel user-msg"><div class="panel-body user-msg-body"><div class="message-text"><span></span></div></div></div><div class="user-msg-bubble"></div></div>');
		$(child).find('span').html(formatted_div);
		chat.append(child);
	
	$("#body-container").scrollTop( $('#body-container')[0].scrollHeight);	
}  


// Function taht is called when the server sends a message via websockets to my front end.
function processAndDisplayChatMessage(message){
	var content_data = JSON.parse(message.data);
	var formatted_div = generate_formatted_chat_message(
		content_data);
	
	if(formatted_div.length > 0){
		add_message_to_chat(content_data, formatted_div);
	}
}


function sendTextMessage(joke_id) {
	

    message = {}
    message.text = joke_id
    message.command= 'send'
    
    
	chatsock.send(JSON.stringify(message));
    return false;   
}
		