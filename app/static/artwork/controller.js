angular.module('ArtSnob')
.controller('artworkController', ['$scope', 'Artwork',
    function($scope, Artwork) {
        'use strict';

        $scope.reload = function() {
			Artwork.get(function(response) {
				$scope.response = response
            $scope.objects = response.objects
          console.log("response is ", $scope.response)
			});
        }

        $scope.ArtworkSelected = function(artwork) {
            $scope.artwork = artwork
        }

        $scope.ArtworkDeselected = function() {
            $scope.artwork = undefined
        }

        //
        //	Initial load
        //
        $scope.reload()
}]);
