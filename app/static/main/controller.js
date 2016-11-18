angular.module('ArtSnob')
.controller('mainController', ['$scope', '$rootScope', '$location',
    function($scope, $rootScope, $location) {
      
      $scope.search = function() {
      	  var searchTerm = $scope.searchTerm;
          $rootScope.$broadcast('rootScope:searchTerm', searchTerm);
          console.log("I am broadcasting");
          console.log(searchTerm);
      }

    }]);
