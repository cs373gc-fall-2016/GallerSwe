angular.module('ArtSnob')

    .service('Artists', ['$http', function ($http) {

    	var url = '/hack-api/artist';

        this.get = function(callback) {
            $http.get(url).then(function(response) {
            	callback(response.data)
            });

            return
        }

     //    this.set = function(callback) {
     //        $http.post(url).then(function(response){
     //        	callback(response.data)
     //        });
     //    }

	    // this.reset = function(callback) {
	    //     $http.delete(url).then(function(response){
	    //     	callback(response.data)
	    //     })
	    // }
}]);