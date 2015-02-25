var redInn = angular.module('redInn',['ngResource','ngAnimate']);

redInn.controller('IncubacionController',['$scope','Incubacion',function($scope,Incubacion){
    this.incubaciones = Incubacion.query();

    this.isToday = function(fecha){
        return Date(fecha) == Date.now();
    }
}])


redInn.factory('Incubacion',['$resource',function($resource){
    return $resource('../list-incubaciones',{},{query:{method:"GET",params:{},isArray:true}});
}])

redInn.controller('crearIncubacionController',['$scope','$filter',function($scope) {
    this.fecha=new Date();
    this.nombre=null;
    this.descripcion=null;
    this.condiciones=null;
    this.perfiles=null;
    this.tipos={};
    this.alcance=0;
}])