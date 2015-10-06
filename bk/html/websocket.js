	var output;
	function Connect(wsUri, onReceive)
	{
		output = document.getElementById("output");
		websocket = new WebSocket(wsUri);
		websocket.onopen = function(evt) { onOpen(evt) };
		websocket.onclose = function(evt) { onClose(evt) };
		websocket.onmessage = function(onReceive)(evt);
		websocket.onerror = function(evt) { onError(evt) };
	}

	function Close()
	{
		websocket.close();
	}

	/**
		WebSocket接続時
	*/
	function onOpen(evt)
	{
		writeToScreen("Connected");
	}

	/**
		WebSocket切断時
	*/
	function onClose(evt)
	{
		writeToScreen("Disconnected");
	}

	/**
		エラー発生時
	*/
	function onError(evt)
	{
		writeToScreen('<span style="color: red;">Error:</span> ' + evt.data);
	}

	/**
		メッセージ送信
	*/
	function onSend(message)
	{
		writeToScreen("Sent: " + JSON.stringify(message));
		websocket.send(JSON.stringify(message));
	}

	function writeToScreen(message)
	{
		var pre = document.createElement("li");
		pre.innerHTML = message;
		output.appendChild(pre);
	}
