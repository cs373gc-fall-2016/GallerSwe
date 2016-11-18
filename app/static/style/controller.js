angular.module('ArtSnob')
.controller('stylesController', ['$scope', '$rootScope', '$timeout', 'Style', 'SingleStyle', 'localStorageService',
    function($scope, $rootScope, $timeout, Style, SingleStyle, localStorageService) {
        'use strict';
        SingleStyle.registerObserverCallback(gotStyle($scope));

        $scope.reload = function() {
			Style.get(function(response) {
				$scope.response = response
                $scope.objects = response.objects
                $scope.rowCollection = response.objects;
			});
        }

        $scope.StyleSelected = function(style) {
            $scope.style = style
        }

        $scope.StyleDeselected = function() {
            $scope.style = undefined
        }

        $scope.ArtworkSelected = function(artwork_id) {
            console.log("artwork id");
            console.log(artwork_id);
            $rootScope.$broadcast('rootScope:artworkSelected', artwork_id);
        }

        $rootScope.$on('rootScope:styleSelected', function (event, data) {
            console.log("Style selected with id: "+ data);
            SingleStyle.get( data, function(callback) {
                localStorageService.set("style", callback);
            });
        });

        $scope.sortType     = 'name'; // set the default sort type
        $scope.sortReverse  = false;  // set the default sort order

        function gotStyle($scope) {
            $timeout(function() {
                if (localStorageService.isSupported){
                    var tempStyle = localStorageService.get("style");
                    if (tempStyle != undefined){
                        $scope.style = tempStyle;
                        localStorageService.set("style", undefined);
                        tempStyle = undefined;
                    }
                } 
            }, 2000); 
        }
        //
        //	Initial load
        //
        $scope.reload()
}]);
