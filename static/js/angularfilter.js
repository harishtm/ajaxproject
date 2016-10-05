var app = angular.module("myfilter",[]);

app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[')
    $interpolateProvider.endSymbol(']]')
});

app.controller("student-data", function($scope){
    $scope.AllStudentList = all_student_data;
//    var stId = $routeParams.pk;
});


