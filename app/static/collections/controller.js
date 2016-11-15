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

        //
        //  Initial load
        //
        $scope.reload()
}]);