angular.module('ArtSnob')

	.service('Results', ['$http', function ($http) {

	    this.get = function(search_term, callback) {
				console.log("getting id: "+ search_term);
	    	url = 'http://artsnob.me/search/' + search_term;
	    	console.log("getting url: "+url);
	        $http.get(url).then(function(search_term) {
	        	callback(search_term.data)
	        });

	        return
	    }
}]);
