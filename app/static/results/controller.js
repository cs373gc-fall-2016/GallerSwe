angular.module('ArtSnob')
.controller('resultsController', ['$scope', 'SearchResults',
    function($scope, SearchResults) {
        'use strict';
        
        //
        //	Call the Timestamp service to fetch all the timestamps
        //
        $scope.reload = function() {
			SearchResults.get(data, function(response) {
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