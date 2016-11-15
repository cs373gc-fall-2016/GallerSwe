angular.module('ArtSnob')
.controller('artworkController', ['$scope', '$rootScope', 'Artwork',
    function($scope, $rootScope, Artwork) {
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

        $scope.ArtistSelected = function(artist_id) {
            $rootScope.$broadcast('rootScope:artistSelected', artist_id);
        }

        //
        //	Initial load
        //
        $scope.reload()
}]);
