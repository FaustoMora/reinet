var redInn = angular.module('redInn',['ngResource','ngAnimate']);

redInn.controller('IncubacionController',['$scope','Incubacion',function($scope,Incubacion){
    this.incubaciones = Incubacion.query();

    this.isToday = function(fecha){
        return fecha = Date.now();
    }
}])


redInn.factory('Incubacion',['$resource',function($resource){
    return $resource('../list-incubaciones',{},{query:{method:"GET",params:{},isArray:true}});
}])