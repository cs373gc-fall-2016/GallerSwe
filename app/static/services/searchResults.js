angular.module('ArtSnob')

	.service('SearchResults', ['$http', function ($http) {

	    this.get = function(data, callback) {
	    	url = 'http://artsnob.me/search/' + data;
	        $http.get(url).then(function(response) {
	        	callback(response.data)
	        });

	        return
	    }
}]);
