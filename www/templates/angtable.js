var app = angular.module('myApp', []);
app.controller('customersCtrl', function($scope, $http) {
    $http.get("http://127.0.0.1:5004/customers.html")
	.then(function (response) {console.log(response);
				   $scope.names = response.data.records;
				   $scope.pathname = response.data.pathname;
				   console.log("response=" + response.data);
				   console.log("names=" + $scope.names);
				  });
    window.alert("alert1");
});

/*
app.controller('myCtrl', function($scope, $http) {
    $http.get("wrongfilename.htm")
    .then(function(response) {
        //First function handles success
        $scope.content = response.data;
    }, function(response) {
        //Second function handles error
        $scope.content = "Something went wrong";
    });
});
*/
