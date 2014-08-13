var todoApp = angular.module('todoApp', []);

todoApp.service('dataService', function($http) {
    delete $http.defaults.headers.common['X-Requested-With'];
    this.getData = function() {
        // $http() returns a $promise that we can add handlers with .then()
        return $http({
            method: 'GET',
            url: '/todos/?format=json',
            //params: 'limit=10',
            headers: {'Authorization': 'bearer f44ba59438f607a23517c423ccb38e9aa798dfeb'}
        });
    }
    this.postData = function(description) {
        // $http() returns a $promise that we can add handlers with .then()
        return $http({
            method: 'POST',
            url: '/todos/?format=json',
            headers: {'Authorization': 'bearer f44ba59438f607a23517c423ccb38e9aa798dfeb'},
            data: {
                description: description, done: false
            }
        });
    }
    this.putData = function(id, description, done) {
        // $http() returns a $promise that we can add handlers with .then()
        return $http({
            method: 'PUT',
             url: '/todo/'+id+'?format=json',
            headers: {'Authorization': 'bearer f44ba59438f607a23517c423ccb38e9aa798dfeb'},
            data: {
                id: id, description: description, done: done
            }
        });
    }
    this.deleteData = function(id) {
        // $http() returns a $promise that we can add handlers with .then()
        return $http({
            method: 'DELETE',
            url: '/todo/'+id+'?format=json',
            headers: {'Authorization': 'bearer f44ba59438f607a23517c423ccb38e9aa798dfeb'},
            data: {
                id: id
            }
        });
    }
});




todoApp.controller('TodoCtrl', ['$scope', 'dataService', function($scope, dataService) {
   /* $scope.todos = [{description: "have a good sleep tonight", done:false},
        {description: "read \"Pro AngularJS\" book", done:false},
        {description: "eat some burgers", done:false},
        {description: "read \"Instant Django Application Development\" book", done:true},
        {description: "finish this project", done:false},
        {description: "watch lynda.com angularjs tutorials", done:true},
        {description: "read \"Two spoons of django\" book", done:false},
        {description: "start this project and commit to github", done:true}
    ];
    console.log($scope.todos);
*/
    //get data from REST
    $scope.todos = null;
    dataService.getData().then(function (dataResponse) {
        $scope.todos = dataResponse.data;
        console.log($scope.todos);
    });



    $scope.toggleTodo = function(todo) {
        todo.done ? todo.done = false : todo.done = true;
        dataService.putData(todo.id, todo.description, todo.done).then(function (dataResponse) {
        });
    };



    $scope.addTodo = function () {
        var newTodo = $scope.newTodo.trim();
        if (!newTodo.length) {
            return;
        }

        dataService.postData(newTodo).then(function (dataResponse) {
            $scope.todos.push({
                description: newTodo,
                done: false
            });
        });


        $scope.newTodo = '';
    };

    $scope.deleteTodo = function (todo) {
        dataService.deleteData(todo.id).then(function (dataResponse) {
            $scope.todos.splice($scope.todos.indexOf(todo), 1);
        });
    };

    $scope.editTodo = function (todo) {
        $scope.editedTodo = todo;
// Clone the original todo to restore it on demand.
        $scope.originalTodo = angular.extend({}, todo);
    };

    $scope.doneEditing = function (todo) {
        dataService.putData(todo.id, todo.description, todo.done).then(function (dataResponse) {
            $scope.editedTodo = null;
            todo.description = todo.description.trim();
        });

        if (!todo.description) {
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



    $scope.editTag = function (tag) {
        $scope.editedTag = tag;
// Clone the original todo to restore it on demand.
        $scope.originalTag = angular.extend({}, tag);
    };

    $scope.doneEditingTag = function (tag) {
        $scope.editedTag = null;
        tag.name = tag.name.trim();

        if (!tag.name) {
            $scope.deleteTag(tag);
        }
    };

    $scope.revertEditingTag = function (tag) {
        $scope.tags[$scope.tags.indexOf(tag)] = $scope.originalTag;
        $scope.doneEditing($scope.originalTag);
    };

}]);;