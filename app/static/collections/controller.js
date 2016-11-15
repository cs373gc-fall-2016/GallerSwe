angular.module('ArtSnob')
.controller('collectionsController', ['$scope', '$rootScope', 'Collection',
    function($scope, $rootScope, Collection) {
        'use strict';

        $scope.reload = function() {
            Collection.get(function(response) {
                $scope.response = response
                $scope.objects = response.objects
            });
        }

        $scope.CollectionSelected = function(collection) {
            $scope.collection = collection
        }

        $scope.CollectionDeselected = function() {
            $scope.collection = undefined
        }

        $scope.ArtworkSelected = function(artwork_id) {
            $rootScope.$broadcast('rootScope:artworkSelected', artwork_id);
        }

        $scope.sortType     = 'institution'; // set the default sort type
        $scope.sortReverse  = false;  // set the default sort order

        //
        //  Initial load
        //
        $scope.reload()
}]);
