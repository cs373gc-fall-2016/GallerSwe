angular.module('ArtSnob')
.controller('mainController', ['$scope', '$rootScope', '$location', '$timeout',
    function($scope, $rootScope, $location, $timeout) {
      
      $scope.reload = function() {
        }

      $scope.search = function() {
      	  var searchTerm = $scope.searchTerm;
          $timeout(function(){
            $rootScope.$broadcast('rootScope:searchTerm', searchTerm);
          }, 500);
          console.log("I am broadcasting");
          console.log(searchTerm);
      }

    }]);
