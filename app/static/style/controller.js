angular.module('ArtSnob')
.controller('stylesController', ['$scope', '$rootScope', 'Style',
    function($scope, $rootScope, Style) {
        'use strict';

        $scope.reload = function() {
			Style.get(function(response) {
				$scope.response = response
                $scope.objects = response.objects
			});
        }

        $scope.StyleSelected = function(style) {
            $scope.style = style
        }

        $scope.StyleDeselected = function() {
            $scope.syle = undefined
        }

        $scope.ArtworkSelected = function(artwork_id) {
            $rootScope.$broadcast('rootScope:artworkSelected', artwork_id);
        }

        $rootScope.$on('rootScope:styleSelected', function (event, data) {
            //this is where we will set style once we know how to request from API with an ID
            console.log("Style selected with id: "+ data);
        });

        $scope.sortType     = 'name'; // set the default sort type
        $scope.sortReverse  = false;  // set the default sort order

        //
        //	Initial load
        //
        $scope.reload()
}]);
