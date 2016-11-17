angular.module('ArtSnob')
.controller('artistsController', ['$scope', '$rootScope', '$timeout', 'Artists', 'SingleArtist',
    function($scope, $rootScope, $timeout, Artists, SingleArtist) {
        'use strict';

        $scope.reload = function() {
			Artists.get(function(response) {
				$scope.response = response
                $scope.objects = response.objects
			});
        }

        $scope.ArtistSelected = function(artist) {
            $scope.artist = artist
        }

        $scope.ArtistDeselected = function() {
            $scope.artist = undefined
        }

        $scope.ArtworkSelected = function(artwork_id) {
            $rootScope.$broadcast('rootScope:artworkSelected', artwork_id);
        }

        $scope.sortType     = 'name'; // set the default sort type
        $scope.sortReverse  = false;  // set the default sort order
        
        $rootScope.$on('rootScope:artistSelected', function (event, data) {
            SingleArtist.get( data, function(artistData) { 
                $scope.artist = artistData 
                console.log("scope artist:");
                console.log($scope.artist);
            });

        });



        //
        //	Initial load
        //
        $scope.reload()
}]);
