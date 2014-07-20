var todoApp = angular.module('todoApp',[]);


todoApp.controller('TodoCtrl', ['$scope', function($scope) {
    $scope.todos = [{subject: "have a good sleep tonight", finished:false},
        {subject: "read \"Pro AngularJS\" book", finished:false},
        {subject: "eat some burgers", finished:false},
        {subject: "read \"Instant Django Application Development\" book", finished:true},
        {subject: "finish this project", finished:false},
        {subject: "watch lynda.com angularjs tutorials", finished:true},
        {subject: "read \"Two spoons of django\" book", finished:false},
        {subject: "start this project and commit to github", finished:true}
    ];

    $scope.toggleTodo = function(todo) {
        todo.finished ? todo.finished = false : todo.finished = true;
    };



    $scope.addTodo = function () {
        var newTodo = $scope.newTodo.trim();
        if (!newTodo.length) {
            return;
        }

        $scope.todos.push({
            subject: newTodo,
            finished: false
        });

        $scope.newTodo = '';
    };

    $scope.deleteTodo = function (todo) {
        $scope.todos.splice($scope.todos.indexOf(todo), 1);
    };

    $scope.editTodo = function (todo) {
        $scope.editedTodo = todo;
// Clone the original todo to restore it on demand.
        $scope.originalTodo = angular.extend({}, todo);
    };

    $scope.doneEditing = function (todo) {
        $scope.editedTodo = null;
        todo.subject = todo.subject.trim();

        if (!todo.subject) {
            $scope.deleteTodo(todo);
        }
    };

    $scope.revertEditing = function (todo) {
        $scope.todos[$scope.todos.indexOf(todo)] = $scope.originalTodo;
        $scope.doneEditing($scope.originalTodo);
    };

    /////////////////////////////////////////
    // TAGS //todo - move to tagsCtrl.js
    ////////////////////////////////////////

    $scope.tags = [{name: "@home"},
            {name: "@work"},
            {name: "Next"},
    ];


    $scope.addTag = function () {
        var newTag = $scope.newTag.trim();
        if (!newTag.length) {
            return;
        }

        $scope.tags.push({
            name: newTag
        });

        $scope.newTag = '';
    };

    $scope.deleteTag = function (tag) {
        $scope.tags.splice($scope.tags.indexOf(tag), 1);
    };


}]);