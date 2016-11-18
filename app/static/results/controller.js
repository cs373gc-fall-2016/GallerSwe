angular.module('ArtSnob')
<<<<<<< HEAD
.controller('resultsController', ['$scope','$rootScope', 'SearchResults',
    function($scope, $rootScope, SearchResults) {
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

      //   $rootScope.$on('rootScope:searchTerm', function (event, data) {
      //   console.log("getting this :" + data)
      //   results.get( data, function(artistData) {
      //       $scope.objects = artistData
      //   });
      // });

        //
        //	Initial load
        //
        $scope.reload()
}]);

