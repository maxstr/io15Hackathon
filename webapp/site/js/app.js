
	var app = angular.module('freshpick',['ngRoute'])

	.controller('IndexCtrl', function ($scope, $routeParams) {
		$scope.index;
	})

	.controller('UserFormCtrl', function($scope, $routeParams) {

	})
	.config(function($routeProvider) {
		$routeProvider

		.when('/', {templateUrl: '/site/pages/index.html',
					controller: 'IndexCtrl'
		})
		.when('/userForm', {templateUrl: '/site/pages/user_form.html',
							controller: 'UserCtrl'

		})

	});
	
