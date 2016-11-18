angular.module('ArtSnob')
.controller('mainController', ['$scope', '$rootScope', '$location',
    function($scope, $rootScope, $location) {
      $scope.search = function() {
          $rootScope.$broadcast('rootScope:searchTerm', searchTerm);
      }

    }]);
