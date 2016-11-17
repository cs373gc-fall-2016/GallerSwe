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

        $scope.StyleSelected = function(style_id) {
            $rootScope.$broadcast('rootScope:styleSelected', style_id);
        }

        //listens to see if artwork is selected from a different model
        $rootScope.$on('rootScope:artworkSelected', function (event, data) {
            //this is where we will set artwork once we know how to request from API with an ID
            console.log("Artwork selected with id: "+ data);
        });

        $scope.sortType     = 'title'; // set the default sort type
        $scope.sortReverse  = false;  // set the default sort order

        //
        //	Initial load
        //
        $scope.reload()
}]);
