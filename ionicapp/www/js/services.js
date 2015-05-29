angular.module('freshpicksb.services', [])

.factory('LoginFactory', function($http, $q) {
  // Might use a resource here that returns a JSON array

  // // Some fake testing data
  // var chats = [{
  //   id: 0,
  //   name: 'Ben Sparrow',
  //   lastText: 'You on your way?',
  //   face: 'https://pbs.twimg.com/profile_images/514549811765211136/9SgAuHeY.png'
  // }, {
  //   id: 1,
  //   name: 'Max Lynx',
  //   lastText: 'Hey, it\'s me',
  //   face: 'https://avatars3.githubusercontent.com/u/11214?v=3&s=460'
  // },{
  //   id: 2,
  //   name: 'Adam Bradleyson',
  //   lastText: 'I should buy a boat',
  //   face: 'https://pbs.twimg.com/profile_images/479090794058379264/84TKj_qa.jpeg'
  // }, {
  //   id: 3,
  //   name: 'Perry Governor',
  //   lastText: 'Look at my mukluks!',
  //   face: 'https://pbs.twimg.com/profile_images/491995398135767040/ie2Z_V6e.jpeg'
  // }, {
  //   id: 4,
  //   name: 'Mike Harrington',
  //   lastText: 'This is wicked good ice cream.',
  //   face: 'https://pbs.twimg.com/profile_images/578237281384841216/R3ae1n61.png'
  // }];




  var factory = {};


  // Authenticate the user
  function authenticateUser(loginData) {
    var request = $http({
      method: "post",
      url: "xxx", //TODO
      headers: {
        'Content-Type': 'application/json'
      },
      data: loginData
    });
    return (request.then(handleSuccess, handleError));
  }

  function createAccount(account) {
    var request = $http({
      method: "post",
      url: "xxx", // TODO:
      headers: {
        'Content-Type': 'application/json'
      },
      data: account
    });
    return (request.then(handleSuccess, handleError));
  }

  // Transform the error response, unwrapping the application data from the API response payload
  function handleError(response) {
    return (response);
  }

  // Transform the successful response, unwrapping the application data from the API response payload
  function handleSuccess(response) {
    return (response);
  }





  factory.authenticateUser = authenticateUser;

  return factory;
  
});
