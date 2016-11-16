angular.module('ArtSnob')

    .service('Artwork', ['$http', function ($http) {
    	var url = 'http://artsnob.me:5000/api/artwork';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);
