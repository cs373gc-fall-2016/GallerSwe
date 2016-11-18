angular.module('ArtSnob')

	.service('SingleArtist', ['$http', function ($http) {


		var observerCallbacks = [];

		//register an observer
		this.registerObserverCallback = function(callback){
		observerCallbacks.push(callback);
		};

		//call this when you know 'foo' has been changed
		var notifyObservers = function(){
			angular.forEach(observerCallbacks, function(callback){
			  callback();
			});
		};

	    this.get = function(artist_id, callback) {
	    	url = 'http://artsnob.me:5000/api/artist/' + artist_id;
	        $http.get(url).then(function(artistData) {
	        	callback(artistData.data)
	        	notifyObservers();
	        });

	        return
	    }
}]);
