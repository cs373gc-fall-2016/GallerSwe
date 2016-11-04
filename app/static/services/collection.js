angular.module('ArtSnob')

    .service('Collections', ['$http', function ($http) {
    	var url = '/api/collections';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);
