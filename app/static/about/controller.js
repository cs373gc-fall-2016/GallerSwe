angular.module('ArtSnob')
.controller('aboutController', ['$scope', 'About',
    function($scope, About) {
        'use strict';
        
        $scope.reload = function() {
        }

        $scope.buttonClick = function() {
			About.get(function(response) {
                console.log("running tests");
				$scope.response = response
			});
        }

        //
        //	Initial load
        //
        $scope.reload()
}]);