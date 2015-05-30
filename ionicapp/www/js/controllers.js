angular.module('freshpicksb.controllers', ['ionic', 'firebase'])

.controller('LoginCtrl', function(
  $scope,
  $location,
  LoginFactory,
  $firebaseObject) {

  var refGrowers = new Firebase('https://brilliant-torch-3697.firebaseio.com');

  $scope.loginData = {};

  $scope.login = function() {
    LoginFactory.authenticateGrower($scope.loginData)
      .then(function(response) {
        console.log(response);
        if (response.data && response.data.username === $scope.loginData.username) {
          LoginFactory.storeUser(response.data.username);
          $location.path("/home");
        }
      });
  }

  $scope.createAccount = function() {
    $location.path("/tab/general");
    console.log("clicked");
  }
})

.controller('HomeCtrl', function() {
  console.log("home");
})

.controller('CreateAccountCtrl', function($scope) {
  $scope.create = {};

  $scope.createAccount = function() {
    console.log($scope.create);
  };
})

.controller('NewPickCtrl', function($scope, LoginFactory) {
  console.log("newpick");

  $scope.schedule = {};
  $scope.selectedProduce = {};

  $scope.userProduce = [];

  $scope.timeOfDay = 'Open';

  $scope.newpick = {};

  console.log("username", LoginFactory.getStoredUser());

  LoginFactory.getUserProduce(LoginFactory.getStoredUser())
    .then(function(res) {
      // console.log(res);

      res.data.forEach(function(produce) {
        // console.log(produce);
        for (var key in produce) {
          $scope.userProduce.push(key);
        }
      });
    });


  $scope.scheduleActive = function(e) {
    if ($scope.schedule[e]) {
      delete $scope.schedule[e];
    } else {
      $scope.schedule[e] = true;
    }
    console.log($scope.schedule);
  };

  $scope.produceActive = function(produce) {
    if ($scope.selectedProduce[produce]) {
      delete $scope.selectedProduce[produce];
    } else {
      $scope.selectedProduce[produce] = true;
    }
    console.log($scope.selectedProduce);
  }

  $scope.setActive = function(type) {
    $scope.active = type;
  };

  $scope.isActive = function(type) {
    return type === $scope.active;
  };

  $scope.submitSchedule = function() {

    var q = {
      schedule: {
        days: $scope.schedule,
        produce: $scope.selectedProduce,
        times: $scope.timeOfDay,
        notes: $scope.newpick.notes
      }
    };

    LoginFactory.postSchedule(LoginFactory.getStoredUser(), q)
      .then(function(res) {
        console.log(res);
        alert("submitted");
      })
  }

})

.controller('GeneralCtrl', function($scope, $location, LoginFactory) {
  console.log("general");

  $scope.create = {};

  $scope.setupProduce = function() {

    // save the data
    LoginFactory.createAccount($scope.create)
      .then(function(res) {
        console.log(res);

        LoginFactory.storeUser(res.data.username);
        console.log(LoginFactory.getStoredUser());

        //move to the produce profile_images
        $location.path("/tab/produce");
      });



    // $location.path("/tab/produce");
  };
})

.controller('ProduceCtrl', function($scope, LoginFactory, $location) {
  $scope.produce = {};

  $scope.produceSelection = {};

  LoginFactory.getProduce()
    .then(function(response) {
      console.log(response.data);

      $scope.produce = response.data;
    });

  $scope.createProduce = function() {
    console.log($scope.produceSelection);

    var produceArray = [];

    for (var key in $scope.produceSelection) {

      console.log(key, $scope.produceSelection[key]);
      var obj = {};
      obj[key] = $scope.produceSelection[key];
      produceArray.push(obj);
    }

    console.log(produceArray);

    LoginFactory.postProduce(LoginFactory.getStoredUser(), {
      produce: produceArray
    }).then(function(res) {
      if (res.status === 200) {
        $location.path("/home");
      }
    });




  };


});
