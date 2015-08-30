			// 画像変更
			function changeImage(action){
				var image = "img/" + action + "_" + Integer.toString(counter % 2) + ".png"
			//	$("#output").append(image);
				$("img").attr("src", image);
				count++;
				if ( count < 10) {
					setInterval(changeImage, 3000);
				}
			}
