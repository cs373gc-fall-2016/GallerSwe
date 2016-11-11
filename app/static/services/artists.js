angular.module('ArtSnob')

    .service('Artists', ['$http', function ($http) {
    	var url = ':5000/api/artist';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);
