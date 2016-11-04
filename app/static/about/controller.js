angular.module('ArtSnob')
.controller('aboutController', ['$scope', 'About',
    function($scope, About) {
        'use strict';
        
        $scope.buttonClick = function() {
            $scope.hasClickedButton = true;
			About.get(function(response) {
				$scope.response = response
			});
        }

        //
        //	Initial load
        //
        $scope.reload()
}]);