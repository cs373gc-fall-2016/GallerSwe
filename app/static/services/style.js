angular.module('ArtSnob')

    .service('Style', ['$http', function ($http) {
    	var url = '/api/style';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);
