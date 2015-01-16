var redInn = angular.module('redInn',['ngRoute']);

redInn.config(['$routeProvider',function($routeProvider){
    $routeProvider.
    when('/institucion/incubaciones',{
        templateUrl:'partials/incubacion_institucion.html',}).
    when('/institucion/incubaciones/incubacion1',{
        templateUrl:'partials/incubacion1_institucion.html',
        controller:'incubaController'}).
    when('/institucion/incubaciones/crear',{
        templateUrl:'partials/crear_incubacion.html',})
    .otherwise('/institucion/incubaciones',{
        templateUrl:'partials/incubacion_institucion.html',});



}]);


redInn.controller('mainController',['$scope','$location',function($scope,$location){
    $scope.go = function(url){
        $location.path(url);
    };
}]);

redInn.controller('createController',['$scope',function($scope){
    $scope.alcance='institucion';
}]);

redInn.controller('incubaController',['$scope',function($scope){
    $scope.modal_content=null;
    $scope.modal_possible=[
        {
            'title':'Crear Convocatoria',
            'tpl':'partials/crear_convocatoria.html'
        },
        {
            'title':'Invitar Consultor',
            'tpl':'partials/invitar_consultor.html'
        },
        {
            'title':'Crear Milestone',
            'tpl':'partials/crear_milestone.html'
        },
        {
            'title':'Aumentar Alcance',
            'tpl':'partials/aumentar_alcance.html'
        },
        {
            'title':'Terminar Incubacion',
            'tpl':'partials/terminar_incubacion.html'
        },
        {
            'title':'Suspender Incubacion',
            'tpl':'partials/suspender_incubacion.html'
        }
    ];
    
    $scope.setModal = function(n){
        $scope.modal_content=$scope.modal_possible[n];
    };
}]);