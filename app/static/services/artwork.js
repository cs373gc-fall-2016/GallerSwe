angular.module('ArtSnob')

    .service('Artwork', ['$http', function ($http) {
        // FIX THIS WHEN API IS DONE
        //var url = '/api/artwork';
    	var url = '/hack-api/artwork';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);
