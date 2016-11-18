angular.module('ArtSnob')

    .service('Collection', ['$http', function ($http) {
    	var url = 'http://artsnob.me:5000/api/collection';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }
}]);
