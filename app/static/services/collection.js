angular.module('ArtSnob')

    .service('Collection', ['$http', function ($http) {
    	var url = '/api/collection';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);
