angular.module('ArtSnob')
.controller('artworkController', ['$scope', 'Artwork',
    function($scope, Artwork) {
        'use strict';
        
        $scope.reload = function() {
			Artwork.get(function(response) {
				$scope.response = response
                $scope.objects = response.objects
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