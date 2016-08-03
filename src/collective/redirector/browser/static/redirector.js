/**
 * Change the target for an anchor or form tag to a specific page.
 * 
 * @param {string} redirectURL - URL or URL pattern to replace with the redirect url.
 * @param {string} redirect_to - URL to edirect to.
 * @param {string} urlRegex - URL Regex. If the urlRegex equals * go a global regex
 *							  test on each anchor or form tag. Otherwise, match
 *							  each anchor or form tag based on what the url starts with.
 */
function url_redirector(redirectURL, redirect_to, urlRegex){
	var urls = redirectURL.split(" ");
	if(urlRegex == "^"){
		for(index in urls){
			$("a[href^='"+urls[index]+"']:not(.allow-submit)").each(function(){
				var href = $(this).attr("href");
				if(href.indexOf("?original_url") == -1){
					$(this).attr("href", redirect_to+"?original_url="+href);	
				}
			});
			$("form[action^='"+urls[index]+"']:not(.allow-submit)").each(function(){
				var action = $(this).attr("action");
				if(action.indexOf("?original_url") == -1){
					$(this).attr("action", redirect_to+"?original_url="+action);
				}
			});
		};
	}else{
		$("a:not([href^='#']):not(.allow-submit)").each(function(){
			var $this = $(this);
			var href = $this.attr("href");
			for(i in urls){
				patt = new RegExp(urls[i]);
				if(patt.test(href) && href.indexOf("?original_url") == -1){
					$(this).attr("href", redirect_to+"?original_url="+href);
				}
			}
		});
		$("form:not(.allow-submit)").each(function(){
			var $this = $(this);
			var href = $this.attr("action");
			for(i in urls){
				patt = new RegExp(urls[i]);
				if(patt.test(href) && action.indexOf("?original_url") == -1){
					$(this).attr("action", redirect_to+"?original_url="+href);
				}
			}
		});
	}
}


$(document).ready(function(){
	
	var $redirect_items = $(".collective-redirect-data");
	$redirect_items.each(function(){
		$this = $(this);
		redirect_url = $this.attr("data-redirect");
		redirect_to = $this.attr("data-url");
		regex = $this.attr("data-regex");
		external_redirect = $this.attr("data-external-redirect");
		if(external_redirect == "true"){
			var not_on_site = "(http|https)://(?!" + base_url.replace(/\./g, "\\.")
				.replace(/\-/g, "\\-")
				.replace("http://", "")
				.replace("https", "")
			+ ").*";
			redirect_url += " ^" + not_on_site;
			redirect_url.trim();
			regex = "*";
		}
		url_redirector(redirect_url, redirect_to, regex);
	});
	
});