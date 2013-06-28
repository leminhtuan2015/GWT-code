<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
	xmlns:og="http://opengraphprotocol.org/schema/"
	xmlns:fb="http://www.facebook.com/2008/fbml" dir="ltr" lang="en-US"
	xmlns:fb="http://ogp.me/ns/fb#">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta content="text/html; charset=UTF-16">
		<title>Superflashcard: Flashcards for everyone from everywhere</title>

		<meta name="description"
			content="Superflashcard software is to create, study and review flashcards with a long-term memory management using the theory of spaced repetition">
			<meta name="keywords"
				content="Superflashcard: language flashcards, exam test flashcards, ipods, iphones, window phone, android mobile, blackberry">

				<link rel="icon" type="image/png" href="favicon.png">
					<link href="css/saas-common.css" rel="stylesheet" type="text/css"
						media="all">
						<link href="css/saas-default.css" rel="stylesheet" type="text/css"
							media="all">
							<link type="text/css" rel="stylesheet"
								href="css/SuperFlashCard.css">

								<!-- <script type="text/javascript" language="javascript">
									var platform = navigator.platform;
									var userAgent = navigator.userAgent;
									//var ismobile=userAgent.match(/(iPad)|(iPhone)|(iPod)|(android)/i);
									//if (ismobile) {
									if ((platform.indexOf("iPhone") >= 0
											|| platform.indexOf("iPad") >= 0
											|| platform.indexOf("iPop") >= 0 || userAgent
											.indexOf("Android") >= 0)
											&& (userAgent.indexOf("Mozilla") >= 0 || userAgent
													.indexOf("Safari") >= 0)) {
										//returns true if user is using one of the following mobile browsers
										//alert("Should go to mobile site: [" + platform + "] [" + userAgent + "]");
										window.location
												.replace("http://www.m.superflashcard.com");
									}
									else if (window.location.href.indexOf("www") < 0 && window.location.href.indexOf("127.0.0.1") < 0) {
										var newurl = window.location.href;
										newurl = newurl.replace("http://", "http://www.");
										window.location.replace(newurl);
									}
									//else
									//       alert("Should go to normal site: [" + platform + "] [" + userAgent + "]");
								</script> -->

								<script type="text/javascript" language="javascript" src="superflashcard/superflashcard.nocache.js" charset="UTF-8"></script>
									 <script type="text/javascript" language="javascript" src="ga.js"></script>  
									  <script type="text/javascript" language="javascript" src="swfobject.js"></script>
								 <script type="text/javascript" language="javascript" src="//www.google.com/uds/api?file=uds.js&amp;v=1.0&amp;gwt=1"></script>  
<body oncontextmenu="return false;">
	<!--<div class="header">
	<div>
		<div class="center">
			<div class="topLinks" id="welcome"></div>
<h1 id="logo"><a href="http://superflashcard.com/"><img src="logo.png" alt="Superflashcard" border="0"></a></h1>
			<div class="nav"><div class="menu-main-nav-container"><ul id="menu-main-nav" class="menu">
</ul></div></div>
			

		</div>
	</div>
</div>
</div>

<div class="container"> 
	<div class="center" id="status"></div> 
	<div class="center" id="content"></div> 
	<div class="center" id="footer"></div> 
</div> 
-->
	<!--div.footer end -->

	<div id="loadingMessage"></div>
	<div id="appHolder"></div>
	<!-- OPTIONAL: include this if you want history support -->
	<iframe src="javascript:''" id="__gwt_historyFrame" tabIndex='-1'
		style="position: absolute; width: 0; height: 0; border: 0"></iframe>

	<!-- RECOMMENDED if your web app will not function without JavaScript enabled -->
	<noscript>
		<div
			style="width: 22em; position: absolute; left: 50%; margin-left: -11em; color: red; background-color: white; border: 1px solid red; padding: 4px; font-family: sans-serif">
			Your web browser must have JavaScript enabled in order for this
			application to display correctly.</div>
	</noscript>
	</div>
	<!--
<div id="footer"><a href="http://superflashcard.com/">About us</a> | <a href="http://superflashcard.com/">Blog</a>
| <a href="http://superflashcard.com/">Contact us</a>
| <a href="http://superflashcard.com/">Term of service</a></div>

-->
	</div>


	<div id="adsense" style="display: none;">
		<script id="adsense-script" type="text/javascript"
			src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
			
		</script>
	</div>


	<!-- Begin Ad Call Tag - Do not Modify -->
	<!--
<div id="lifestreet" style="display: none;">
<iframe width='468' height='60' frameborder='no' framespacing='0' scrolling='no' src='//ads.lfstmedia.com/slot/slot43129?ad_size=468x60&adkey=1ef'></iframe>
</div>
-->
	<!-- End of Ad Call Tag -->

	<div id="fb-root"></did>
		<script>
			 var facebookLoaded = 0;
			window.fbAsyncInit = function() {
				facebookLoaded = 1;
				FB.init({
	 	 			  appId : '164743756926136',  /* main version*/ 
				   /*      appId	: '388712944501004',  */   /* test version*/
					status : true,
					cookie : true,
					xfbml : true
				});
			}; 
			//Load the SDK Asynchronously
			/* (function(d) {
				var js, id = 'facebook-jssdk', ref = d
						.getElementsByTagName('script')[2];
				if (d.getElementById(id)) {
					return;
				}
				js = d.createElement('script');
				js.id = id;
				js.async = true;
				js.src = "//connect.facebook.net/en_US/all.js";
				ref.parentNode.insertBefore(js, ref);
			}(document)); */
			
			(function(d, s, id) {
			  var js, fjs = d.getElementsByTagName(s)[0];
			  if (d.getElementById(id)) return;
			  js = d.createElement(s); js.id = id;
			 /*      js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=388712944501004"; */     /* test version*/
			    js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=164743756926136";     /* main version*/
			  fjs.parentNode.insertBefore(js, fjs);
			}(document, 'script', 'facebook-jssdk'));
		</script>
</body>
</html>
