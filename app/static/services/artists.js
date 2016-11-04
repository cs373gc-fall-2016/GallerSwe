angular.module('ArtSnob')

    .service('Artists', ['$http', function ($http) {
    	var url = '/api/artist';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);