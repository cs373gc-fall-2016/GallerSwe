angular.module('ArtSnob')
.controller('artistsController', ['$scope', 'Artists',
    function($scope, Artists) {
        'use strict';

        $scope.reload = function() {
			Artists.get(function(response) {
				$scope.response = response
        $scope.objects = response.objects
			    console.log("response is ", $scope.response)
			});
        }

        $scope.ArtistSelected = function(artist) {
            $scope.artist = artist
        }

        $scope.ArtistDeselected = function() {
            $scope.artist = undefined
        }

        $scope.ArtworkSelected = function(artwork) {
        }

        $scope.sortType     = 'name'; // set the default sort type
        $scope.sortReverse  = false;  // set the default sort order
        //
        //	Initial load
        //
        $scope.reload()
}]);
