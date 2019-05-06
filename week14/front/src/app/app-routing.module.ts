import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {MainComponent} from './main/main.component';
import {TodolistComponent} from './todolist/todolist.component';
import {TodotasksComponent} from './todotasks/todotasks.component';

const routes: Routes = [
  {path:'task_list', component: TodolistComponent},
  {path: 'task_list/:id/task', component: TodotasksComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
