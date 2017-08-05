// Module documentation https://docs.angularjs.org/guide/module
var app = angular.module("helloPython", ["ngRoute"]);
/*************************************************************************************** 
1. "app" is defined on the global scope so we can attach controllers to it in other files
2. "helloPython" is the module name that we assigned to ng-app so angular will look for this
3. ["ngRoute"] this list is an example of angulars dependency injection which will give
    the helloPython module the ability to use the ngRoute module. This list can be modified
    to bring in mode modules. Typically "ngAnimate" is also found here
***************************************************************************************/  

/*************************************************************************************** 
This code sets up the built in client side routing which will enable the page
to behave as a single page application, SPA, when we go to 'ourpage.com/' angular
will insert the main.htm content into the <div ng-view></div> component and 
when we go to ourpage.com/#/test angular will insert test.htm and bind the 
test controller javascript to control it's behavior 
***************************************************************************************/  
app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "/static/views/main.htm"
    })
    .when("/test", {
        templateUrl : "/static/views/test.htm",
        controller: "testCtrl"
    })
});