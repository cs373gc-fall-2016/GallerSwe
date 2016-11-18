angular.module('ArtSnob')

    .service('Style', ['$http', function ($http) {
    	var url = 'http://artsnob.me:5000/api/style';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);
