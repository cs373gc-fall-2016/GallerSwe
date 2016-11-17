angular.module('ArtSnob')

.service('Artists', ['$http', function ($http) {
	var url = 'http://artsnob.me:5000/api/artist?q=%7B%22order_by%22:%5B%7B%22field%22:%22name%22%7D%5D%7D';

    this.get = function(callback) {
        $http.get(url).then(function(response) {
        	callback(response.data)
        });

        return
    }
}]);
