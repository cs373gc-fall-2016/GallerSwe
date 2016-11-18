angular.module('ArtSnob')
.controller('collectionsController', ['$scope', '$rootScope', 'Collection',
    function($scope, $rootScope, Collection) {
        'use strict';

        $scope.reload = function() {
            Collection.get(function(response) {
                $scope.response = response
                $scope.objects = response.objects
                $scope.rowCollection = response.objects;
            });
        }


        $scope.CollectionSelected = function(collection) {
            $scope.collection = collection
        }

        $scope.CollectionDeselected = function() {
            $scope.collection = undefined
        }

        $scope.ArtworkSelected = function(artwork_id) {
            console.log(artwork_id);
            $rootScope.$broadcast('rootScope:artworkSelected', artwork_id);
        }



        //
        //  Initial load
        //
        $scope.reload()
}]);
