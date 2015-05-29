angular.module('freshpicksb.controllers', [])

.controller('LoginCtrl', function(
  $scope,
  $location,
  LoginFactory) {


  $scope.loginData = {};

  $scope.login = function() {
    console.log($scope.loginData.email);
    console.log($scope.loginData.password);

    LoginFactory.authenticateUser($scope.loginData)
      .then(function(response) {
        console.log(response);
      });

  }


  $scope.createAccount = function() {
    $location.path("/createAccount");
    console.log("clicked");
  }
})

.controller('CreateAccountCtrl', function($scope) {
  $scope.create = {};

  $scope.createAccount = function () {
    console.log($scope.create);
  };


})

.controller('GeneralCtrl', function($scope, $location) {
  console.log("general");

  $scope.setupProduce = function () {
    // console.log("inside");
    $location.path("/tab/produce");
  };
})

.controller('ChatsCtrl', function($scope, Chats) {
  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  }
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('AccountCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
});
