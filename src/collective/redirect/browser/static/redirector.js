function url_redirector(redirectURL, redirect_to, urlRegex){
	var urls = redirectURL.split(" ");
	for(index in urls){
		$("a[href"+urlRegex+"='"+urls[index]+"']:not(.allow-submit)").each(function(){
			var href = $(this).attr("href");
			$(this).attr("href", redirect_to+"?original_url="+href);
		});
		$("form[action"+urlRegex+"='"+urls[index]+"']:not(.allow-submit)").each(function(){
			var action = $(this).attr("action");
			$(this).attr("action", redirect_to+"?original_url="+action);
		});
	};
}


$(document).ready(function(){
	
	var $redirect_items = $(".collective-redirect-data");
	$redirect_items.each(function(){
		$this = $(this);
		redirect_url = $this.attr("data-redirect");
		redirect_to = $this.attr("data-url");
		regex = $this.attr("data-regex");
		url_redirector(redirect_url, redirect_to, regex);
		console.log(this);
	});
	
});