angular.module('ArtSnob')
.controller('resultsController', ['$scope', '$rootScope', 'Result',
    function($scope, $rootScope, Result) {

    $rootScope.$on('rootScope:searchTerm', function (event, data) {
        console.log("getting this :" + data)
        results.get( data, function(artistData) {
            $scope.objects = artistData
        });
      });
}]);
