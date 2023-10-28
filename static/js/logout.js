function logout() {
	var expirationDate = new Date();
	expirationDate.setDate(expirationDate.getDate() - 30);

	document.cookie = "access_token=;" + 
					  "expires=" + expirationDate.toUTCString() + 
					  "; path=/;";
	document.cookie = "refrest_token=;" + 
					  "expires=" + expirationDate.toUTCString() + 
					  "; path=/;";

	location.href = "/auth/";
}