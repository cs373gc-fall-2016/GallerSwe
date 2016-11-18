angular.module('ArtSnob')
.controller('artworkController', ['$scope', '$rootScope','$timeout', 'Artwork', 'SingleArtwork', 'localStorageService',
    function($scope, $rootScope, $timeout, Artwork, SingleArtwork, localStorageService) {
        'use strict';
        SingleArtwork.registerObserverCallback(gotArtwork($scope));

        $scope.reload = function() {
			Artwork.get(function(response) {
                $scope.objects = response.objects
                $scope.rowCollection = response.objects;
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
            console.log("heard broadcast");
            console.log(data);
            SingleArtwork.get( data, function(callback) {
                localStorageService.set("artwork", callback);
            });
        });

        function gotArtwork($scope) {
            $timeout(function() {
                if (localStorageService.isSupported){
                    var tempArtwork = localStorageService.get("artwork");
                    if (tempArtwork != undefined){
                        $scope.artwork = tempArtwork;
                        localStorageService.set("artwork", undefined);
                        tempArtwork = undefined;
                    }
                } 
            }, 2000); 
        }

        $scope.sortType     = 'title'; // set the default sort type
        $scope.sortReverse  = false;  // set the default sort order

        //
        //	Initial load
        //
        $scope.reload()
}]);
