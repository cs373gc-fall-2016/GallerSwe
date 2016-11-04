angular.module('ArtSnob')

    .service('About', ['$http', function ($http) {
    	var url = '/run-unit-tests';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response)
            });

            return
        }
}]);