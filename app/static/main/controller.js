angular.module('ArtSnob')
.controller('mainController', ['$scope', 'Artists',
    function($scope, Artists) {
        'use strict';
        
        //
        //	Call the Timestamp service to fetch all the timestamps
        //
        $scope.reload = function() {
			Artists.get(function(response) {
				$scope.response = response
                $scope.objects = response.objects
			    console.log("response is ", $scope.response)
			});
        }

        //
        //	Initial load
        //
        $scope.reload()
}]);