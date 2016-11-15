angular.module('ArtSnob')
.controller('artistsController', ['$scope', '$rootScope', 'Artists',
    function($scope, $rootScope, Artists) {
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

        $scope.ArtworkSelected = function(artwork_id) {
            $rootScope.$broadcast('rootScope:artworkSelected', artwork_id);
        }

        $scope.sortType     = 'name'; // set the default sort type
        $scope.sortReverse  = false;  // set the default sort order
        
        //listens to see if artist is selected from a different model
        $rootScope.$on('rootScope:artistSelected', function (event, data) {
            //this is where we will set artist once we know how to request from API with an ID
            console.log("Artist selected with id: "+ data);
        });

        //
        //	Initial load
        //
        $scope.reload()
}]);
