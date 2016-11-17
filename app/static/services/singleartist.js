angular.module('ArtSnob')

	.service('SingleArtist', ['$http', function ($http) {

	    this.get = function(artist_id, callback) {
				console.log("getting id: "+ artist_id);
	    	url = 'http://artsnob.me:5000/api/artist/' + artist_id;
	    	console.log("getting url: "+url);
	        $http.get(url).then(function(artistData) {
	        	callback(artistData.data)
	        });

	        return
	    }
}]);
