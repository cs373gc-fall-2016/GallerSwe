angular.module('ArtSnob')

	.service('SingleArtist', ['$http', function ($http) {

	    this.get = function(search_term, callback) {
				console.log("getting id: "+ artist_id);
	    	url = 'http://artsnob.me/search/' + search_term;
	    	console.log("getting url: "+url);
	        $http.get(url).then(function(artistData) {
	        	callback(artistData.data)
	        });

	        return
	    }
}]);
