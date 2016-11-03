angular.module("ArtSnob", ['ui.router', 'ngResource']);

angular.module('ArtSnob').config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
	$stateProvider
	.state('main', {
		url: '/main',
		templateUrl: 'main/template.html',
		resolve: {
			// timestamps: ['Timestamps', function (TimestampService) {
			// 	return TimestampService.getAll();
			// }]
		},
		controller: 'mainController'
	})
	.state('artists', {
		url: '/artists',
		templateUrl: 'artists/template.html',
		resolve: {
			// timestamps: ['Timestamps', function (TimestampService) {
			// 	return TimestampService.getAll();
			// }]
		},
		controller: 'artistsController'
	})

	.state('artwork', {
		url: '/artworks',
		templateUrl: 'artwork/template.html',
		resolve: {
			// timestamps: ['Timestamps', function (TimestampService) {
			// 	return TimestampService.getAll();
			// }]
		},
		controller: 'artworkController'
	})
	 
	.state('styles', {
		url: '/styles',
		templateUrl: 'style/template.html',
		resolve: {
			// timestamps: ['Timestamps', function (TimestampService) {
			// 	return TimestampService.getAll();
			// }]
		},
		controller: 'stylesController'
	})

	.state('collections', {
		url: '/collections',
		templateUrl: 'collections/template.html',
		resolve: {
			// timestamps: ['Timestamps', function (TimestampService) {
			// 	return TimestampService.getAll();
			// }]
		},
		controller: 'collectionsController'
	})

	$urlRouterProvider.otherwise('/main');
}])