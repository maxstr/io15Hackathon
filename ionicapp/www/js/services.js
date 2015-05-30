angular.module('freshpicksb.services', ['firebase'])

.factory('LoginFactory', function($http, $q, $firebaseObject) {

  var factory = {};
  var loggedInUser;


  // Authenticate the user
  function authenticateGrower(loginData) {
    var request = $http({
      method: "GET",
      url: "https://brilliant-torch-3697.firebaseio.com/growers/" + loginData.username + ".json", //TODO
      headers: {
        'Content-Type': 'application/json'
      },
      data: loginData
    });

    return (request.then(handleSuccess, handleError));
  }

  function createAccount(account) {
    var request = $http({
      method: "PUT",
      url: "https://brilliant-torch-3697.firebaseio.com/growers/" + account.username + ".json",
      headers: {
        'Content-Type': 'application/json'
      },
      data: account
    });
    return (request.then(handleSuccess, handleError));
  }

  function getProduce() {
    var request = $http({
      method: "GET",
      // url: "http://freshpicksb.appspot.com/produce",
      url: "https://brilliant-torch-3697.firebaseio.com/produce.json", // TODO:
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return (request.then(handleSuccess, handleError));
  }

  function postProduce(username, produce) {
    console.log(JSON.stringify(produce));
    var request = $http({
      method: "PATCH",
      url: "https://brilliant-torch-3697.firebaseio.com/growers/" + username + ".json",
      headers: {
        'Content-Type': 'application/json'
      },
      data: produce
    });
    return (request.then(handleSuccess, handleError));
  }

  function getUserProduce(username) {
    var request = $http({
      method: "GET",
      url: "https://brilliant-torch-3697.firebaseio.com/growers/" + username + "/produce.json",
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return (request.then(handleSuccess, handleError));
  }

  function postSchedule(username, schedule) {
    console.log(JSON.stringify(schedule));
    var request = $http({
      method: "PATCH",
      url: "https://brilliant-torch-3697.firebaseio.com/growers/" + username + ".json",
      headers: {
        'Content-Type': 'application/json'
      },
      data: schedule
    });
    return (request.then(handleSuccess, handleError));
  }



  // function getEmailFromStoredUser() {
  //   if (loggedInUser) {
  //     return loggedInUser.user_email;
  //   }
  // }


  function storeUser(account) {
    console.log("attempting to store user", account);
    loggedInUser = account;
  }

  function getStoredUser() {
    return loggedInUser;
  }





  // Transform the error response, unwrapping the application data from the API response payload
  function handleError(response) {
    return (response);
  }

  // Transform the successful response, unwrapping the application data from the API response payload
  function handleSuccess(response) {
    return (response);
  }





  factory.authenticateGrower = authenticateGrower;
  factory.createAccount = createAccount;
  factory.storeUser = storeUser;
  factory.getStoredUser = getStoredUser;
  factory.getProduce = getProduce;
  factory.postProduce = postProduce;
  factory.getUserProduce = getUserProduce;
  factory.postSchedule = postSchedule;

  return factory;

});
