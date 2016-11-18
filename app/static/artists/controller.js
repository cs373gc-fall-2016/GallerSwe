angular.module('ArtSnob')
.controller('artistsController', ['$scope', '$rootScope', '$timeout', 'Artists', 'SingleArtist', 'localStorageService',
    function($scope, $rootScope, $timeout, Artists, SingleArtist, localStorageService) {
        'use strict';
        SingleArtist.registerObserverCallback(gotArtist($scope));



        $scope.reload = function() {
			Artists.get(function(response) {
				$scope.response = response
                $scope.objects = response.objects
                $scope.rowCollection = response.objects
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
                console.log("setting local"); 
                localStorageService.set("artist", artistData);
            });

        });

        function gotArtist($scope) {
            console.log("in gotArtist");
            $timeout(function() {
                if (localStorageService.isSupported){
                        var maybeArtist = localStorageService.get("artist");
                        if (maybeArtist != undefined){
                            $scope.artist = maybeArtist;
                            localStorageService.set("artist", undefined);
                            maybeArtist = undefined;
                        }
                } 
            }, 2000); 
        }


        //
        //	Initial load
        //
        $scope.reload()
}]);
