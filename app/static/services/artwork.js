angular.module('ArtSnob')

    .service('Artwork', ['$http', function ($http) {
        // FIX THIS WHEN API IS DONE
    	var url = '/hack-api/artist';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);