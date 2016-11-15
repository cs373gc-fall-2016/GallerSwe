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

        //
        //	Initial load
        //
        $scope.reload()
}]);