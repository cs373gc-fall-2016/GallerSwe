angular.module('ArtSnob')

    .service('Artists', ['$http', function ($http) {
        // FIX THIS WHEN API WORKS!!
    	var url = '/hack-api/artist';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);