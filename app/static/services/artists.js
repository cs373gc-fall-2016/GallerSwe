angular.module('ArtSnob')

    .service('Artists', ['$http', function ($http) {
    	var url = 'http://artsnob.me/api/artist';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);