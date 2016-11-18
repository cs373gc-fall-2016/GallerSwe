angular.module('ArtSnob')

.controller('resultsController', ['$scope','$rootScope', 'SearchResults', 'localStorageService',
    function($scope, $rootScope, SearchResults, localStorageService) {
        'use strict';
        
        //
        //	Call the Timestamp service to fetch all the timestamps
        //
        $scope.reload = function() {
            console.log("I am loading the resultsController");
			$scope.objects = localStorageService.get("objects");
        }

        $rootScope.$on('rootScope:searchTerm', function (event, data) {
            console.log("I heard you");
            SearchResults.get(data, function(response) {
                localStorageService.set("objects", response.objects);
                $scope.response = response
                $scope.objects = response.objects
            });
        });
        

        //
        //	Initial load
        //
        $scope.reload()
}]);

