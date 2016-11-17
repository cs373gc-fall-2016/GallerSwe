angular.module("ArtSnob", ['ui.router', 'ngResource', 'smart-table']);

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
	.state('about', {
		url: '/about',
		templateUrl: 'about/template.html',
		resolve: {
			// timestamps: ['Timestamps', function (TimestampService) {
			// 	return TimestampService.getAll();
			// }]
		},
		controller: 'aboutController'
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
		url: '/artwork',
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

	.state('states', {
		url: '/states',
		templateUrl: 'visual/index.html',
		resolve: {
			// timestamps: ['Timestamps', function (TimestampService) {
			// 	return TimestampService.getAll();
			// }]
		},
		controller: ''
	})

	$urlRouterProvider.otherwise('/main');
}])
